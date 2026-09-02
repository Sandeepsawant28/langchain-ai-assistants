# About LangChain

LangChain is a framework for building applications powered by large language models (LLMs).
It provides tools for chaining together prompts, models, memory, and external data sources.

## Key Components

- **Document Loaders**: Load data from files, websites, databases, and more into a standard format.
- **Text Splitters**: Break large documents into smaller chunks so they fit within a model's context window.
- **Embeddings**: Convert text into numerical vectors that capture semantic meaning.
- **Vector Stores**: Store and search embeddings efficiently (e.g. FAISS, Chroma, Pinecone).
- **Chains**: Combine multiple steps — like retrieval plus generation — into a single pipeline.
- **Agents**: Let an LLM decide which tools to call and in what order, based on the task.

## Retrieval-Augmented Generation (RAG)

RAG is a technique where relevant documents are retrieved from a knowledge base and passed
to a language model as context before it generates an answer. This helps the model answer
questions using information it wasn't originally trained on, such as private documents or
recent data.

A typical RAG pipeline works like this:

1. Load and split documents into chunks.
2. Embed each chunk and store it in a vector database.
3. When a question comes in, embed the question and search for the most similar chunks.
4. Pass those chunks as context to the language model along with the question.
5. The model generates an answer grounded in the retrieved context.

## Why Use LangGraph

LangGraph extends LangChain by letting you build stateful, multi-step workflows as a graph
of nodes. This is useful for agents that need to loop, branch, or maintain memory across
multiple steps rather than following a single linear chain.