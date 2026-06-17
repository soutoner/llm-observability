---
layout: section
number: "02"
---

# The ReAct loop

::subtitle::

<p class="section-sub">The dominant pattern for tool-calling agents</p>

---

# ReAct: Reason + Act

<p style="color: #7874F0; font-weight: 600; margin-bottom: 1.2rem;">The dominant pattern for tool-calling agents (Yao et al., 2022)</p>

<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin-top: 0.5rem;">
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1rem; text-align: center;">
    <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">🤔</div>
    <div style="font-weight: 700; color: #7874F0; margin-bottom: 0.4rem;">Thought</div>
    <div style="font-size: 0.82rem; color: #283046; opacity: 0.8;">LLM reasons about what to do next</div>
  </div>
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1rem; text-align: center;">
    <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">⚡</div>
    <div style="font-weight: 700; color: #7874F0; margin-bottom: 0.4rem;">Action</div>
    <div style="font-size: 0.82rem; color: #283046; opacity: 0.8;">Calls a tool with specific arguments</div>
  </div>
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1rem; text-align: center;">
    <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">👁</div>
    <div style="font-weight: 700; color: #7874F0; margin-bottom: 0.4rem;">Observation</div>
    <div style="font-size: 0.82rem; color: #283046; opacity: 0.8;">Tool result fed back into context</div>
  </div>
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1rem; text-align: center;">
    <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">🔁</div>
    <div style="font-weight: 700; color: #7874F0; margin-bottom: 0.4rem;">Repeat</div>
    <div style="font-size: 0.82rem; color: #283046; opacity: 0.8;">Until the LLM has enough to answer</div>
  </div>
</div>

<v-click>

<p style="margin-top: 1.2rem; font-weight: 600;">The loop runs <strong style="color: #7874F0;">inside a single user request</strong>. Each iteration is a separate LLM call — invisible without tracing.</p>

</v-click>

<!--
ReAct is the reasoning pattern behind most tool-calling agents today. The model alternates between thinking and acting. Without tracing, every iteration is invisible.
-->

---

# ReAct: The Loop

```mermaid
flowchart LR
    U([User Request]) --> T
    U ~~~ D

    T["🤔 Thought\nReason about next step"] --> A["⚡ Action\nCall a tool"] --> O["👁 Observation\nTool result → context"] --> T
    T -->|"enough info"| D(["✅ Final Answer"])

    style T fill:#7874F0,color:#fff,stroke:none
    style A fill:#E8854A,color:#fff,stroke:none
    style O fill:#4ABEAA,color:#fff,stroke:none
    style D fill:#28304680,color:#fff,stroke:none
    style U fill:#28304620,stroke:#283046,color:#283046
```

<p style="margin-top: 1rem; font-weight: 600; color: #283046; opacity: 0.8;">Each iteration is a separate LLM call — <strong style="color: #7874F0;">invisible without tracing</strong>.</p>

<!--
The diagram makes the loop explicit: Thought drives Action, Action returns an Observation, which feeds the next Thought. The cycle exits only when the model decides it has enough to answer.
-->
