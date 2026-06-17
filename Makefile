.PHONY: help fmt slides \
        docker-up docker-down docker-logs docker-clean \
        run run-raw run-regression \
        model-pull model-run model-stop model-rm

MODEL_NAME ?= qwen2.5:7b

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "  fmt                 Format Python code"
	@echo "  slides              Start Slidev dev server"
	@echo ""
	@echo "  docker-up           Start Langfuse (http://localhost:3000)"
	@echo "  docker-down         Stop containers, keep data"
	@echo "  docker-logs         Tail Langfuse logs"
	@echo "  docker-clean        Remove containers, volumes, and images"
	@echo ""
	@echo "  run                 Run the instrumented agent"
	@echo "  run-raw             Run the agent without instrumentation"
	@echo "  run-regression      Run good-data vs bad-data regression demo"
	@echo ""
	@echo "  model-pull          Download $(MODEL_NAME) via Ollama"
	@echo "  model-run           Start an interactive session with $(MODEL_NAME)"
	@echo "  model-stop          Unload $(MODEL_NAME) from memory"
	@echo "  model-rm            Delete $(MODEL_NAME) from disk"

fmt:
	uv run --project demo ruff format demo/

slides:
	cd slides && pnpm install --frozen-lockfile && pnpm dev

docker-up:
	docker compose up -d
	@echo "Langfuse → http://localhost:3000  (demo@example.com / demo1234)"

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f langfuse

docker-clean:
	docker compose down -v --rmi local

run:
	uv run --project demo python demo/agent.py

run-raw:
	uv run --project demo python demo/agent_raw.py

run-regression:
	uv run --project demo python demo/regression.py

model-pull:
	ollama pull $(MODEL_NAME)

model-run:
	ollama run $(MODEL_NAME)

model-stop:
	ollama stop $(MODEL_NAME)

model-rm:
	ollama rm $(MODEL_NAME)
