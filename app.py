import os
import json
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Set up the chat model
llm = HuggingFaceEndpoint(
    repo_id="ibm-granite/granite-4.2-3b",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)
chat_model = ChatHuggingFace(llm=llm)

# Prompt for general knowledge, structured JSON output
prompt = ChatPromptTemplate.from_template(
    "Answer the following question using your own general knowledge.\n\n"
    "Question: {question}\n\n"
    "Respond ONLY with valid JSON in exactly this format, no extra text, "
    "no markdown code fences:\n"
    '{{"answer": "your answer here", "confidence": "high", "medium", or "low"}}'
)

def ask(question: str):
    messages = prompt.format_messages(question=question)
    response = chat_model.invoke(messages)

    raw = response.content.strip()
    if raw.startswith("```"):
        raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        structured = json.loads(raw)
    except json.JSONDecodeError:
        print("Warning: could not parse JSON, raw output was:", raw)
        structured = {"answer": raw, "confidence": "low"}

    return structured

if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or 'exit'): ")
        if q.lower() == "exit":
            break
        result = ask(q)
        print(json.dumps(result, indent=2))