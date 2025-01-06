<template>
  <div>
    <nav class="navbar bg-base-100">
      <div class="flex-1">
        <NuxtLink to="/" class="btn btn-ghost normal-case text-xl">
          Your App
        </NuxtLink>
      </div>
      
      <!-- User info section -->
      <ClientOnly>
        <template v-if="authStore.initialized">
          <div class="flex items-center gap-4">
            <!-- Show logout only if authenticated -->
            <NuxtLink 
              v-if="authStore.isAuthenticated" 
              to="/logout" 
              class="btn btn-ghost normal-case"
            >
              logout
            </NuxtLink>

            <!-- User account link -->
            <NuxtLink 
              v-if="authStore.user"
              to="/dashboard/account" 
              class="btn btn-ghost"
            >
              welcome, {{ authStore.user.full_name }}
            </NuxtLink>
          </div>
        </template>
        <!-- Loading placeholder -->
        <template v-else>
          <div class="h-10 w-32"></div>
        </template>
      </ClientOnly>
    </nav>

    <!-- Main content -->
    <main>
      <slot />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
//console.log('layout hydrated',authStore.hydrated)
console.log('layout authstore user', authStore.user)
</script>