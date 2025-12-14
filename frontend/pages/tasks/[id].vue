<script setup>
const route = useRoute()
const { data } = await useFetch(`${config.public.apiBase}/tasks/${route.params.id}` )
</script>

<template>
  <h2>{{ data.name }}</h2>
  <pre>{{ data.logs }}</pre>
</template>
