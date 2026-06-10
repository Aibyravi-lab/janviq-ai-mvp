# Release Notes

## JANVIQ AI v0.1

Release Date:
2026-06-09

Features:

* Streamlit UI
* OpenAI Integration
* OIM Knowledge Assistant
* Knowledge Base Loader
* Search Engine
* GitHub Integration

Repository:
janviq-ai-mvp

Known Limitations:

* OIM only
* Keyword search only
* No citations

Next Release:
v0.2

Planned Features:

* Source citations
* Better search
* Multi-IAM support
* Saviynt integration
# JANVIQ AI Release Notes


---

## Version: v0.2

Release Date: 10 June 2026

Release Name:
Evidence-Based IAM Assistant


### Overview

JANVIQ AI v0.2 introduces a major enhancement by transforming the MVP from a simple knowledge-based chatbot into an evidence-driven IAM assistant.

The system can now provide answers backed by original IAM documentation with document-level and page-level citations.


### New Features

#### 1. PDF Metadata Extraction

- Extracted knowledge from IAM PDF documents.
- Added document names to every knowledge chunk.
- Added page number references.
- Generated structured `knowledge_chunks.json` containing 4315 knowledge chunks.


#### 2. Citation Search Engine

Implemented a new citation-aware retrieval engine:

- `citation_search.py`
- Question cleaning.
- Stop word filtering.
- Frequency-based relevance scoring.
- Junk content removal.
- OIM-specific ranking optimization.


#### 3. Evidence-Based Answer Generation

Streamlit application upgraded to:

- Retrieve relevant documentation chunks.
- Send verified context to GPT-5.5.
- Generate professional IAM answers.
- Display document and page references.


#### 4. User Experience Improvements

Added:

- Improved JANVIQ AI branding.
- Professional enterprise assistant interface.
- Source reference section for every answer.


### Testing Evidence

Validated with IAM questions including:

- Explain OIM reconciliation types.
- What is trusted reconciliation in OIM.

Result:

- Accurate documentation-based answers.
- Successful citation display.
- Multiple source verification.


### Technical Changes

New Files:

- `pdf_metadata_loader.py`
- `citation_search.py`
- `citation_test.py`
- `knowledge_chunks.json`

Modified Files:

- `app.py`


### Architecture Evolution

v0.1:

Knowledge.txt → Keyword Search → GPT → Answer


v0.2:

PDF Documents → Metadata Extraction → JSON Knowledge Chunks → Citation Search → GPT → Answer + Sources


### Release Status

JANVIQ AI v0.2

Status: Production Ready MVP ✅


### Next Version

v0.3 Intelligence Layer

Planned Features:

- Semantic Search.
- Embeddings.
- Vector Database.
- Confidence Scoring.
- Advanced Retrieval Ranking.
