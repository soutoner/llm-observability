<!-- Default content: #C3CDE2 outer, #F4F4F8 rounded card -->
<template>
  <div class="slidev-layout default outer">
    <div class="card">
      <NocHeader text-color="#283046" />
      <div class="content">
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup>
import NocHeader from '../components/NocHeader.vue'
</script>

<style scoped>
.outer {
  width: 100%;
  height: 100%;
  background: #C3CDE2;
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
  padding: 28px 48px 32px;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}
.content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding-top: 6px;
  overflow: hidden;
}
</style>
