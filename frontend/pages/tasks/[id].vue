<script setup lang="ts">
const route = useRoute()
const config = useRuntimeConfig()

const task = await $fetch(
  `${config.public.apiBase}/tasks/${route.params.id}/`
)
</script>

<template>
  <div>
    <h2>Task Details</h2>

    <p><strong>Name:</strong> {{ task.name }}</p>
    <p><strong>Type:</strong> {{ task.type }}</p>
    <p><strong>Status:</strong> {{ task.status }}</p>
    <p><strong>Execution Time:</strong> {{ task.execution_time }} seconds</p>
    <p><strong>Attempts:</strong> {{ task.attempts }}</p>

    <h3>Execution Logs</h3>
    <pre>{{ task.logs }}</pre>
  </div>
</template>
