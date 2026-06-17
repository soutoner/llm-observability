# OpenTelemetry

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 0.5rem; align-items: start;">
  <div>
    <p style="font-size: 0.88rem; color: #283046; line-height: 1.6; margin: 0 0 0.75rem;">
      The open standard for collecting logs, metrics, and traces — any language, any vendor.
    </p>

<v-clicks>

- SDKs for Python, Go, JS, Java…
- Auto-instrumentation for common frameworks
- Vendor-neutral: Grafana, Datadog, Jaeger…
- CNCF graduated project — industry standard

</v-clicks>

  </div>
  <v-click>
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1rem;">
    <div style="font-weight: 600; color: #7874F0; margin-bottom: 0.6rem; font-size: 0.82rem;">Trace an HTTP request end-to-end</div>

```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def get_user(user_id: int):
    with tracer.start_as_current_span("get_user") as span:
        span.set_attribute("user.id", user_id)
        user = db.query(User).get(user_id)
        span.set_attribute("db.rows_returned", 1)
        return user
```

  </div>
  </v-click>
</div>

<!--
Show OTel as the established foundation before introducing why it's not enough for LLMs.
-->
