---
name: doc-grounded-qa
description: Read a document, answer questions grounded in that document, and maintain section-organized notes from the user's questions and insights. Use when the user asks to read, analyze, summarize, review, annotate, take notes on, or answer questions from a PDF, DOCX, Markdown, text file, pasted document, paper, report, resume, job description, company note, or search-result packet, especially when answers must distinguish what is in the document from what requires fallback search.
---

# Doc-Grounded Q&A

## Goal

Answer the user's questions from the provided document first. Do not guess.
Separate document-supported answers from fallback search results.

Use this skill for:

- Reading a document and answering questions about it.
- Grounding interview prep questions in a company doc, job description, paper,
  resume, recruiter note, or local research artifact.
- Checking whether a claim is present in the document.
- Using search only when the document does not contain the answer.
- Taking running notes that summarize the user's questions, insights, and
  corrected understanding under the corresponding document section.

## Source Priority

Use sources in this order:

1. **Primary document**: the file, pasted text, URL, or attached document the
   user asked about.
2. **Provided search results**: snippets, result pages, local corpus outputs, or
   search-result files the user supplied.
3. **Fresh search**: web search or local search, only when the answer is not in
   the document and the user did not forbid search.

If using source 2 or 3, label the answer as outside the document.

## First Move

Identify the document and the question. If either is missing, ask one concise
clarifying question.

If the document is a local file:

- Read the file directly when it is Markdown, text, JSON, CSV, or code.
- For PDF, DOCX, slides, or spreadsheets, use the appropriate document tooling
  or extraction method available in the environment.
- For large files, search within the extracted text first, then read surrounding
  context.

If the document is pasted in chat, treat the pasted text as the source of truth.
If the document is a URL or current web page, browse or fetch it before
answering.

## Grounding Workflow

1. Extract or read the document text.
2. Search the document for terms from the question and likely synonyms.
3. Read enough surrounding context to avoid quote-mining.
4. Answer only what the document supports.
5. Include a short citation handle:
   - Local Markdown/text: file path and line when available.
   - PDF/DOCX/slides: page, section, heading, or quoted phrase.
   - Pasted text: section heading or short quoted phrase.
   - URL: link and page title.
6. If the document does not answer the question, say so plainly before using
   fallback search.
7. If the user asks questions, shares insights, or corrects their understanding,
   update notes according to the Note-Taking section.

## Fallback Search

Use fallback search only after checking the document.

When falling back:

1. State: "I do not see this in the document."
2. Search the supplied search results first if they exist.
3. If no supplied results answer it and search is allowed, run a fresh search.
4. Prefer primary or authoritative sources over blogs and summaries.
5. Cite fallback sources separately from document citations.
6. Do not merge fallback facts into the document's claims. Use wording like
   "The document does not say this; external sources indicate..."

For time-sensitive facts, verify with fresh search before answering.

## Answer Format

For simple questions:

```text
Answer: <direct answer>
Grounding: <document citation or "Not found in the document">
Fallback: <only if used>
```

For multi-part questions:

```text
1. <question or subtopic>
   Answer: <document-grounded answer>
   Grounding: <citation>

2. <question or subtopic>
   Answer: <answer>
   Grounding: Not found in the document
   Fallback: <source and concise result>
```

Keep answers concise unless the user asks for a detailed brief.

## Note-Taking

By default, take notes when the session involves reading or learning from a
document and the user asks questions, makes observations, or surfaces an
insight. Do not take notes for meta commands about editing this skill or agent
workflow unless the user explicitly asks to save that meta instruction.

Choose the note target:

- If the source is a local Markdown document and it is appropriate to edit,
  append notes under the corresponding section in that document.
- If the source is PDF, DOCX, URL, pasted text, or should not be modified,
  create or append a sibling Markdown note named `<document-stem>_notes.md`.
- If the user provides an existing notes file, use that file.
- If no file target is clear, ask once before creating a new note file.

Place notes under the most relevant existing heading. Match by the section that
supports the answer, not just by keyword overlap. If no existing heading fits,
create a concise heading near the closest parent section, such as
`## Notes: <topic>`.

Use this compact format:

```markdown
### Q&A Notes

- **Question**: <cleaned version of the user's question>
  - **Document-grounded answer**: <1-3 bullets grounded in the document>
  - **Insight / corrected mental model**: <what the user should remember>
  - **Evidence**: <section, page, line, or short source handle>
  - **External context**: <only if fallback search was used>
```

If a `### Q&A Notes` block already exists in the corresponding section, append
to it instead of creating a duplicate block. Keep notes concise and reviewable;
do not paste full chat transcripts.

## Evidence Standards

- Use direct quotes sparingly and only for exact wording that matters.
- Prefer paraphrase plus citation over long copied passages.
- If the document is ambiguous, say what it says, what it does not say, and the
  most likely interpretation.
- If a question asks for judgment or recommendation, separate evidence from
  inference.
- If sources conflict, show the conflict instead of forcing agreement.

## Interview Prep Use

When the document is for interview prep, convert the grounded answer into usable
prep material:

- Likely interviewer question.
- Evidence from the document.
- Strong candidate answer grounded in that evidence.
- What is missing and needs external research.

Do not invent company facts, role requirements, metrics, or personal stories
that are not present in the document.
