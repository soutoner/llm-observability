---
layout: section
number: "04"
---

# Langfuse

::subtitle::

<p class="section-sub">Open-source LLM observability built on OpenTelemetry</p>

---

# Langfuse

<p style="color: #7874F0; font-weight: 600; margin-bottom: 1rem;">Open-source LLM observability platform</p>

<v-clicks>

- **Built on OpenTelemetry** — a native OTel backend that extends it with LLM-specific data: tokens, cost, prompts, and generations
- **Traces** every LLM call, tool call, and step — with full inputs/outputs
- **Open-source** (MIT) and self-hostable via Docker Compose, or use Langfuse Cloud
- **SDKs** for Python, TypeScript, and any OpenAI-compatible API
- **Drop-in OpenAI wrapper** — one import change, no refactor
- **Evaluations** — score traces programmatically or via human review

</v-clicks>

<!--
Open source, MIT license. Self-host from day one — no production data leaves your infra.
-->

---

# Langfuse & OpenTelemetry

<div class="flex justify-center items-center" style="height: 70vh;">
<div style="transform: scale(2.6);">

```mermaid
flowchart LR
    subgraph AgentCode["Our Agent Code"]
        subgraph LangfuseSDK["Langfuse SDK"]
            OTelSDK["OTel SDK"]
        end
    end

    subgraph LangfusePlatform["Langfuse Platform"]
        Backend["OTel Backend"]
        UI["UI + Analytics"]
        Backend --> UI
    end

    LangfuseSDK -- "OTLP + LLM\ntokens · cost · prompts" --> Backend

    style AgentCode fill:#fde8d8,stroke:#E8854A,color:#7a3510
    style LangfuseSDK fill:#fbd0b0,stroke:#E8854A,color:#7a3510
    style LangfusePlatform fill:#ccf0e8,stroke:#4ABEAA,color:#0d5c4c

    classDef codeNode fill:#f5a57a,stroke:#E8854A,color:#7a3510
    classDef obsNode fill:#99e6d4,stroke:#4ABEAA,color:#0d5c4c

    class OTelSDK codeNode
    class Backend,UI obsNode
```

</div>
</div>

<!--
Langfuse SDK wraps OTel SDK — it speaks standard OTLP but enriches every span with LLM-specific attributes (tokens, cost, prompt/completion text). The backend is a native OTel collector, so any plain OTel SDK can also ship traces to it.
-->

---

# Langfuse data model

<div style="font-size: 0.88rem; line-height: 1.6; margin-top: 0.5rem;">
<div style="padding: 0.4rem 1rem; border-left: 4px solid #283046; background: rgba(40,48,70,0.08); border-radius: 0 8px 8px 0; margin-bottom: 0.4rem; display: flex; justify-content: space-between;"><span style="font-weight: 700; font-family: monospace;">Trace</span><span style="opacity: 0.5; font-size: 0.8rem;">one user request, end-to-end</span></div>
<div style="margin-left: 1.5rem;">
<div style="padding: 0.4rem 1rem; border-left: 4px solid #283046; background: rgba(40,48,70,0.05); border-radius: 0 8px 8px 0; margin-bottom: 0.4rem; display: flex; justify-content: space-between;"><span style="font-weight: 700; font-family: monospace;">Span: agent</span><span style="opacity: 0.5; font-size: 0.8rem;">the ReAct loop</span></div>
<div style="margin-left: 1.5rem; display: flex; flex-direction: column; gap: 0.3rem;">
<div style="padding: 0.4rem 1rem; border-left: 4px solid #7874F0; background: rgba(120,116,240,0.08); border-radius: 0 8px 8px 0; display: flex; justify-content: space-between;"><span style="font-weight: 600; font-family: monospace; color: #7874F0;">Span: LLM call</span><span style="opacity: 0.5; font-size: 0.8rem;">Thought 1 — decides to search</span></div>
<div style="padding: 0.4rem 1rem; border-left: 4px solid #E8854A; background: rgba(232,133,74,0.08); border-radius: 0 8px 8px 0; display: flex; justify-content: space-between;"><span style="font-weight: 600; font-family: monospace; color: #E8854A;">Span: tool / search</span><span style="opacity: 0.5; font-size: 0.8rem;">Action 1 + Observation 1</span></div>
<div style="padding: 0.4rem 1rem; border-left: 4px solid #7874F0; background: rgba(120,116,240,0.08); border-radius: 0 8px 8px 0; display: flex; justify-content: space-between;"><span style="font-weight: 600; font-family: monospace; color: #7874F0;">Span: LLM call</span><span style="opacity: 0.5; font-size: 0.8rem;">Thought 2 — decides to calculate</span></div>
<div style="padding: 0.4rem 1rem; border-left: 4px solid #E8854A; background: rgba(232,133,74,0.08); border-radius: 0 8px 8px 0; display: flex; justify-content: space-between;"><span style="font-weight: 600; font-family: monospace; color: #E8854A;">Span: tool / calculate</span><span style="opacity: 0.5; font-size: 0.8rem;">Action 2 + Observation 2</span></div>
<div style="padding: 0.4rem 1rem; border-left: 4px solid #7874F0; background: rgba(120,116,240,0.08); border-radius: 0 8px 8px 0; display: flex; justify-content: space-between;"><span style="font-weight: 600; font-family: monospace; color: #7874F0;">Span: LLM call</span><span style="opacity: 0.5; font-size: 0.8rem;">Final answer</span></div>
</div>
</div>
</div>

<v-click>

<div style="margin-top: 1rem; padding: 0.85rem 1.2rem; border-left: 3px solid #4DD699; background: rgba(77,214,153,0.08); border-radius: 0 8px 8px 0;">
  Each span captures: <strong>input · output · latency · tokens · cost · metadata</strong>
</div>

</v-click>

<!--
A trace is one request from end to end. Spans are the steps inside it — one per ReAct iteration. This nesting is what lets you see exactly where time and tokens went.
-->
