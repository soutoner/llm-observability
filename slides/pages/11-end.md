---
layout: section
number: "07"
---

# Key takeaways

::subtitle::

<p class="section-sub">What to bring back from this session</p>

---

# Key takeaways

<v-clicks>

<div style="margin-bottom: 1rem; padding: 1rem 1.2rem; background: rgba(40,48,70,0.05); border-radius: 10px;">
  <span style="color: #4DD699; font-weight: 700;">01 &nbsp;</span>
  <strong>Agents are loops</strong> — traditional request tracing misses the recursion. You need nested spans per ReAct iteration.
</div>

<div style="margin-bottom: 1rem; padding: 1rem 1.2rem; background: rgba(40,48,70,0.05); border-radius: 10px;">
  <span style="color: #4DD699; font-weight: 700;">02 &nbsp;</span>
  <strong>Traditional telemetry falls short</strong> — spans and logs don't capture prompts, tokens, or cost. You need telemetry that understands the model.
</div>

<div style="padding: 1rem 1.2rem; background: rgba(40,48,70,0.05); border-radius: 10px;">
  <span style="color: #4DD699; font-weight: 700;">03 &nbsp;</span>
  <strong>Non-determinism raises the stakes</strong> — the same input can produce different outputs. Observability isn't optional; it's the only way to reason about what your agent actually did.
</div>

</v-clicks>

---

# The code is on GitHub

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 65vh; gap: 2rem;">

<div style="padding: 2rem 3rem; background: rgba(40,48,70,0.06); border-radius: 16px; text-align: center; border: 2px dashed rgba(120,116,240,0.3);">
  <p style="font-size: 1.1rem; color: #283046; opacity: 0.6; margin: 0 0 0.5rem;"><!-- replace with actual repo URL --></p>
  <p style="font-size: 1.6rem; font-weight: 700; color: #7874F0; font-family: monospace; margin: 0;">github.com/YOUR_ORG/YOUR_REPO</p>
</div>

<p style="color: #283046; opacity: 0.6; font-size: 0.9rem;">Demo agent · Docker Compose stack · instrumented with Langfuse</p>

</div>

<!--
Replace the URL above with the actual GitHub repo before presenting.
-->

---
layout: image
image: /feedback.svg
---
