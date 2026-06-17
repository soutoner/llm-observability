---
layout: section
number: "06"
---

# Demo

::subtitle::

<p class="section-sub">Run the instrumented agent. Watch the trace land in Langfuse.</p>

---

# The agent

<video :src="'./demo-agent.mp4'" controls style="display: block; max-width: 100%; max-height: 370px; margin: 0.75rem auto 0; border-radius: 12px;" />

<!--
Walk through the trace: total latency + cost at the top, expand the agent span to see both ReAct iterations, each LLM call shows the full prompt and token usage, each tool call shows name + args + result.
-->

---

# Regression detection

<video :src="'./demo-regression.mp4'" controls style="display: block; max-width: 100%; max-height: 370px; margin: 0.75rem auto 0; border-radius: 12px;" />

<!--
Show how the regression is detected in Langfuse: scores drop, alerts fire, traces pinpoint the broken prompt or tool call.
-->
