<!-- Section divider: #F4F4F8 outer, #283046 dark card left panel -->
<template>
  <div class="slidev-layout section outer">
    <div class="card">
      <div class="content" :class="{ 'has-bottom': $slots.subtitle || dots?.length }">
        <div class="title-area">
          <div v-if="number" class="section-number">{{ number }}</div>
          <slot />
        </div>
        <div v-if="$slots.subtitle || dots?.length" class="bottom-area">
          <div v-if="dots?.length" class="coral-dots">
            <div v-for="(d, i) in dots" :key="i" class="dot-row">
              <span class="dot" />
              <span class="dot-label">{{ d }}</span>
            </div>
          </div>
          <slot name="subtitle" />
        </div>
      </div>
    </div>
    <div class="right-panel">
      <span class="brand-right">navigators of code.</span>
      <div v-if="$slots.right" class="right-slot">
        <slot name="right" />
      </div>
      <span v-else class="arrow-right">→</span>
    </div>
  </div>
</template>

<script setup>
defineProps(['number', 'dots'])
</script>

<style scoped>
.outer {
  width: 100%;
  height: 100%;
  background: #F4F4F8;
  display: flex;
  padding: 18px;
  box-sizing: border-box;
  gap: 0;
}
.card {
  background: #283046;
  border-radius: 24px;
  width: 51%;
  height: 100%;
  padding: 32px 36px;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  flex-shrink: 0;
}
.content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.content.has-bottom {
  justify-content: space-between;
}
.bottom-area {
  flex-shrink: 0;
}
.right-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-end;
  padding: 0 8px 0 20px;
}
.brand-right {
  font-family: 'Poppins', sans-serif;
  font-size: 0.7rem;
  font-weight: 700;
  color: #283046;
}
.arrow-right {
  font-size: 2.2rem;
  color: #283046;
  font-weight: 300;
  line-height: 1;
}
.right-slot {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 1rem 0;
}
</style>
