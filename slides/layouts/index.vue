<template>
  <div class="slidev-layout index outer">
    <div class="card">
      <NocHeader text-color="#283046" />

      <div class="index-title">Index</div>

      <div class="grid">
        <div v-for="(item, index) in items" :key="item" class="item">
          <span class="num">{{ String(index + 1).padStart(2, '0') }}</span>
          <span class="label">{{ item }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import NocHeader from '../components/NocHeader.vue'

defineProps(['items'])
</script>

<style scoped>
.outer {
  width: 100%;
  height: 100%;
  background: #283046;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 18px;
  box-sizing: border-box;
}
.card {
  background: #F4F4F8;
  border-radius: 24px;
  width: 100%;
  height: 100%;
  padding: 28px 48px 36px;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}
.index-title {
  font-family: 'Poppins', sans-serif;
  font-size: 4.5rem;
  font-weight: 800;
  color: transparent;
  -webkit-text-stroke: 2.5px #7874F0;
  line-height: 1.1;
  margin: 8px 0 20px;
  letter-spacing: -0.01em;
}
.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  flex: 1;
  align-content: start;
}
.item {
  display: flex;
  align-items: center;
  gap: 14px;
  background: #ffffff;
  border-radius: 10px;
  padding: 12px 18px;
}
.num {
  font-family: 'Poppins', sans-serif;
  font-size: 1.15rem;
  font-weight: 800;
  color: transparent;
  -webkit-text-stroke: 1.5px #4DD699;
  flex-shrink: 0;
  letter-spacing: 0.02em;
}
.label {
  font-family: 'Poppins', sans-serif;
  font-size: 0.95rem;
  font-weight: 600;
  color: #283046;
}
</style>
