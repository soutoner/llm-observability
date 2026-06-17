---
layout: section
number: "01"
---

# What is observability?

::subtitle::

<p class="section-sub">Not logging. Not monitoring. Something more specific.</p>

---

# The three pillars

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 0.5rem;">
  <v-click>
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1rem; text-align: center;">
    <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">📝</div>
    <div style="font-weight: 700; color: #7874F0; margin-bottom: 0.4rem;">Logs</div>
    <div style="font-size: 0.82rem; color: #283046; opacity: 0.8;">Discrete events — what happened, when</div>
  </div>
  </v-click>
  <v-click>
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1rem; text-align: center;">
    <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">📊</div>
    <div style="font-weight: 700; color: #7874F0; margin-bottom: 0.4rem;">Metrics</div>
    <div style="font-size: 0.82rem; color: #283046; opacity: 0.8;">Aggregated numbers — rates, latencies, counts</div>
  </div>
  </v-click>
  <v-click>
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1rem; text-align: center;">
    <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">🔗</div>
    <div style="font-weight: 700; color: #7874F0; margin-bottom: 0.4rem;">Traces</div>
    <div style="font-size: 0.82rem; color: #283046; opacity: 0.8;">The full path of one request, step by step</div>
  </div>
  </v-click>
</div>

<v-click>

<div style="margin-top: 1.2rem; padding: 0.85rem 1.2rem; border-left: 3px solid #7874F0; background: rgba(120,116,240,0.08); border-radius: 0 8px 8px 0; font-weight: 600; color: #283046;">
  Observability is the process of making a system's internal state more transparent - <br>
  this way you can answer questions you didn't think in advance.
</div>

</v-click>

<!--
Set the baseline definition here so "the problem with LLMs" lands as a gap relative to this, not a vague complaint.
-->

---

# The three pillars — in practice

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 0.5rem;">
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1rem;">
    <div style="font-weight: 700; color: #7874F0; margin-bottom: 0.6rem;">Logs</div>
    <div style="font-size: 0.78rem; color: #283046; opacity: 0.85; font-family: monospace; background: rgba(0,0,0,0.04); border-radius: 6px; padding: 0.5rem; line-height: 1.6;">
      ERROR 14:02:31<br>
      service=checkout<br>
      user=u_8821<br>
      msg="payment gateway timeout"<br>
      order_id=ord_4492
    </div>
    <div style="font-size: 0.78rem; color: #283046; opacity: 0.7; margin-top: 0.5rem;">A single event, timestamped, with context</div>
  </div>
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1rem;">
    <div style="font-weight: 700; color: #7874F0; margin-bottom: 0.6rem;">Metrics</div>
    <div style="font-size: 0.78rem; color: #283046; opacity: 0.85; font-family: monospace; background: rgba(0,0,0,0.04); border-radius: 6px; padding: 0.5rem; line-height: 1.6;">
      http_latency_p99 = 420ms<br>
      http_requests_per_sec = 1200<br>
      http_error_rate = 0.3%<br>
      db_pool_wait_ms = 12
    </div>
    <div style="font-size: 0.78rem; color: #283046; opacity: 0.7; margin-top: 0.5rem;">Aggregated over time — trends and thresholds</div>
  </div>
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1rem;">
    <div style="font-weight: 700; color: #7874F0; margin-bottom: 0.6rem;">Traces</div>
    <div style="font-size: 0.78rem; color: #283046; opacity: 0.85; font-family: monospace; background: rgba(0,0,0,0.04); border-radius: 6px; padding: 0.5rem; line-height: 1.6;">
      req_id: a3f9<br>
      ├─ auth        18ms<br>
      ├─ db_query    95ms<br>
      ├─ cache_read   3ms<br>
      └─ render      12ms
    </div>
    <div style="font-size: 0.78rem; color: #283046; opacity: 0.7; margin-top: 0.5rem;">One request, every step, end-to-end</div>
  </div>
</div>
