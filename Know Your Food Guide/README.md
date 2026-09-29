# Know Your Food Guide

Know Your Food Guide is a Streamlit application that combines a local RAG assistant with practical shopper tools. It helps users ask food-quality questions, compare unit prices, and look up packaged products by barcode.

## Core capabilities

- Chatbot powered by RAG over food-buying guides (`rag/data/*.md`)
- OpenAI web-search fallback when local guides are insufficient
- Unit price comparison tool call (price per 100 and per base unit)
- Barcode lookup tool call using Open Food Facts (`uk.openfoodfacts.org`)
- Conversation export for chatbot messages (JSON, CSV, PDF)
- Token usage + estimated cost visibility in the UI

## How the RAG flow works

1. User asks a question in Streamlit (`app/main.py`).
2. Router (`rag/router.py`) decides whether the question should use RAG.
3. Retriever pipeline loads indexed chunks from local markdown guides.
4. Generator (`rag/rag_chain.py`) answers with grounded guidance.
5. If needed, fallback (`rag/llmfallback.py`) queries OpenAI web search and returns sources.

## Tool calls included

- `tool_calling/unit_price_comparison.py`
  - Compares two products by amount, unit, and price
  - Returns normalized price metrics to support cheaper-choice decisions

- `tool_calling/barcode_lookup.py`
  - Looks up product details from Open Food Facts via barcode
  - Returns structured product summary and user-friendly markdown output

- `tool_calling/checklist_generation.py`
  - Builds guided shopping checklists from user needs

## Project structure

- `app/main.py` - Streamlit UI and orchestration
- `ui.css` - custom app styling
- `rag/` - retrieval, indexing, prompts, router, chain, fallback
- `rag/data/` - domain knowledge markdown files
- `tool_calling/` - callable utility tools for task-specific operations
- `eval/rag_eval_notebook.ipynb` - notebook-based RAG evaluation workflow
- `eval/ragas_evalset.jsonl` - evaluation dataset
- `eval/results/` - generated evaluation outputs

## Requirements

- Python `>=3.11`
- OpenAI API key

Dependencies are declared in `pyproject.toml`.

## Run locally

### 1) Clone and enter the project

```bash
git clone <your-repo-url>
cd "Know Your Food Guide"
```

### 2) Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -e .
```

### 4) Add environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5) Start the app

```bash
streamlit run app/main.py
```

Open the local URL shown in terminal (usually `http://localhost:8501`).

## Evaluation (optional)

This project includes a runnable notebook for RAG evaluation:

- `eval/rag_eval_notebook.ipynb`

It supports:
- Retrieval checks (`recall@k` style)
- RAGAs metric evaluation (faithfulness and optional full metric set)

Run it from Jupyter/VS Code after dependencies and `.env` are set.

## Notes

- `.env` should not be committed.
- Barcode lookup relies on external API availability.
- Web-search fallback and RAGAs evaluation increase token usage/cost.