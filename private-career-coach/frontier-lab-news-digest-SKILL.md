---
name: frontier-lab-news-digest
description: |
  Generate daily HTML digest of tech and financial news from frontier AI labs, optimized for mobile email. Compiles curated updates about Anthropic, OpenAI, xAI, Google DeepMind, Meta, and other leading AI organizations from the last 24 hours. Covers product launches, model releases, funding announcements, regulatory news, hiring updates, market movements, and cross-lab patterns. Output is responsive HTML formatted for email clients and mobile phones. Send via scheduled routine daily at 7am PST to heheni723@gmail.com.
compatibility: Requires web search capability and email delivery integration
---

## Overview

This skill searches for frontier AI lab news from the **last 24 hours only** and compiles them into a **responsive HTML digest** optimized for mobile email rendering. Output is email-ready and designed for readability on phones, tablets, and desktop clients (Gmail, Outlook, Apple Mail, etc.).

**Flexible Company Tracking:** The skill supports both default frontier labs and custom company subscriptions. You can add or remove companies at any time to customize your digest.

## What to Search For

Search across these sources and categories for updates from the last 24 hours:

### Default Labs to Monitor
- **Anthropic** (Claude releases, funding, regulatory engagement, compute partnerships)
- **OpenAI** (GPT releases, products, partnerships, IPO activity, deployment strategy)
- **xAI** (Grok models, funding, compute business, SpaceX integration)
- **Google DeepMind** (Gemini/Genie releases, research, agents, acquisitions)
- **Meta** (Llama/Muse releases, products, capex plans, consolidation moves)

### Custom Subscriptions (Configurable)
Add any AI company or lab you want to track. Examples:
- **Reflection AI** (reasoning models, inference optimization)
- **Mistral** (open models, enterprise offerings)
- **Modal** (AI infrastructure, model serving)
- **Decart** (AI infrastructure, system design)
- **Microsoft Research** (foundation models, research)
- **Tesla AI** (autonomous systems, embodied AI)
- **Hugging Face** (open source, model hub)
- **Stability AI** (generative models, diffusion)
- **Robustness Institute** (AI safety research)
- **Any other company** you want to monitor

**How to add/update subscriptions:**
When scheduling the daily digest, specify the `custom_companies` parameter with a comma-separated list. Example: `Reflection AI, Mistral, Tesla AI`. The skill will automatically include these alongside the default labs.

### News Categories
- **Product launches & model releases** — New models, APIs, agents, capabilities
- **Research & technical breakthroughs** — Multi-agent systems, efficiency innovations, algorithmic improvements
- **Funding & M&A** — Funding rounds, valuations, acquisitions, talent consolidation
- **Compute & infrastructure** — Data center deals, GPU availability, capex commitments, revenue streams
- **Policy & regulation** — AI safety regulations, labor impact debates, government initiatives
- **Market & financial** — IPO filings, stock movements, private valuations
- **Partnerships & integrations** — Enterprise deals, strategic partnerships
- **Robotics & embodied AI** — Physical AI breakthroughs, autonomous systems

## Time Scope

**Only include news from the last 24 hours.** Do not include news older than 24 hours, even if it's significant. If a particular lab has no updates in the last 24 hours, use "No significant updates in the last 24 hours" placeholder.

## Customization Parameters

When invoking this skill (manually or via schedule), you can specify:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `custom_companies` | string (comma-separated) | none | Additional companies to track beyond default labs. Example: "Reflection AI, Mistral, Modal Labs" |
| `include_default_labs` | boolean | true | Whether to include Anthropic, OpenAI, xAI, DeepMind, Meta in the digest |
| `include_other_labs` | boolean | true | Whether to include "Other Notable Labs" section with ecosystem updates |
| `max_items_per_company` | integer | 3 | Maximum news items per company section (prevents digest from getting too long) |
| `time_period_hours` | integer | 24 | Hours back to search (default 24 for daily digest) |

**Example scheduled call:**
```
Frontier Lab News Digest - custom_companies: "Reflection AI, Mistral, Tesla AI"; include_default_labs: true
```

## Output Format: Responsive HTML Email

Generate a complete HTML email digest with this structure and styling. The HTML must be:
- **Mobile-responsive** (readable on phones without scrolling left/right)
- **Email-client compatible** (inline CSS, no external stylesheets, works in Gmail, Outlook, Apple Mail)
- **Dark mode friendly** (uses system colors where possible)
- **Fast-loading** (optimized images, minimal external resources)

### HTML Template Structure

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Frontier Lab Updates — [Date]</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: #1f2937;
            background-color: #f9fafb;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            border: 1px solid #e5e7eb;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 24px;
            text-align: center;
        }
        .header h1 {
            margin: 0;
            font-size: 24px;
            font-weight: 700;
        }
        .header p {
            margin: 8px 0 0 0;
            font-size: 14px;
            opacity: 0.9;
        }
        .content {
            padding: 24px;
        }
        .lab-section {
            margin-bottom: 32px;
        }
        .lab-title {
            font-size: 18px;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 16px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .lab-emoji {
            font-size: 20px;
        }
        .news-item {
            margin-bottom: 16px;
            padding: 12px;
            background-color: #f9fafb;
            border-left: 4px solid #667eea;
            border-radius: 4px;
        }
        .news-title {
            font-weight: 700;
            color: #1f2937;
            margin: 0 0 8px 0;
            font-size: 15px;
        }
        .news-summary {
            color: #4b5563;
            font-size: 14px;
            margin: 0 0 8px 0;
            line-height: 1.5;
        }
        .news-source {
            font-size: 13px;
            color: #667eea;
        }
        .news-source a {
            color: #667eea;
            text-decoration: none;
        }
        .news-source a:hover {
            text-decoration: underline;
        }
        .trends-section {
            background-color: #f0f4ff;
            padding: 20px;
            border-radius: 8px;
            margin-top: 32px;
        }
        .trends-title {
            font-size: 18px;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 12px;
        }
        .trend {
            margin-bottom: 12px;
            font-size: 14px;
            color: #374151;
            line-height: 1.6;
        }
        .trend strong {
            color: #667eea;
        }
        .footer {
            background-color: #f3f4f6;
            padding: 16px 24px;
            text-align: center;
            border-top: 1px solid #e5e7eb;
            font-size: 12px;
            color: #6b7280;
        }
        .no-updates {
            color: #9ca3af;
            font-style: italic;
            padding: 12px;
        }
        @media (max-width: 600px) {
            .container {
                border: none;
            }
            .header {
                padding: 16px;
            }
            .header h1 {
                font-size: 20px;
            }
            .content {
                padding: 16px;
            }
            .lab-section {
                margin-bottom: 24px;
            }
            .news-item {
                padding: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Frontier Lab Updates</h1>
            <p>[Date] — Last 24 hours</p>
        </div>

        <div class="content">
            <!-- DEFAULT LABS SECTIONS: Anthropic, OpenAI, xAI, DeepMind, Meta -->
            <!-- (Include only if include_default_labs=true) -->

            <div class="lab-section">
                <div class="lab-title">
                    <span class="lab-emoji">🔬</span>
                    <span>Anthropic</span>
                </div>

                <!-- NEWS ITEMS REPEAT: Each update is a news item -->
                <div class="news-item">
                    <h3 class="news-title">Update Headline Here</h3>
                    <p class="news-summary">2-3 sentence summary with key details and implications.</p>
                    <div class="news-source">
                        📌 Source: <a href="[URL]">Source Name</a>
                    </div>
                </div>

                <!-- If no updates in last 24h -->
                <div class="no-updates">
                    No significant updates in the last 24 hours
                </div>
            </div>

            <!-- Repeat for: OpenAI (🤖), xAI (⚡), Google DeepMind (🧠), Meta (👍), Other Labs (🌟) -->

            <!-- CUSTOM SUBSCRIPTIONS SECTIONS: Dynamic based on custom_companies parameter -->
            <!-- Example: If custom_companies="Reflection AI, Mistral" then add sections below -->

            <div class="lab-section">
                <div class="lab-title">
                    <span class="lab-emoji">🎯</span>
                    <span>Reflection AI</span>
                </div>

                <!-- NEWS ITEMS: Follow same format as default labs -->
                <div class="news-item">
                    <h3 class="news-title">[News headline]</h3>
                    <p class="news-summary">[2-3 sentence summary with key details]</p>
                    <div class="news-insight">
                        <span class="insight-icon">💡</span>
                        <span><strong>Key insight:</strong> [1-sentence strategic implication]</span>
                    </div>
                    <div class="news-source">
                        📌 Source: <a href="[URL]">[Source Name]</a>
                    </div>
                </div>

                <!-- Or if no updates in last 24h -->
                <div class="no-updates">
                    No significant updates in the last 24 hours
                </div>
            </div>

            <!-- Repeat for each custom_company in the subscriptions list -->

            <!-- TRENDS SECTION -->
            <div class="trends-section">
                <div class="trends-title">📊 Trends & Strategic Patterns</div>
                <div class="trend">
                    <strong>Pattern Name:</strong> 2-3 sentence summary of emerging pattern across labs.
                </div>
                <!-- Repeat for 3-4 key trends -->
            </div>
        </div>

        <div class="footer">
            <p><strong>Last updated:</strong> [Date & Time, PST]</p>
            <p><strong>Sources:</strong> TechCrunch, Bloomberg, Axios, CNBC, Crunchbase, DeepMind Blog, and others</p>
            <p>Frontier Lab News Crawler • Delivered daily at 7:00 AM PST</p>
        </div>
    </div>
</body>
</html>
```

## Key HTML Design Features

**Mobile Optimization:**
- Responsive width (max 600px for desktop, 100% on mobile)
- Large touch-friendly link targets (minimum 44px height)
- Clear hierarchy with proper spacing
- Proper meta viewport tag for mobile rendering

**Email Compatibility:**
- Inline CSS (not external stylesheets)
- No JavaScript or external resources
- Standard HTML5 doctype
- Tested rendering in Gmail, Outlook, Apple Mail

**Visual Design:**
- Color scheme with accessible contrast ratios
- Clear section hierarchy with lab emojis
- Visual distinction between news items (background color, left border)
- Trends section highlighted with subtle background color
- Footer with timestamp and source attribution

## News Item Format

Each news item in HTML should follow this structure:

```html
<div class="news-item">
    <h3 class="news-title">**[Headline]**</h3>
    <p class="news-summary">[2-3 sentence summary with key details and implications].</p>
    <div class="news-source">
        📌 Source: <a href="[URL]">[Source Name]</a>
    </div>
</div>
```

## Time Filtering

Before including any news item, verify:
1. **Last 24 hours only** — No news older than 24 hours before generation time
2. **Recent = current day or previous calendar day** — If generating at May 27 2pm, include May 27 and May 26 news only
3. **Check source dates** — Verify publication date, not just when you found it

## Quality Checks

Before finalizing:

1. **Is it accurate?** — Summaries match source articles. Use exact figures (valuations, amounts).
2. **Is it timely?** — All items from last 24 hours only.
3. **Are links valid?** — Every source link is working URL to original source.
4. **Is it mobile-friendly?** — Text readable at phone width without horizontal scroll. Line length reasonable.
5. **Is it scannable?** — User can glance and extract key info in <3 minutes.
6. **Is it strategic?** — Summaries explain *why* news matters, not just *what* happened.
7. **HTML renders correctly** — No broken styling, emojis display properly, links clickable.

## Email Delivery Specification

- **Subject line:** "Frontier Lab Updates — [Date]" (e.g., "Frontier Lab Updates — May 27, 2026")
  - If custom subscriptions included, optionally append: "Frontier Lab Updates (+ Custom) — May 27, 2026"
- **Send time:** 7:00 AM PST daily
- **Recipient:** heheni723@gmail.com
- **Format:** HTML (multipart email with plain text fallback optional)
- **Headers:** Include timezone info in send time

## Managing Your Subscriptions

**Current subscriptions:** Anthropic, OpenAI, xAI, Google DeepMind, Meta + Other Notable Labs

**To add a company:** When running the skill or scheduling, pass the company name in `custom_companies` parameter.

**To remove a company:** Omit it from the `custom_companies` parameter.

**To modify only custom companies** (skip default labs): Set `include_default_labs: false` and provide your custom list.

**Examples:**
```
# Include defaults + Reflection AI, Mistral, Tesla AI
custom_companies: "Reflection AI, Mistral, Tesla AI"

# Only track Reflection AI and Mistral
include_default_labs: false
custom_companies: "Reflection AI, Mistral"

# Only defaults (no custom)
custom_companies: ""
# or just don't include the parameter
```
