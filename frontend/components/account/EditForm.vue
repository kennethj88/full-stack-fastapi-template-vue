<script setup lang="ts">
import { ref } from 'vue'
import type { User } from '@/types'
import { authApi } from '@/composables/api/auth'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const props = defineProps<{
  user: User | null
}>()

const isLoading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const form = ref({
  full_name: props.user?.full_name || '',
  email: props.user?.email || ''
})

const updateProfile = async () => {
  try {
    isLoading.value = true
    errorMessage.value = ''
    successMessage.value = ''

    await authApi.updateProfile({
      full_name: form.value.full_name,
      email: form.value.email
    })

    authStore.refreshUser()
    
    successMessage.value = 'Profile updated successfully'
  } catch (error: any) {
    errorMessage.value = error.response?.data?.detail || 'An error occurred while updating profile'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <form @submit.prevent="updateProfile" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
    <!-- Success Message -->
    <div v-if="successMessage" class="mb-4 p-4 bg-green-100 text-green-700 rounded">
      {{ successMessage }}
    </div>

    <!-- Error Message -->
    <div v-if="errorMessage" class="mb-4 p-4 bg-red-100 text-red-700 rounded">
      {{ errorMessage }}
    </div>

    <!-- Full Name Field -->
    <div class="mb-4">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="full_name">
        Full Name
      </label>
      <input
        id="full_name"
        v-model="form.full_name"
        type="text"
        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        placeholder="Enter your full name"
      >
    </div>

    <!-- Email Field -->
    <div class="mb-6">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
        Email
      </label>
      <input
        id="email"
        v-model="form.email"
        type="email"
        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        placeholder="Enter your email"
      >
    </div>

    <!-- Submit Button -->
    <div class="flex items-center justify-between">
      <button
        type="submit"
        :disabled="isLoading"
        class="btn btn-primary w-full"
        :class="{ 'opacity-50 cursor-not-allowed': isLoading }"
      >
        {{ isLoading ? 'Updating...' : 'Update Profile' }}
      </button>
    </div>
  </form>
</template> 