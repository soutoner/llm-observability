<template>
  <div class="noc-header">
    <img src="/rindus-logo.png" alt="Rindus" class="logo" />
    <span class="brand" :style="{ color: textColor }">navigators of code.</span>
  </div>
</template>

<script setup>
defineProps({
  textColor: {
    type: String,
    default: '#ffffff',
  },
})
</script>

<style scoped>
.noc-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  flex-shrink: 0;
}
.logo {
  height: 22px;
  width: auto;
}
.brand {
  font-family: 'Poppins', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.01em;
}
</style>
