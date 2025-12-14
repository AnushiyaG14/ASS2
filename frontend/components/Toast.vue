<script setup lang="ts">
import { ref } from 'vue'

const show = ref(false)
const message = ref('')
const type = ref<'success' | 'error'>('success')

function notify(msg: string, t: 'success' | 'error' = 'success') {
  message.value = msg
  type.value = t
  show.value = true

  setTimeout(() => {
    show.value = false
  }, 3000)
}

defineExpose({ notify })
</script>

<template>
  <div
    v-if="show"
    class="toast"
    :class="type"
  >
    {{ message }}
  </div>
</template>

<style scoped>
.toast {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 12px 16px;
  border-radius: 6px;
  color: white;
  font-weight: 500;
  z-index: 9999;
}
.success { background: #16a34a; }
.error { background: #dc2626; }
</style>
