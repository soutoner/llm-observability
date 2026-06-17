<template>
  <div class="slidev-layout cover outer">
    <div class="card">
      <NocHeader text-color="#ffffff" />

      <div class="body">
        <slot />
      </div>

      <div class="footer">
        <span class="date">{{ date ?? '' }}</span>
        <img src="/anchor-icon.png" alt="" class="anchor" />
      </div>
    </div>
  </div>
</template>

<script setup>
import NocHeader from '../components/NocHeader.vue'

defineProps(['date'])
</script>

<style scoped>
.outer {
  width: 100%;
  height: 100%;
  background: #7874F0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 18px;
  box-sizing: border-box;
}
.card {
  background: #283046;
  border-radius: 24px;
  width: 100%;
  height: 100%;
  padding: 32px 48px 32px;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}
.body {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 16px 0 8px;
}
.footer {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  flex-shrink: 0;
}
.date {
  font-family: 'Poppins', sans-serif;
  font-size: 0.95rem;
  font-weight: 700;
  color: #ffffff;
}
.anchor {
  height: 48px;
  width: auto;
  opacity: 0.85;
}
</style>

<style>
/* Title: large, white, bold — upper portion */
.slidev-layout.cover h1 {
  font-family: 'Poppins', sans-serif !important;
  font-size: 4.6rem !important;
  font-weight: 800 !important;
  line-height: 1.05 !important;
  color: #ffffff !important;
  margin: 0 !important;
  letter-spacing: -0.01em;
}

/* Subtitle: purple, large, bold — lower portion */
.slidev-layout.cover .subtitle {
  font-family: 'Poppins', sans-serif !important;
  font-size: 3.05rem !important;
  font-weight: 700 !important;
  color: #7874F0 !important;
  margin: 0 !important;
}
</style>
