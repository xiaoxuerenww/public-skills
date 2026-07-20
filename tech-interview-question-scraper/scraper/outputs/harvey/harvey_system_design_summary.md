# Harvey System Design Summary

Source: `outputs/harvey/harvey.md`

## High-Level Pattern

The dominant Harvey system design prompt is a Google Drive / Vault / data-room style product. The wording varies, but the expected design is usually a file storage and sharing system tailored to legal documents.

Other reported prompts:
- RAG system.
- AI code-generation agent.
- "Mint" / external-call scheduling system.

## 1. Google Drive / Vault / Data Room

Most common onsite system design question.

Reported variants:
- Design Google Drive.
- Design Harvey Vault.
- Design a legal data room.
- Data room defaults to PDFs only.
- Focus on organization-level ACL.
- Sometimes focus on scaling instead of ACL.

Core requirements to cover:
- Upload files.
- Download files.
- Organize folders/files.
- Share files or folders.
- Permission management / ACL.
- Security.
- Large file handling.

Important clarifications:
- Ask whether this is full Google Drive or Harvey-style legal document vault.
- Ask whether files are immutable PDFs or editable documents.
- Ask whether multi-device sync is required. Several reports say it was not required.
- Ask whether version conflicts need to be handled. If files are PDFs / immutable, this may be out of scope.
- Ask whether sharing is user-level, organization-level, group/team-level, or link-based.
- Ask expected scale. One report mentions about 100K total users and sharing files with thousands of users in an organization.

Suggested architecture:
- Metadata service for file/folder records.
- Blob/object storage for file bytes, e.g. S3.
- Metadata DB for file tree, owner, org, folder hierarchy, timestamps, versions, and object keys.
- ACL / permission service.
- Upload service using pre-signed URLs or a controlled upload API.
- Download service with authorization check before issuing pre-signed download URL.
- Search/indexing service if document search is in scope.
- Audit log service for legal/compliance events.

Large file follow-ups:
- Split large files into chunks.
- Store chunk metadata linked by `file_id`.
- Track checksum/hash per chunk.
- Verify each uploaded chunk is the expected content.
- Compose chunks after all are uploaded.
- Support retries and resumable upload.

ACL / permission focus:
- Model orgs, users, groups, files, folders.
- Decide whether folder permissions inherit to child files.
- Support explicit allow/deny or keep it simpler with inherited ACL plus overrides.
- Sharing to thousands of users should use org/group ACL entries instead of one row per user.
- Check permissions before upload/download/share/list.
- Include audit events for access, share, revoke, upload, and download.

Security focus:
- AuthN/AuthZ boundary.
- Object storage should not be directly public.
- Pre-signed URLs should be short-lived.
- Encrypt at rest and in transit.
- Malware scanning / document validation if relevant.
- Audit trail matters because the product is legal/compliance-oriented.

What interviewers seem to like:
- Clearly separate metadata store and blob store.
- Mention large-file chunking.
- Explain ACL at organization and group levels.
- Keep the design product-specific rather than generic sync-heavy Google Drive.

## 2. RAG System

Reported as a system design round for ML / AI-oriented loops.

Likely requirements:
- Ingest legal or enterprise documents.
- Chunk documents.
- Embed chunks.
- Store vectors and metadata.
- Retrieve top-k chunks for a query.
- Generate answer with citations.
- Evaluate retrieval / answer quality.

Suggested architecture:
- Document ingestion pipeline.
- Parser / OCR if PDFs are in scope.
- Chunker.
- Embedding workers.
- Vector DB plus metadata DB.
- Query service.
- Retriever / reranker.
- LLM answer generation service.
- Citation renderer.
- Evaluation / feedback pipeline.

Key tradeoffs:
- Chunk size and overlap.
- Vector search vs hybrid lexical + vector retrieval.
- Metadata filters for org/user permissions.
- Reranking cost vs quality.
- Latency budget for retrieval and generation.
- Freshness of newly uploaded documents.
- Grounding / hallucination mitigation.

Evaluation metrics to prepare:
- Recall@k.
- Precision@k.
- MRR / nDCG.
- Citation correctness.
- Answer faithfulness.
- Latency and cost.

## 3. AI Code-Generation Agent

Reported in an AI application loop.

Prompt:
- Design an AI code-generation agent.

Notes from report:
- Interviewer may not have a standardized rubric.
- Prep call suggested they wanted something beyond a basic RAG answer.
- Overly complex design got negative feedback, so keep the architecture focused and incremental.

Suggested architecture:
- User task intake.
- Repo/context indexing.
- Planning component.
- Code edit generator.
- Test runner / sandbox.
- Iterative repair loop.
- Diff review / explanation.
- Safety and permission boundaries.

Key design points:
- Context selection from repo files, symbols, tests, docs, and recent diffs.
- Tool use: search, read files, edit files, run tests.
- Guardrails around destructive edits and secret exposure.
- Evaluation by test pass rate, compile success, lint, human acceptance, and rollback rate.
- Avoid designing an overly broad autonomous agent unless the interviewer explicitly asks for it.

## 4. Mint / External-Call Scheduling System

Less common, but one report mentions it as an SD round.

Prompt:
- Design "mint".
- Main focus: scheduling external calls.
- External calls can only be pulled, not pushed.

Reported follow-ups:
- How to schedule external calls.
- How to handle call failures.
- How to partition queues at large scale.

Suggested architecture:
- Job creation API.
- Durable job store.
- Scheduler / dispatcher.
- Pull-based worker model.
- Retry policy with exponential backoff.
- Dead-letter queue.
- Idempotency keys.
- Queue partitioning by tenant, job type, priority, or hash.
- Monitoring and alerting.

Key tradeoffs:
- At-least-once vs exactly-once semantics.
- Retry storms and backpressure.
- Fairness across tenants.
- Failure isolation by partition.
- Ordering requirements, if any.

## Prep Priority

1. Google Drive / Vault / data room with ACL, large-file upload, metadata/blob split, and security.
2. RAG system with ingestion, retrieval, citations, and evaluation.
3. AI code-generation agent if interviewing for AI application / agent teams.
4. External-call scheduler / queue partitioning as a backup design prompt.

## Short Answer Template For Google Drive / Vault

Start with:
"I want to clarify whether this is full Google Drive with editing/sync, or Harvey-style Vault/data room for mostly immutable PDFs. If it is the latter, I would focus on upload/download, folders, sharing, ACL, large-file handling, auditability, and secure object storage."

Then structure:
1. Requirements and scale.
2. APIs.
3. Data model: users, orgs, groups, files, folders, ACLs, chunks.
4. High-level architecture: metadata service, object storage, ACL service, upload/download service, audit log.
5. Deep dive: ACL inheritance or large-file chunking.
6. Reliability/security: retries, checksums, encryption, audit logs, short-lived URLs.
