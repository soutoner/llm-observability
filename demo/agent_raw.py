import json
import math
import os
from dotenv import load_dotenv
from openai import OpenAI
from tools import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL", "http://localhost:11434/v1"),
    api_key=os.getenv("OPENAI_API_KEY", "ollama"),
)
MODEL = os.getenv("MODEL", "qwen2.5:7b")

SEARCH_DB = {
    "population of spain": "Spain has approximately 47 million people (2024).",
}


def search(query: str) -> str:
    q = query.lower()
    for key, value in SEARCH_DB.items():
        if any(word in q for word in key.split()):
            return value
    return f"No results found for: {query}"


def calculate(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {"math": math})
        return str(result)
    except Exception as e:
        return f"Error evaluating '{expression}': {e}"


TOOL_MAP = {"search": search, "calculate": calculate}

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": "Search the web for factual information",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a mathematical expression",
            "parameters": {
                "type": "object",
                "properties": {"expression": {"type": "string"}},
                "required": ["expression"],
            },
        },
    },
]


def call_tool(name: str, args: dict) -> str:
    return TOOL_MAP[name](**args)


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
