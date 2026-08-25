# two-agent-grounded-qa
# Two-Agent Grounded Q&A Assistant

## Overview

A grounded question-answering assistant for Rich Dad Poor Dad.

## Architecture

User
→ Researcher Agent
→ Qdrant
→ Draft Answer
→ Reviewer Agent
→ Final Answer

## Technologies

- Python
- LangChain
- OpenAI
- Qdrant
- Streamlit

## How to Run

1. Install dependencies
2. Configure .env
3. Run ingestion
4. Run Streamlit

## Environment Variables

OPENAI_API_KEY
QDRANT_URL
QDRANT_API_KEY
...
