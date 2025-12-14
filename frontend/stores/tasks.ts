import { defineStore } from "pinia"

export interface Task {
  id: number
  name: string
  type: "notification" | "processing"
  execution_time: number
  status: "Pending" | "Running" | "Completed" | "Failed"
  attempts: number
  logs: string
}

export const useTasksStore = defineStore("tasks", {
  state: () => ({
    tasks: [] as Task[]
  }),

  actions: {
    async fetchTasks() {
      const config = useRuntimeConfig()

      this.tasks = await $fetch<Task[]>(
        `${config.public.apiBase}/tasks/`
      )
    }
  }
})
