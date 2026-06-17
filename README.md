# LLM Observability in Practice

45-minute talk on tracing agents with Langfuse. Hands-on demo using a Python tool-calling agent.

Slides available at https://soutoner.github.io/llm-observability

## Prerequisites

| Tool                                          | Version | Install                                                                   |
| --------------------------------------------- | ------- | ------------------------------------------------------------------------- |
| [Docker](https://docs.docker.com/get-docker/) | 24+     | Required for Langfuse                                                     |
| [Python](https://python.org)                  | 3.10+   | Required for the demo                                                     |
| [uv](https://docs.astral.sh/uv/)              | latest  | `curl -LsSf https://astral.sh/uv/install.sh \| sh`                        |
| [Ollama](https://ollama.com)                  | latest  | Run natively — **do not containerise** (no GPU access in Docker on macOS) |
| [Node.js](https://nodejs.org)                 | 18+     | Required for the slides                                                   |
| [pnpm](https://pnpm.io)                       | 8+      | `npm install -g pnpm`                                                     |

> **Cloud LLM alternative:** if you skip Ollama, set `MODEL=gpt-4o` and `OPENAI_API_KEY=sk-...` in `demo/.env`.

## Repo structure

```
slides/              # Slidev presentation
demo/                # Python demo agent
  agent_raw.py       # tool-calling agent, no instrumentation
  agent.py           # tool-calling agent with Langfuse tracing
  regression.py      # good-data vs bad-data comparison (two scenarios)
  tools.py           # mock search + calculator tools
  pyproject.toml
  .env.example
docker-compose.yml   # Langfuse + Postgres
```

## Quick start

```bash
make docker-up       # start Langfuse
cp demo/.env.example demo/.env
make model-pull      # download qwen2.5:7b
make run             # run the agent
make slides          # start the slide deck
```

Run `make` with no arguments to see all available targets.

## Setup

### 1. Start Langfuse

The `docker-compose.yml` starts two containers: **Langfuse** (port 3000) and **Postgres** (port 5432).

```bash
make docker-up
```

Langfuse starts pre-configured with a demo user and fixed API keys — no manual setup needed:

|          |                       |
| -------- | --------------------- |
| URL      | http://localhost:3000 |
| Email    | `demo@example.com`    |
| Password | `demo1234`            |

Sign-ups are disabled. API keys are pre-seeded and already match `demo/.env.example`.

```bash
make docker-down     # stop containers, keep data
make docker-clean    # remove containers, volumes, and images
```

### 2. Configure the demo

```bash
cp demo/.env.example demo/.env
```

The Langfuse keys in `.env.example` match the pre-seeded project — no edits needed unless you change the defaults in `docker-compose.yml`.

### 3. Pull the local model (Ollama)

```bash
make model-pull        # download qwen2.5:7b
make model-run         # start an interactive session (optional, for testing)
make model-stop        # unload the model from memory
make model-rm          # delete the model from disk
```

Override the model name with `make model-pull MODEL_NAME=llama3.2`.

To use a cloud model instead, set `MODEL=gpt-4o` and `OPENAI_API_KEY=sk-...` in `demo/.env`.

### 4. Run the demo

```bash
make run               # run with Langfuse tracing
make run-regression    # run good-data vs bad-data comparison
```

Check traces at http://localhost:3000/traces.

### 5. Run the slides

```bash
make slides
```
