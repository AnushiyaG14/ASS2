<script setup>
const config = useRuntimeConfig()
const { data: tasks, refresh } = await useFetch(
  `${config.public.apiBase}/tasks/`
)

setInterval(refresh, 3000)
</script>

<template>
  <TaskForm />
  <table>
    <tr v-for="t in tasks" :key="t.id">
      <td><NuxtLink :to="`/tasks/${t.id}`">{{ t.name }}</NuxtLink></td>
      <td>{{ t.status }}</td>
      <td>{{ t.execution_time }}</td>
      <td>{{ t.attempts }}</td>
    </tr>
  </table>
</template>
