# LangChain AI Assistant

A simple Retrieval-Augmented Generation (RAG) and general-knowledge Q&A assistant built with LangChain, FAISS, and Hugging Face models. It loads a local knowledge base, retrieves relevant context for a question, and returns a structured JSON response.

## Features

- **Document loading & chunking** — loads a Markdown/text knowledge base and splits it into manageable chunks.
- **Vector search** — embeds chunks with a Hugging Face sentence-transformer model and stores them in a FAISS vector store.
- **RAG pipeline** — retrieves the most relevant chunks for a given question and passes them to the LLM as context.
- **General knowledge fallback** — answers questions outside the knowledge base using the model's own knowledge.
- **Structured output** — responses are returned as JSON (`answer`, `source`, `confidence`) instead of raw text.

## Tech Stack

- [LangChain](https://www.langchain.com/) — orchestration framework
- [Hugging Face](https://huggingface.co/) — embeddings + LLM inference (`langchain-huggingface`)
- [FAISS](https://github.com/facebookresearch/faiss) — vector similarity search
- Python 3.10+

## Project Structure
langgraph-ai-assistants/
├── app.py # Main application script
├── data/
│ └── notes.md # Knowledge base document
├── requirements.txt # Python dependencies
├── .env # API keys (not committed)
└── README.md

You'll be prompted to ask questions in a loop:

Ask a question (or 'exit'): What is RAG?

Type `exit` to quit.

## Example Output

```json
{
  "answer": "RAG (Retrieval-Augmented Generation) retrieves relevant documents and passes them to a language model as context before generating an answer.",
  "source": "context",
  "confidence": "high"
}
```

## Notes

- The embedding model (`sentence-transformers/all-MiniLM-L6-v2`) downloads automatically on first run and is cached locally.
- The LLM used is `ibm-granite/granite-4.2-3b` via Hugging Face Inference Endpoint — swap `repo_id` in `app.py` to use a different model.
- `.env` and `myvenv/` are excluded from version control via `.gitignore` — never commit API keys.

