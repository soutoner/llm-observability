---
layout: section
number: "03"
---

# You deployed an agent. A user got a wrong answer. Now what?

::right::

<img :src="'/meme-non-determinism.jpg'" style="width: 90%; border-radius: 12px;" />

<!--
Open with this. Let it land. That's the problem we're solving today.
-->

---

# The logs say nothing useful

<div class="terminal">
  <div class="term-bar">
    <span class="dot red"></span>
    <span class="dot yellow"></span>
    <span class="dot green"></span>
  </div>
  <div class="term-body">
    <div v-click class="term-line">
      <span class="prompt">$</span> python agent.py "What is 15% of the population of Spain?"
    </div>
    <div v-click class="term-line output">Q: What is 15% of the population of Spain?</div>
    <div v-click class="term-line output">A: ~7.05 million people</div>
  </div>
</div>

<v-clicks>

- Did we use any tool in the process?
- What was the exact prompt on each loop iteration?
- How many tokens did it consume? What did that cost?
- Did it hallucinate Spain's population instead of looking it up?
- Where did most of the time go — the LLM, or the tool calls?

</v-clicks>

<style>
.terminal {
  margin: 0 0 0.75rem;
  background: #1e2333;
  border-radius: 12px;
  overflow: hidden;
  font-family: 'JetBrains Mono', monospace;
  box-shadow: 0 8px 24px rgba(0,0,0,0.25);
}
.term-bar {
  display: flex;
  gap: 8px;
  padding: 10px 14px;
  background: #161a26;
}
.dot { width: 11px; height: 11px; border-radius: 50%; }
.dot.red { background: #ff5f57; }
.dot.yellow { background: #febc2e; }
.dot.green { background: #28c840; }
.term-body { padding: 1rem 1.2rem; }
.term-line { font-size: 0.95rem; line-height: 1.8; color: #e4e6ef; }
.term-line .prompt { color: #4DD699; margin-right: 0.5rem; }
.term-line.output { color: #9ea3c4; }
</style>

<!--
The request succeeded and the answer is even correct. That's all you know. Traditional observability stops here — it can't see inside the ReAct loop.
-->

