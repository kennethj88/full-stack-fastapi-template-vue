<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const user = computed(() => authStore.user)

// Redirect if not authenticated
definePageMeta({
  layout: 'dashboard',
  middleware: ['auth']
})
</script>

<template>
  <div class="container mx-auto px-4 py-8">
    <div class="max-w-2xl mx-auto">
      <h1 class="text-2xl font-bold mb-6">Account Settings</h1>
      <AccountEditForm :user="user" />
    </div>
  </div>
</template> 