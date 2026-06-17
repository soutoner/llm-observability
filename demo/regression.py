import json
import os
from dotenv import load_dotenv
from langfuse.openai import OpenAI
from langfuse import observe, get_client, propagate_attributes
from tools import (
    TOOLS,
    SEARCH_DB_REAL_GOOD,
    SEARCH_DB_EMPTY,
    SYSTEM_PROMPT,
    make_search,
    calculate,
)

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL", "http://localhost:11434/v1"),
    api_key=os.getenv("OPENAI_API_KEY", "ollama"),
)
MODEL = os.getenv("MODEL", "qwen2.5:7b")
langfuse = get_client()

QUESTION = "What is 15% of the population of Spain?"


@observe()
def run_agent(
    question: str, tool_map: dict, scenario: str, system_prompt: str | None = None
) -> str:
    with propagate_attributes(tags=[scenario]):
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": question})

        while True:
            response = client.chat.completions.create(
                model=MODEL, messages=messages, tools=TOOLS, parallel_tool_calls=False
            )
            msg = response.choices[0].message

            if msg.tool_calls:
                messages.append(msg)
                for tc in msg.tool_calls:
                    with langfuse.start_as_current_observation(name=tc.function.name) as span:
                        args = json.loads(tc.function.arguments)
                        result = tool_map[tc.function.name](**args)
                        span.update(input=args, output=result)
                    messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})
            else:
                return msg.content


def run(label: str, question: str, db: dict, system_prompt: str | None = None) -> str:
    tool_map = {"search": make_search(db), "calculate": calculate}
    return run_agent(question, tool_map, label, system_prompt)


if __name__ == "__main__":
    for label, db in [("working", SEARCH_DB_REAL_GOOD), ("hallucinating", SEARCH_DB_EMPTY)]:
        answer = run(label, QUESTION, db, SYSTEM_PROMPT)
        print(f"[{label}]\n  Q: {QUESTION}\n  A: {answer}\n")

    print(
        "Both answers look plausible — open Langfuse to see what the search tool actually returned."
    )
    langfuse.flush()
    langfuse_host = os.getenv("LANGFUSE_HOST", "http://localhost:3000")
    print(f"Traces → {langfuse_host}/project/llm-observability/traces")
