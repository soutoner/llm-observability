.PHONY: help up down logs fmt demo-raw demo demo-regression slides clean

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "  fmt               Format Python code"
	@echo "  up                Start Langfuse (http://localhost:3000)"
	@echo "  down              Stop containers, keep data"
	@echo "  logs              Tail Langfuse logs"
	@echo "  demo-raw          Run the agent without instrumentation"
	@echo "  demo              Run the instrumented agent"
	@echo "  demo-regression   Run good-data vs bad-data regression demo"
	@echo "  slides            Start Slidev dev server"
	@echo "  clean             Remove containers, volumes, and images"

up:
	docker compose up -d
	@echo "Langfuse → http://localhost:3000  (demo@example.com / demo1234)"

down:
	docker compose down

logs:
	docker compose logs -f langfuse

fmt:
	uv run --project demo ruff format demo/

demo:
	uv run --project demo python demo/agent.py

demo-regression:
	uv run --project demo python demo/regression.py

slides:
	cd slides && pnpm install --frozen-lockfile && pnpm dev

clean:
	docker compose down -v --rmi local
