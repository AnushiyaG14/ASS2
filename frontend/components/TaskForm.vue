<script setup lang="ts">
import { ref } from 'vue'
import Toast from './Toast.vue'

const name = ref('')
const type = ref('notification')
const execution_time = ref(1)
const toast = ref<InstanceType<typeof Toast>>()
const config = useRuntimeConfig()
async function submit() {
  try {
    await $fetch(`${config.public.apiBase}/tasks/`, {
        method: 'POST',
        body: {
            name: name.value,
            type: type.value,
            execution_time: execution_time.value
        }
        })
  } catch {
    toast.value?.notify('Failed to create task', 'error')
  }
}
</script>

<template>
  <form @submit.prevent="submit">
    <input v-model="name" placeholder="Task name" required />
    <select v-model="type">
      <option value="notification">Notification</option>
      <option value="processing">Processing</option>
    </select>
    <input type="number" v-model="execution_time" min="1" max="60" />
    <button>Create</button>
  </form>

  <Toast ref="toast" />
</template>
