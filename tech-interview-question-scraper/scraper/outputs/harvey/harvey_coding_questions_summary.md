# Harvey Coding Questions Summary

Source: `outputs/harvey/harvey.md`

## 1. Source Highlighting / Citation Tagging

Most common phone-screen question.

Input: a model response or sentence plus `sources` / matching phrases.

Tasks:
- Count how many times each source appears.
- Wrap matched spans with `<yellow>...</yellow>` or `<tag>...</tag>`.
- Merge overlapping matches.
- Add citations after highlighted spans, such as `<yellow>...</yellow>[1][3]`.
- Order citations by source occurrence count in some variants.

Important edge cases:
- Word-level matching, not substring matching. `blue` should not match `blueprint`; `row` should not match `brown`.
- Overlapping phrases should become one highlighted span.
- Repeated sources and repeated matches need clear counting.
- Track which source IDs contributed to each merged interval.

Likely approach:
- Tokenize by words.
- Find all matching source phrase ranges.
- Merge intervals.
- Carry source IDs/frequencies through the merge.
- Render the final string from left to right.

## 2. Spreadsheet / Cell Formula Engine

Repeated 2026 phone-screen question.

Build:
- `set_cell(label, value)`
- `get_cell(label)`

Parts:
- Values start as integers.
- Later values can be formulas like `A1+20`, `A1+A2+5`, or `=B1+5`.
- Only `+` is required.
- `get_cell` may need to be `O(1)`, so update propagation should happen in `set_cell`.
- Detect circular dependencies, for example `A1 = B1 + 1`, `B1 = A1 + 1`.

Likely approach:
- Store raw values/formulas.
- Store computed cell values.
- Maintain dependencies and reverse dependencies.
- On `set_cell`, validate cycle, recompute affected downstream cells, and keep `get_cell` as a dictionary lookup.

## 3. Filesystem / Folder-File Trie

Seen in phone screen and onsite.

Build:
- `addFile(path)` stores a file at paths like `path/to/file.txt`.
- `getFile(path)` returns a file or folder by path.

Follow-ups:
- Each folder can contain at most 5 items.
- Duplicate filename handling like an OS:
  - `file.txt`
  - `file(1).txt`
  - `file(2).txt`
- Tricky case: adding `file.txt`, `file.txt`, `file(1).txt` should produce `file.txt`, `file(1).txt`, `file(1)(1).txt`.
- Production discussion may ask about storage model, DB representation, and detecting identical file content.

Likely approach:
- Use nested dictionaries / trie nodes.
- Track child count per folder.
- Parse file extension carefully when generating duplicate names.

## 4. Expression Map / Symbol Evaluation

Onsite coding variant.

Problem:
- Given an expression map, compute the final value for every symbol.
- Follow-up: if dependencies contain a cycle, raise an exception.

Likely approach:
- DFS with memoization.
- Use three-color marking for cycle detection.

## 5. RAG / ML Coding Notebook

Appears in AI / ML-oriented rounds.

Tasks reported:
- Fill in parts of a simple RAG notebook.
- Generate text embeddings from pandas DataFrames using provided utilities.
- Compute query embedding.
- Use cosine similarity to retrieve top 10.
- Implement evaluation logic / metrics.

Prep focus:
- Pandas manipulation.
- Vectorized cosine similarity.
- Retrieval metrics such as recall@k / precision@k / MRR, depending on prompt.

## 6. DB Connection Pool

Onsite coding.

Problem:
- Given a mocked `db.query`, implement `acquire` and `release` for a connection pool.
- Reported follow-up: thread-safe version with locks.

Prep focus:
- Queue / semaphore style implementation.
- Lock discipline.
- Handling wait, release, and pool exhaustion clearly.

## 7. Web Crawler

One onsite report mentions a multithreaded web crawler.

No detailed spec was included in the scrape.

Prep focus:
- BFS/queue crawl frontier.
- Visited set.
- Worker threads.
- URL filtering / domain constraints.
- Locking around shared state.

## 8. Cursor / String Editing

One onsite report describes a mouse/cursor string-editing problem with emphasis on time complexity.

No detailed spec was included in the scrape.

Prep focus:
- Text editor buffer operations.
- Cursor movement.
- Efficient insertion/deletion.
- Consider linked list, gap buffer, or two-stack representation depending on operations.

## Prep Priority

1. Source highlighting + citations.
2. Spreadsheet formula engine with `O(1)` reads and cycle detection.
3. Filesystem trie with duplicate rename rules.
4. DFS dependency evaluation with cycle detection.
5. RAG notebook if interviewing for ML / AI application roles.
6. DB connection pool and multithreaded crawler for onsite systems-flavored coding.
