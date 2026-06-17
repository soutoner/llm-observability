import math

SEARCH_DB_REAL_GOOD = {
    "population of spain": "Spain has approximately 47 million people (2024).",
}

# Empty — tool finds nothing, model hallucinates
SEARCH_DB_EMPTY: dict = {}


SYSTEM_PROMPT = (
    "You are a helpful assistant. "
    "Always answer in exactly one sentence: state the population, then the result. "
    "Always call tools one at a time, never in parallel."
)


def make_search(db: dict):
    def search(query: str) -> str:
        q = query.lower()
        for key, value in db.items():
            if any(word in q for word in key.split()):
                return value
        return f"No results found for: {query}"

    return search


def calculate(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {"math": math})
        return str(result)
    except Exception as e:
        return f"Error evaluating '{expression}': {e}"


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": "Search the web for factual information",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string", "description": "The search query"}},
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a mathematical expression and return the result",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A valid Python math expression, e.g. '2000 * 0.12'",
                    }
                },
                "required": ["expression"],
            },
        },
    },
]
