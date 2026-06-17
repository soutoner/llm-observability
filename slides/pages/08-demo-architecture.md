---
layout: section
number: "05"
---

# Demo architecture

::subtitle::

<p class="section-sub">How the pieces fit together before we touch any code</p>

---

# Architecture

<div style="display: flex; justify-content: center; align-items: center; height: 75vh;">
<div style="transform: scale(2.4) translateX(5%); transform-origin: center center;">

```mermaid
%%{init: {'flowchart': {'rankSpacing': 90, 'nodeSpacing': 60, 'wrappingWidth': 300 }, 'themeVariables': {'fontSize': '26px'}}}%%
flowchart LR
    subgraph PythonCode["Our Python Code"]
        Tools["tools.py\nsearch · calculate"]
        Agent["agent.py\nReAct loop · @observe()"]
        Tools <--> Agent
    end

    subgraph LLMBox["Local LLM"]
        Ollama["Ollama\nqwen2.5:7b"]
    end

    subgraph ObsBox["Observability"]
        Stack["Langfuse stack\ndocker-compose"]
    end

    Agent --> Ollama
    Agent -- "trace events" --> Stack

    style PythonCode fill:#fde8d8,stroke:#E8854A,color:#7a3510
    style LLMBox fill:#ede9fe,stroke:#7874F0,color:#4c1d95
    style ObsBox fill:#ccf0e8,stroke:#4ABEAA,color:#0d5c4c

    classDef pythonNode fill:#fbd0b0,stroke:#E8854A,color:#7a3510
    classDef llmNode fill:#ddd6fe,stroke:#7874F0,color:#4c1d95
    classDef obsNode fill:#99e6d4,stroke:#4ABEAA,color:#0d5c4c

    class Tools,Agent pythonNode
    class Ollama llmNode
    class Stack obsNode
```

</div>
</div>

<!--
agent.py talks to an OpenAI-compatible endpoint served by Ollama. The only instrumentation is swapping the OpenAI import for langfuse.openai and adding @observe(): every chat completion and tool call is now also shipped to the Langfuse stack, which docker-compose brings up as one unit (web, worker, Postgres, ClickHouse, Redis, MinIO).
-->
