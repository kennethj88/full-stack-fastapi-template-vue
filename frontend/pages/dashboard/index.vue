<script lang="ts" setup>
  definePageMeta({
    middleware: 'auth' // this should match the name of the file inside the middleware directory 
})

import { useAuthStore } from '~/stores/auth'

const authStore = useAuthStore()
</script>

<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-2xl font-bold mb-6">
      Welcome, {{ authStore.user?.full_name }}!
    </h1>

    <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      <!-- Items Card -->
      <NuxtLink
        to="/dashboard/items"
        class="card bg-base-100 shadow-xl hover:shadow-2xl transition-shadow"
      >
        <div class="card-body">
          <h2 class="card-title">
            <Icon name="material-symbols:inventory-2" class="text-2xl" />
            Items
          </h2>
          <p class="text-gray-600">
            Manage your items - create, view, edit, and delete items in your inventory.
          </p>
          <div class="card-actions justify-end">
            <button class="btn btn-primary btn-sm">
              View Items
            </button>
          </div>
        </div>
      </NuxtLink>

      <!-- Add more dashboard cards here as needed -->
    </div>
  </div>
</template>

