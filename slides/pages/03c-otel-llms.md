# OTel + LLMs: what you get

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 0.75rem;">
  <div style="background: rgba(40,48,70,0.06); border-radius: 12px; padding: 1.2rem;">
    <p style="font-weight: 700; color: #283046; margin: 0 0 0.75rem;">Spans give you</p>
    <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.88rem; color: #283046;">
      <li style="padding: 0.3rem 0; border-bottom: 1px solid rgba(40,48,70,0.08);">Request latency end-to-end</li>
      <li style="padding: 0.3rem 0; border-bottom: 1px solid rgba(40,48,70,0.08);">HTTP status — success or error</li>
      <li style="padding: 0.3rem 0; border-bottom: 1px solid rgba(40,48,70,0.08);">Model name, API endpoint</li>
      <li style="padding: 0.3rem 0;">Retry count, timeout events</li>
    </ul>
  </div>
  <v-click>
  <div style="background: rgba(120,116,240,0.1); border-radius: 12px; padding: 1.2rem;">
    <p style="font-weight: 700; color: #7874F0; margin: 0 0 0.75rem;">Still dark</p>
    <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.88rem; color: #283046;">
      <li style="padding: 0.3rem 0; border-bottom: 1px solid rgba(120,116,240,0.15);">What prompt was actually sent</li>
      <li style="padding: 0.3rem 0; border-bottom: 1px solid rgba(120,116,240,0.15);">What the model replied</li>
      <li style="padding: 0.3rem 0; border-bottom: 1px solid rgba(120,116,240,0.15);">Token usage and cost per call</li>
      <li style="padding: 0.3rem 0; border-bottom: 1px solid rgba(120,116,240,0.15);">Whether the answer was correct</li>
      <li style="padding: 0.3rem 0;">The full reasoning chain across steps</li>
    </ul>
  </div>
  </v-click>
</div>

<v-click>

<div style="margin-top: 1rem; padding: 0.75rem 1.2rem; border-left: 3px solid #7874F0; background: rgba(120,116,240,0.08); border-radius: 0 8px 8px 0; font-weight: 600; color: #283046; font-size: 0.9rem;">
  A span tells you the call took 3.2 s and succeeded. It says nothing about what happened inside.
</div>

</v-click>

<!--
The point: OTel is not wrong, it's just incomplete. The dark column is what drives the need for LLM-specific observability.
-->
