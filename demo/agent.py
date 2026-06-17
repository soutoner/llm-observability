import json
import os
from dotenv import load_dotenv
from langfuse.openai import OpenAI
from langfuse import observe
from tools import TOOLS, SEARCH_DB_REAL_GOOD, SYSTEM_PROMPT, make_search, calculate

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL", "http://localhost:11434/v1"),
    api_key=os.getenv("OPENAI_API_KEY", "ollama"),
)
MODEL = os.getenv("MODEL", "qwen2.5:7b")
TOOL_MAP = {"search": make_search(SEARCH_DB_REAL_GOOD), "calculate": calculate}


@observe()
def call_tool(name: str, args: dict) -> str:
    return TOOL_MAP[name](**args)


@observe()
def run_agent(question: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    while True:
        response = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
        msg = response.choices[0].message

        if msg.tool_calls:
            messages.append(msg)
            for tc in msg.tool_calls:
                result = call_tool(tc.function.name, json.loads(tc.function.arguments))
                messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})
        else:
            return msg.content


if __name__ == "__main__":
    question = "What is 15% of the population of Spain?"
    print(f"Q: {question}\nA: {run_agent(question)}")
    langfuse_host = os.getenv("LANGFUSE_HOST", "http://localhost:3000")
    print(f"\nTraces → {langfuse_host}/project/llm-observability/traces")
