import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import Mock, patch

import requests

from scraper.company import (
    build_asset_filename,
    build_company_page_url,
    build_summary,
    build_table_of_contents,
    collect_company_post_metadata,
    collect_company_post_metadata_from_files,
    collect_company_post_targets,
    collect_company_post_targets_from_files,
    combine_company_posts,
    download_post_assets,
    extract_position_type_tag,
    extract_published_date,
    fetch_company_page_html,
    fetch_company_input_pages,
    limit_input_html_files,
    load_company_input_files,
    inject_post_tags_into_markdown,
    is_http_403_or_429_error,
    run_company_scrape,
    sanitize_filename,
)
from scraper.cli import extract_post_id, format_post_markdown, save_post_content
from scraper import (
    DownloadableAsset,
    ScrapedPost,
    apply_cookie_header,
    build_authenticated_session,
    parse_post_ids_from_html_file,
    parse_post_html,
    scrape_post,
)
from scraper.forum import parse_post_records_from_html
from scraper.post import DEBUG_HTML_DIR, RequestLimitExceededError, _rate_limited_get


class ParsePostHtmlTests(unittest.TestCase):
    def test_extracts_core_fields(self) -> None:
        html = """
        <html>
          <head>
            <title>Fallback Title</title>
          </head>
          <body>
            <div class="comiis_viewbox">
              <h1>How I Prepared for My Interview</h1>
              <div class="authi">
                <a class="xw1" href="/user/42">test_user</a>
                <em><time datetime="2026-05-01T14:30:00+00:00">2026-05-01</time></em>
              </div>
              <div class="comiis_message">
                <p>First paragraph.</p>
                <p>Second paragraph.</p>
              </div>
            </div>
          </body>
        </html>
        """

        post = parse_post_html(
            html,
            url="https://www.1point3acres.com/home/pins/1176924",
        )

        self.assertEqual(
            post.url,
            "https://www.1point3acres.com/home/pins/1176924",
        )
        self.assertEqual(post.title, "How I Prepared for My Interview")
        self.assertEqual(post.author, "test_user")
        self.assertEqual(post.published_at, "2026-05-01T14:30:00+00:00")
        self.assertEqual(post.content, "First paragraph.\nSecond paragraph.")

    def test_uses_title_tag_as_fallback(self) -> None:
        html = """
        <html>
          <head>
            <title>Thread Title From Head</title>
          </head>
          <body>
            <div class="message">Post body text.</div>
          </body>
        </html>
        """

        post = parse_post_html(html, url="https://example.com/post")

        self.assertEqual(post.title, "Thread Title From Head")
        self.assertEqual(post.content, "Post body text.")

    def test_apply_cookie_header_populates_session(self) -> None:
        import requests

        session = requests.Session()
        apply_cookie_header(
            session,
            "foo=bar; fizz=buzz",
            domain=".1point3acres.com",
        )

        self.assertEqual(session.cookies.get("foo"), "bar")
        self.assertEqual(session.cookies.get("fizz"), "buzz")

    def test_build_authenticated_session_reads_env_file(self) -> None:
        with TemporaryDirectory() as temp_dir:
            env_path = Path(temp_dir) / ".env"
            env_path.write_text(
                "SCRAPER_COOKIE_HEADER='foo=bar; fizz=buzz'\n"
                "SCRAPER_MIN_REQUEST_INTERVAL='0.25'\n",
                encoding="utf-8",
            )

            session = build_authenticated_session(env_file=str(env_path))

        self.assertEqual(session.cookies.get("foo"), "bar")
        self.assertEqual(session.cookies.get("fizz"), "buzz")
        self.assertEqual(session.cookies.get_dict(domain=".1point3acres.com")["foo"], "bar")
        self.assertEqual(session.headers["User-Agent"], "scraper/1.0 (+polite rate-limited requests)")
        self.assertEqual(getattr(session, "_scraper_min_request_interval"), 0.25)
        self.assertEqual(getattr(session, "_scraper_request_interval_jitter"), 2.0)

    def test_build_authenticated_session_reads_request_interval_jitter(self) -> None:
        with TemporaryDirectory() as temp_dir:
            env_path = Path(temp_dir) / ".env"
            env_path.write_text(
                "SCRAPER_COOKIE_HEADER='foo=bar; fizz=buzz'\n"
                "SCRAPER_REQUEST_INTERVAL_JITTER='1.5'\n",
                encoding="utf-8",
            )

            session = build_authenticated_session(env_file=str(env_path))

        self.assertEqual(getattr(session, "_scraper_min_request_interval"), 10.0)
        self.assertEqual(getattr(session, "_scraper_request_interval_jitter"), 1.5)

    def test_build_authenticated_session_reads_raw_cookie_file(self) -> None:
        with TemporaryDirectory() as temp_dir:
            env_path = Path(temp_dir) / ".env"
            env_path.write_text(
                "foo=bar; fizz=buzz",
                encoding="utf-8",
            )

            session = build_authenticated_session(env_file=str(env_path))

        self.assertEqual(session.cookies.get("foo"), "bar")
        self.assertEqual(session.cookies.get("fizz"), "buzz")
        self.assertEqual(
            session.cookies.get_dict(domain=".1point3acres.com")["foo"],
            "bar",
        )

    def test_build_authenticated_session_reads_request_cookie_constant(self) -> None:
        with (
            patch("scraper.post.REQUEST_COOKIE", "foo=bar; fizz=buzz"),
            patch("scraper.post.Path.exists", return_value=False),
        ):
            session = build_authenticated_session()

        self.assertEqual(session.cookies.get("foo"), "bar")
        self.assertEqual(session.cookies.get("fizz"), "buzz")
        self.assertEqual(
            session.cookies.get_dict(domain=".1point3acres.com")["foo"],
            "bar",
        )

    def test_scrape_post_fetches_the_human_page_url(self) -> None:
        session = Mock()
        response = Mock()
        response.text = """
        <html>
          <body>
            <div id="post_1">
              <div class="authi">
                <a class="xw1">地里匿名用户CJ8IF</a>
                <em><time datetime="1778883960">2026-05-15</time></em>
              </div>
              <h1>人类学昂赛</h1>
              <div class="comiis_message">
                <p>四轮昂赛</p>
                <p>coding: lru</p>
              </div>
            </div>
            <div id="post_2">
              <div class="authi">
                <a class="xw1">地里匿名用户0VWQJ</a>
                <em><time datetime="1778884780">2026-05-15</time></em>
              </div>
              <div class="comiis_message">
                <p>面的mle or sde?</p>
              </div>
            </div>
          </body>
        </html>
        """
        session.get.return_value = response

        post = scrape_post(
            "https://www.1point3acres.com/home/pins/1176924",
            session,
        )

        session.get.assert_called_once_with(
            "https://www.1point3acres.com/home/pins/1176924",
            params=None,
            timeout=30.0,
        )
        self.assertEqual(post.title, "人类学昂赛")
        self.assertEqual(post.author, "地里匿名用户CJ8IF")
        self.assertEqual(post.published_at, "1778883960")
        self.assertEqual(
            post.content,
            "四轮昂赛\ncoding: lru\n\nReplies:\n\n#2 地里匿名用户0VWQJ at 1778884780\n\n面的mle or sde?",
        )

    def test_scrape_post_falls_back_to_legacy_human_url_and_saves_debug_html(self) -> None:
        session = Mock()
        shell_response = Mock()
        shell_response.text = """
        <html>
          <body>
            <a href="/bbs/thread-1177483-1-1.html">返回旧版</a>
            <script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"tid":1177483}}}</script>
          </body>
        </html>
        """
        legacy_response = Mock()
        legacy_response.text = """
        <html>
          <head><title>Legacy Title</title></head>
          <body>
            <div id="post_1">
              <div class="authi">
                <a class="xw1">test_user</a>
                <em><time datetime="2026-05-20T12:00:00+00:00">2026-05-20</time></em>
              </div>
              <h1>人类学在线笔试+时间线</h1>
              <div class="comiis_message">
                <p>Legacy body.</p>
              </div>
            </div>
          </body>
        </html>
        """
        session.get.side_effect = [shell_response, legacy_response]

        with TemporaryDirectory() as temp_dir, patch("scraper.post.DEBUG_HTML_DIR", Path(temp_dir)):
            post = scrape_post(
                "https://www.1point3acres.com/home/pins/1177483",
                session,
            )
            initial_debug = Path(temp_dir) / "1177483_initial.html"
            legacy_debug = Path(temp_dir) / "1177483_legacy.html"
            self.assertTrue(initial_debug.exists())
            self.assertTrue(legacy_debug.exists())

        self.assertEqual(session.get.call_count, 2)
        self.assertEqual(
            session.get.call_args_list[0].args[0],
            "https://www.1point3acres.com/home/pins/1177483",
        )
        self.assertEqual(
            session.get.call_args_list[1].args[0],
            "https://www.1point3acres.com/bbs/thread-1177483-1-1.html",
        )
        self.assertEqual(post.title, "人类学在线笔试+时间线")
        self.assertEqual(post.url, "https://www.1point3acres.com/bbs/thread-1177483-1-1.html")
        self.assertEqual(post.author, "test_user")
        self.assertEqual(post.published_at, "2026-05-20T12:00:00+00:00")

    def test_scrape_post_falls_back_to_html_for_non_pin_urls(self) -> None:
        session = Mock()
        response = Mock()
        response.text = """
        <html>
          <head><title>Fallback Title</title></head>
          <body><div class="message">Fallback body.</div></body>
        </html>
        """
        session.get.return_value = response

        post = scrape_post("https://example.com/post", session)

        session.get.assert_called_once_with("https://example.com/post", params=None, timeout=30.0)
        response.raise_for_status.assert_called_once_with()
        self.assertEqual(post.title, "Fallback Title")
        self.assertEqual(post.content, "Fallback body.")

    def test_scrape_post_rate_limits_requests(self) -> None:
        session = Mock()
        session.get.return_value = Mock(
            text="<html><head><title>Body</title></head><body><div class='message'>Body.</div></body></html>"
        )
        session._scraper_min_request_interval = 1.0
        session._scraper_request_interval_jitter = 0.0
        session._scraper_last_request_time = None

        with patch("scraper.post.time.monotonic", side_effect=[10.0, 10.0, 10.2, 10.2]), patch(
            "scraper.post.time.sleep"
        ) as mock_sleep:
            scrape_post("https://example.com/post-a", session)
            scrape_post("https://example.com/post-b", session)

        mock_sleep.assert_called_once()
        self.assertAlmostEqual(mock_sleep.call_args.args[0], 0.8)

    def test_scrape_post_rate_limits_requests_with_jitter(self) -> None:
        session = Mock()
        session.get.return_value = Mock(
            text="<html><head><title>Body</title></head><body><div class='message'>Body.</div></body></html>"
        )
        session._scraper_min_request_interval = 10.0
        session._scraper_request_interval_jitter = 2.0
        session._scraper_last_request_time = 100.0

        with patch("scraper.post.time.monotonic", side_effect=[105.0, 110.0]), patch(
            "scraper.post.random.uniform",
            return_value=1.5,
        ) as mock_uniform, patch("scraper.post.time.sleep") as mock_sleep:
            scrape_post("https://example.com/post-b", session)

        mock_uniform.assert_called_once_with(0.0, 2.0)
        mock_sleep.assert_called_once_with(6.5)

    def test_rate_limited_get_stops_at_request_cap(self) -> None:
        session = Mock()
        session.get.return_value = Mock()
        session._scraper_min_request_interval = 0.0
        session._scraper_request_interval_jitter = 0.0
        session._scraper_last_request_time = None
        session._scraper_max_total_requests = 1
        session._scraper_total_requests_made = 1

        with self.assertRaises(RequestLimitExceededError):
            _rate_limited_get(session, "https://example.com", timeout=30.0)

    def test_extract_post_id_from_home_pin_url(self) -> None:
        self.assertEqual(
            extract_post_id("https://www.1point3acres.com/home/pins/1175782"),
            "1175782",
        )

    def test_save_post_content_writes_markdown_file(self) -> None:
        with TemporaryDirectory() as temp_dir:
            post = ScrapedPost(
                url="https://www.1point3acres.com/home/pins/1175782",
                title="人类学店面挂经",
                author="地里匿名用户EFMJX",
                published_at="1778089756",
                content=(
                    "Q2 LRU cache。\n\n"
                    "先fix bug，再extend。\n\n"
                    "捣鼓了一阵coderpad filepath。最后没来得及跑通。周一面的周五通知不move on了。"
                    "\n\nReplies:\n\n"
                    "#2 地里匿名用户5ARCA at 1778096572\n\n"
                    "lz用python面的吗 不知道这题有没有非python版本"
                ),
            )
            output_path = save_post_content(
                post,
                output_root=Path(temp_dir),
            )

            self.assertEqual(output_path.name, "1175782.md")
            self.assertTrue(output_path.exists())
            self.assertEqual(
                output_path.read_text(encoding="utf-8"),
                format_post_markdown(post),
            )

    def test_format_post_markdown_matches_selected_layout(self) -> None:
        post = ScrapedPost(
            url="https://www.1point3acres.com/home/pins/1175782",
            title="人类学店面挂经",
            author="地里匿名用户EFMJX",
            published_at="1778089756",
            content=(
                "Q2 LRU cache。\n\n"
                "先fix bug，再extend。\n\n"
                "捣鼓了一阵coderpad filepath。最后没来得及跑通。周一面的周五通知不move on了。"
                "\n\nReplies:\n\n"
                "#2 地里匿名用户5ARCA at 1778096572\n\n"
                "lz用python面的吗 不知道这题有没有非python版本"
            ),
        )

        expected = """# 人类学店面挂经

`Post ID: 1175782` | `Author: 地里匿名用户EFMJX` | `Published: 2026-05-06 10:49:16 PDT`

Source: https://www.1point3acres.com/home/pins/1175782

---

## Post

Q2 LRU cache。

先fix bug，再extend。

捣鼓了一阵coderpad filepath。最后没来得及跑通。周一面的周五通知不move on了。

---

## Replies

**#2 地里匿名用户5ARCA** | `2026-05-06 12:42:52 PDT`

lz用python面的吗 不知道这题有没有非python版本
"""
        self.assertEqual(format_post_markdown(post), expected)

    def test_parse_post_ids_from_html_file_extracts_fixture_ids_in_order(self) -> None:
        post_ids = parse_post_ids_from_html_file("inputs/anthropic/1.html")

        self.assertEqual(
            post_ids,
            [
                "1177660",
                "1177483",
                "1177358",
                "1177056",
                "1177035",
                "1176924",
                "1176747",
                "1176562",
                "1176508",
                "1176227",
                "1176214",
                "1176172",
                "1175918",
                "1175805",
                "1175782",
                "1175723",
                "1175489",
                "1175484",
                "1174952",
                "1174864",
            ],
        )

    def test_collect_company_post_targets_deduplicates_across_html_files(self) -> None:
        with TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "anthropic"
            input_dir.mkdir()
            html = """
            <div data-sentry-component="ForumThreadItem">
              <a href="https://www.1point3acres.com/home/pins/1175782">one</a>
            </div>
            <div data-sentry-component="ForumThreadItem">
              <a href="https://www.1point3acres.com/bbs/thread-1176000-1-1.html">two</a>
            </div>
            """
            (input_dir / "1.html").write_text(html, encoding="utf-8")
            (input_dir / "2.html").write_text(html, encoding="utf-8")

            targets = collect_company_post_targets(input_dir)

        self.assertEqual(
            targets,
            [
                "https://www.1point3acres.com/home/pins/1175782",
                "https://www.1point3acres.com/bbs/thread-1176000-1-1.html",
            ],
        )

    def test_collectors_parse_human_company_page_html(self) -> None:
        html = """
        <div data-sentry-component="ForumThreadItem">
          <a href="https://www.1point3acres.com/home/pins/1175782"><h3>人类学店面挂经</h3></a>
          <div class="text-muted-foreground mt-1 flex flex-wrap items-center gap-x-1 text-xs">
            <span class="font-bold text-orange-400">Anthropic</span>
            <span class="bg-muted-foreground"></span>
            <span>2026(4-6月)</span>
            <span class="bg-muted-foreground"></span>
            <span>全职</span>
            <span class="bg-muted-foreground"></span>
            <span>码农类</span>
            <span class="bg-muted-foreground"></span>
            <span>在职跳槽</span>
          </div>
        </div>
        <div data-sentry-component="ForumThreadItem">
          <a href="https://www.1point3acres.com/interview/post/1176214"><h3>Anthropic OA面经</h3></a>
          <div class="text-muted-foreground mt-1 flex flex-wrap items-center gap-x-1 text-xs">
            <span class="font-bold text-orange-400">Anthropic</span>
            <span class="bg-muted-foreground"></span>
            <span>2026(4-6月)</span>
            <span class="bg-muted-foreground"></span>
            <span>全职</span>
            <span class="bg-muted-foreground"></span>
            <span>应届毕业生</span>
          </div>
        </div>
        """

        with TemporaryDirectory() as temp_dir:
            html_path = Path(temp_dir) / "1.html"
            html_path.write_text(html, encoding="utf-8")

            targets = collect_company_post_targets_from_files([html_path])
            metadata = collect_company_post_metadata_from_files([html_path])

        self.assertEqual(
            targets,
            [
                "https://www.1point3acres.com/home/pins/1175782",
                "https://www.1point3acres.com/interview/post/1176214",
            ],
        )
        self.assertEqual(
            metadata,
            {
                "1175782": ["Anthropic", "2026(4-6月)", "全职", "码农类", "在职跳槽"],
                "1176214": ["Anthropic", "2026(4-6月)", "全职", "应届毕业生"],
            },
        )

    def test_parse_post_records_extracts_center_section_tags(self) -> None:
        html = """
        <div data-sentry-component="ForumThreadItem">
          <a href="https://www.1point3acres.com/home/pins/1175782">Anthropic 面经</a>
          <div class="text-muted-foreground mt-1 flex flex-wrap items-center gap-x-1 text-xs">
            <span class="font-bold text-orange-400">Anthropic</span>
            <span class="bg-muted-foreground size-1 rounded-full"></span>
            <span>2026(4-6月)</span>
            <span class="bg-muted-foreground size-1 rounded-full"></span>
            <span>全职</span>
            <span class="bg-muted-foreground size-1 rounded-full"></span>
            <span>码农类</span>
            <span class="bg-muted-foreground size-1 rounded-full"></span>
            <span>在职跳槽</span>
          </div>
        </div>
        <aside>
          <a href="https://www.1point3acres.com/home/pins/9999999">sidebar</a>
        </aside>
        """

        records = parse_post_records_from_html(html)

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].post_id, "1175782")
        self.assertEqual(
            list(records[0].tags),
            ["Anthropic", "2026(4-6月)", "全职", "码农类", "在职跳槽"],
        )

    def test_collect_company_post_metadata_keeps_first_tags_for_post(self) -> None:
        with TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "anthropic"
            input_dir.mkdir()
            (input_dir / "1.html").write_text(
                """
                <div data-sentry-component="ForumThreadItem">
                  <a href="https://www.1point3acres.com/home/pins/1175782">one</a>
                  <div class="text-muted-foreground text-xs">
                    <span>Anthropic</span>
                    <span class="bg-muted-foreground"></span>
                    <span>2026(4-6月)</span>
                  </div>
                </div>
                """,
                encoding="utf-8",
            )
            (input_dir / "2.html").write_text(
                """
                <div data-sentry-component="ForumThreadItem">
                  <a href="https://www.1point3acres.com/home/pins/1175782">two</a>
                  <div class="text-muted-foreground text-xs">
                    <span>Different</span>
                  </div>
                </div>
                """,
                encoding="utf-8",
            )

            metadata = collect_company_post_metadata(input_dir)

        self.assertEqual(metadata, {"1175782": ["Anthropic", "2026(4-6月)"]})

    def test_build_company_page_url_uses_human_facing_route(self) -> None:
        self.assertEqual(
            build_company_page_url("anthropic", page=3),
            "https://www.1point3acres.com/interview/company/anthropic?page=3",
        )

    def test_limit_input_html_files_supports_default_and_all(self) -> None:
        html_files = [Path("1.html"), Path("2.html"), Path("3.html")]

        self.assertEqual(limit_input_html_files(html_files, max_pages=2), html_files[:2])
        self.assertEqual(limit_input_html_files(html_files, max_pages=-1), html_files)

    def test_load_company_input_files_reuses_existing_html_by_default(self) -> None:
        session = Mock()
        with TemporaryDirectory() as temp_dir, patch("scraper.company.fetch_company_input_pages") as mock_fetch:
            input_dir = Path(temp_dir) / "anthropic"
            input_dir.mkdir()
            html_path = input_dir / "1.html"
            html_path.write_text("<html></html>", encoding="utf-8")

            html_files = load_company_input_files(
                "anthropic",
                input_dir=input_dir,
                session=session,
                refresh_inputs=False,
                max_pages=1,
            )

        self.assertEqual(html_files, [html_path])
        mock_fetch.assert_not_called()

    def test_load_company_input_files_refreshes_when_requested(self) -> None:
        session = Mock()
        with TemporaryDirectory() as temp_dir, patch(
            "scraper.company.fetch_company_input_pages",
            return_value=[Path(temp_dir) / "anthropic" / "1.html"],
        ) as mock_fetch:
            input_dir = Path(temp_dir) / "anthropic"
            input_dir.mkdir()
            (input_dir / "1.html").write_text("<html></html>", encoding="utf-8")

            html_files = load_company_input_files(
                "anthropic",
                input_dir=input_dir,
                session=session,
                refresh_inputs=True,
                max_pages=1,
            )

        self.assertEqual(html_files, [Path(temp_dir) / "anthropic" / "1.html"])
        mock_fetch.assert_called_once()

    def test_download_post_assets_saves_images_and_attachments(self) -> None:
        post = ScrapedPost(
            url="https://www.1point3acres.com/home/pins/1175782",
            title="title",
            author="author",
            published_at="1778089756",
            content="body",
            images=[DownloadableAsset(url="https://example.com/image.png", kind="image")],
            attachments=[DownloadableAsset(url="https://example.com/file.pdf", kind="attachment")],
        )
        session = Mock()
        session.get.side_effect = [
            Mock(content=b"image-bytes", raise_for_status=Mock()),
            Mock(content=b"pdf-bytes", raise_for_status=Mock()),
        ]

        with TemporaryDirectory() as temp_dir:
            image_count, attachment_count = download_post_assets(
                post,
                post_id="1175782",
                session=session,
                image_root=Path(temp_dir) / "images",
                attachment_root=Path(temp_dir) / "attachments",
            )

            self.assertEqual(image_count, 1)
            self.assertEqual(attachment_count, 1)
            self.assertEqual(
                (Path(temp_dir) / "images" / "1175782_image.png").read_bytes(),
                b"image-bytes",
            )
            self.assertEqual(
                (Path(temp_dir) / "attachments" / "1175782_file.pdf").read_bytes(),
                b"pdf-bytes",
            )

    def test_combine_company_posts_writes_single_markdown_file(self) -> None:
        with TemporaryDirectory() as temp_dir:
            raw_posts_dir = Path(temp_dir) / "raw_posts"
            raw_posts_dir.mkdir()
            (raw_posts_dir / "1175782.md").write_text(
                "# First\n\n`Post ID: 1175782` | `Author: A` | `Published: 2026-05-06 10:49:16 PDT`\n",
                encoding="utf-8",
            )
            (raw_posts_dir / "1176000.md").write_text(
                "# Second\n\n`Post ID: 1176000` | `Author: B` | `Published: 2026-05-07 10:49:16 PDT`\n",
                encoding="utf-8",
            )
            output_path = Path(temp_dir) / "outputs" / "anthropic" / "anthropic.md"
            output_path.parent.mkdir(parents=True)

            combine_company_posts(
                "anthropic",
                post_targets=[
                    "https://www.1point3acres.com/home/pins/1175782",
                    "https://www.1point3acres.com/bbs/thread-1176000-1-1.html",
                ],
                raw_posts_dir=raw_posts_dir,
                output_path=output_path,
                post_metadata={"1175782": ["Anthropic", "2026(4-6月)", "全职", "码农类"]},
            )

            self.assertEqual(
                output_path.read_text(encoding="utf-8"),
                "# Anthropic\n\nThis file contains 2 posts created between 2026-05-06 and 2026-05-07.\n\n## Table of Contents\n\n- [First 2026-05-06 [码农类]](#post-1175782)\n- [Second 2026-05-07](#post-1176000)\n<a id=\"post-1175782\"></a>\n\n# First 2026-05-06 [码农类]\n\n`Post ID: 1175782` | `Author: A` | `Published: 2026-05-06 10:49:16 PDT`\n\n---\n\n<a id=\"post-1176000\"></a>\n\n# Second 2026-05-07\n\n`Post ID: 1176000` | `Author: B` | `Published: 2026-05-07 10:49:16 PDT`\n",
            )

    def test_inject_post_tags_into_markdown_updates_first_heading_only(self) -> None:
        markdown = "# First\n\nbody\n\n## Replies\n\ntext"

        updated = inject_post_tags_into_markdown(
            markdown,
            tags=["Anthropic", "2026(4-6月)", "全职", "码农类", "在职跳槽"],
            published_date="2026-05-06",
        )

        self.assertEqual(updated, "# First 2026-05-06 [码农类]\n\nbody\n\n## Replies\n\ntext")

    def test_extract_position_type_tag_uses_fourth_metadata_tag(self) -> None:
        self.assertEqual(
            extract_position_type_tag(["Anthropic", "2026(4-6月)", "全职", "码农类", "在职跳槽"]),
            "码农类",
        )
        self.assertIsNone(extract_position_type_tag(["Anthropic", "2026(4-6月)"]))

    def test_run_company_scrape_reports_stats_and_skips_existing_posts(self) -> None:
        with TemporaryDirectory() as temp_dir:
            inputs_root = Path(temp_dir) / "inputs"
            outputs_root = Path(temp_dir) / "outputs"
            company_dir = inputs_root / "anthropic"
            company_dir.mkdir(parents=True)
            html_path = company_dir / "1.html"
            html_path.write_text(
                """
                <div data-sentry-component="ForumThreadItem">
                  <a href="https://www.1point3acres.com/home/pins/1175782">one</a>
                </div>
                <div data-sentry-component="ForumThreadItem">
                  <a href="https://www.1point3acres.com/home/pins/1176000">two</a>
                </div>
                <div data-sentry-component="ForumThreadItem">
                  <a href="https://www.1point3acres.com/home/pins/1177000">three</a>
                </div>
                """,
                encoding="utf-8",
            )
            raw_posts_dir = outputs_root / "raw_posts"
            raw_posts_dir.mkdir(parents=True)
            (raw_posts_dir / "1175782.md").write_text("# Existing\n", encoding="utf-8")

            def fake_scrape_post(url: str, session) -> ScrapedPost:
                if url.endswith("/1177000"):
                    raise RuntimeError("boom")
                return ScrapedPost(
                    url=url,
                    title="Fresh",
                    author="author",
                    published_at="1778089756",
                    content="body",
                )

            with patch("scraper.company.build_authenticated_session", return_value=Mock()), patch(
                "scraper.company.load_company_input_files",
                return_value=[html_path],
            ), patch(
                "scraper.company.scrape_post",
                side_effect=fake_scrape_post,
            ), patch("scraper.company.download_post_assets", return_value=(0, 0)):
                stats = run_company_scrape(
                    "anthropic",
                    inputs_root=inputs_root,
                    outputs_root=outputs_root,
                )

            self.assertEqual(stats["identified"], 3)
            self.assertEqual(stats["already_exists"], 1)
            self.assertEqual(stats["newly_scraped"], 1)
            self.assertEqual(stats["failed"], 1)
            self.assertTrue((raw_posts_dir / "1176000.md").exists())
            self.assertFalse((raw_posts_dir / "1177000.md").exists())
            combined_path = outputs_root / "anthropic" / "anthropic.md"
            self.assertTrue(combined_path.exists())
            combined_text = combined_path.read_text(encoding="utf-8")
            self.assertIn("# Existing", combined_text)
            self.assertIn("# Fresh", combined_text)

    def test_run_company_scrape_limits_processed_pages_before_skip_logic(self) -> None:
        with TemporaryDirectory() as temp_dir:
            inputs_root = Path(temp_dir) / "inputs"
            outputs_root = Path(temp_dir) / "outputs"
            company_dir = inputs_root / "anthropic"
            company_dir.mkdir(parents=True)
            html_path = company_dir / "1.html"
            html_path.write_text(
                """
                <div data-sentry-component="ForumThreadItem"><a href="https://www.1point3acres.com/home/pins/1175782">one</a></div>
                <div data-sentry-component="ForumThreadItem"><a href="https://www.1point3acres.com/home/pins/1176000">two</a></div>
                """,
                encoding="utf-8",
            )
            html_path_2 = company_dir / "2.html"
            html_path_2.write_text(
                """
                <div data-sentry-component="ForumThreadItem"><a href="https://www.1point3acres.com/home/pins/1177000">three</a></div>
                """,
                encoding="utf-8",
            )
            raw_posts_dir = outputs_root / "raw_posts"
            raw_posts_dir.mkdir(parents=True)
            (raw_posts_dir / "1175782.md").write_text("# Existing\n", encoding="utf-8")

            with patch("scraper.company.build_authenticated_session", return_value=Mock()), patch(
                "scraper.company.load_company_input_files",
                return_value=[html_path],
            ), patch(
                "scraper.company.scrape_post",
                return_value=ScrapedPost(
                    url="https://www.1point3acres.com/home/pins/1176000",
                    title="Fresh",
                    author="author",
                    published_at="1778089756",
                    content="body",
                ),
            ), patch("scraper.company.download_post_assets", return_value=(0, 0)):
                stats = run_company_scrape(
                    "anthropic",
                    inputs_root=inputs_root,
                    outputs_root=outputs_root,
                    max_pages=1,
                )

            self.assertEqual(stats["identified_total"], 2)
            self.assertEqual(stats["identified"], 2)
            self.assertEqual(stats["already_exists"], 1)
            self.assertEqual(stats["newly_scraped"], 1)
            self.assertFalse((raw_posts_dir / "1177000.md").exists())

    def test_fetch_company_input_pages_saves_numbered_html_files(self) -> None:
        session = Mock()
        with TemporaryDirectory() as temp_dir, patch(
            "scraper.company.fetch_company_page_html",
            return_value="""
            <html><body>
              <div data-sentry-component="ForumThreadItem">
                <a href="https://www.1point3acres.com/home/pins/1175782">one</a>
              </div>
            </body></html>
            """,
        ):
            paths = fetch_company_input_pages(
                "anthropic",
                input_dir=Path(temp_dir) / "anthropic",
                session=session,
                max_pages=1,
            )

            self.assertEqual(paths, [Path(temp_dir) / "anthropic" / "1.html"])
            self.assertTrue(paths[0].exists())
            self.assertIn("1175782", paths[0].read_text(encoding="utf-8"))

    def test_fetch_company_input_pages_stops_after_requested_page_count(self) -> None:
        session = Mock()
        with TemporaryDirectory() as temp_dir, patch(
            "scraper.company.fetch_company_page_html",
            side_effect=[
                """
                <html><body>
                  <div data-sentry-component="ForumThreadItem"><a href="https://www.1point3acres.com/home/pins/1175782">one</a></div>
                </body></html>
                """,
                """
                <html><body>
                  <div data-sentry-component="ForumThreadItem"><a href="https://www.1point3acres.com/home/pins/1176000">two</a></div>
                </body></html>
                """,
            ],
        ) as mock_fetch:
            paths = fetch_company_input_pages(
                "anthropic",
                input_dir=Path(temp_dir) / "anthropic",
                session=session,
                max_pages=1,
            )

        self.assertEqual(len(paths), 1)
        mock_fetch.assert_called_once()

    def test_fetch_company_page_html_uses_human_company_url(self) -> None:
        session = Mock()
        response = Mock(text="<html></html>")
        session.get.return_value = response

        html = fetch_company_page_html("anthropic", page=2, session=session)

        self.assertEqual(html, "<html></html>")
        session.get.assert_called_once_with(
            "https://www.1point3acres.com/interview/company/anthropic?page=2",
            params=None,
            timeout=30.0,
        )

    def test_build_asset_filename_and_sanitize_filename(self) -> None:
        self.assertEqual(
            build_asset_filename("https://example.com/path/file name.pdf", post_id="1175782", index=1),
            "1175782_file_name.pdf",
        )
        self.assertEqual(sanitize_filename(" weird*&name .png "), "weird_name_.png")

    def test_run_company_scrape_stops_after_first_429_error(self) -> None:
        with TemporaryDirectory() as temp_dir:
            inputs_root = Path(temp_dir) / "inputs"
            outputs_root = Path(temp_dir) / "outputs"
            company_dir = inputs_root / "anthropic"
            company_dir.mkdir(parents=True)
            company_dir.joinpath("1.html").write_text(
                """
                <div data-sentry-component="ForumThreadItem"><a href="https://www.1point3acres.com/home/pins/1176001">one</a></div>
                <div data-sentry-component="ForumThreadItem"><a href="https://www.1point3acres.com/home/pins/1176002">two</a></div>
                <div data-sentry-component="ForumThreadItem"><a href="https://www.1point3acres.com/home/pins/1176003">three</a></div>
                <div data-sentry-component="ForumThreadItem"><a href="https://www.1point3acres.com/home/pins/1176004">four</a></div>
                <div data-sentry-component="ForumThreadItem"><a href="https://www.1point3acres.com/home/pins/1176005">five</a></div>
                <div data-sentry-component="ForumThreadItem"><a href="https://www.1point3acres.com/home/pins/1176006">six</a></div>
                """,
                encoding="utf-8",
            )

            def raise_429(url: str, session) -> ScrapedPost:
                response = requests.Response()
                response.status_code = 429
                raise requests.HTTPError("rate limited", response=response)

            with patch("scraper.company.build_authenticated_session", return_value=Mock()), patch(
                "scraper.company.load_company_input_files",
                return_value=[company_dir / "1.html"],
            ), patch(
                "scraper.company.scrape_post",
                side_effect=raise_429,
            ), patch("scraper.company.download_post_assets", return_value=(0, 0)):
                stats = run_company_scrape(
                    "anthropic",
                    inputs_root=inputs_root,
                    outputs_root=outputs_root,
                )

            self.assertEqual(stats["identified"], 6)
            self.assertEqual(stats["newly_scraped"], 0)
            self.assertEqual(stats["failed"], 1)
            self.assertFalse((outputs_root / "raw_posts" / "1176002.md").exists())
            self.assertTrue((outputs_root / "anthropic" / "anthropic.md").exists())

    def test_run_company_scrape_rejects_invalid_max_pages(self) -> None:
        with self.assertRaises(ValueError):
            run_company_scrape(
                "anthropic",
                inputs_root=Path("inputs"),
                outputs_root=Path("outputs"),
                max_pages=0,
            )

    def test_is_http_403_or_429_error_detects_http_error(self) -> None:
        response = requests.Response()
        response.status_code = 429
        exc = requests.HTTPError("rate limited", response=response)

        self.assertTrue(is_http_403_or_429_error(exc))

        response_403 = requests.Response()
        response_403.status_code = 403
        exc_403 = requests.HTTPError("forbidden", response=response_403)

        self.assertTrue(is_http_403_or_429_error(exc_403))

    def test_build_table_of_contents_handles_duplicate_headings(self) -> None:
        markdown = """# anthropic

<a id="post-1"></a>
# Same
`Post ID: 1` | `Author: A` | `Published: 2026-05-06 10:49:16 PDT`

<a id="post-2"></a>
# Same
`Post ID: 2` | `Author: B` | `Published: 2026-05-07 10:49:16 PDT`
"""

        self.assertEqual(
            build_table_of_contents(markdown),
            "## Table of Contents\n\n- [Same 2026-05-06](#post-1)\n- [Same 2026-05-07](#post-2)\n\n",
        )

    def test_extract_published_date_and_build_summary(self) -> None:
        markdown = "`Post ID: 1175782` | `Author: A` | `Published: 2026-05-06 10:49:16 PDT`\n"

        self.assertEqual(extract_published_date(markdown), "2026-05-06")
        self.assertEqual(
            build_summary(2, ["2026-05-07", "2026-05-06"]),
            "This file contains 2 posts created between 2026-05-06 and 2026-05-07.",
        )


if __name__ == "__main__":
    unittest.main()
