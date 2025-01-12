<template>
  <div class="flex min-h-screen">
    <!-- Sidebar -->
    <div class="leftmenu-wrapper">
      <NuxtLink to="/dashboard" class="flex h-16 items-center justify-center">
        <!-- Logo -->
        <div class="inline">
          <img
            alt="logo-dark"
            loading="lazy"
            class="hidden h-6 dark:inline"
            src="/assets/public/assets/images/logo/logo-dark.png"
          />
          <img
            alt="logo-light"
            loading="lazy"
            class="inline h-6 dark:hidden"
            src="/assets/public/assets/images/logo/logo-light.png"
          />
        </div>
      </NuxtLink>
      
      <!-- Navigation Menu -->
      <nav class="menu mb-6">
        <ul>
          <li class="mb-0.5">
            <NuxtLink 
              to="/dashboard" 
              class="flex items-center gap-2 p-3 hover:bg-base-content/15"
            >
              <Icon name="lucide:airplay" size="18" />
              Dashboard
            </NuxtLink>
          </li>
          <li class="mb-0.5">
            <NuxtLink 
              to="/dashboard/items" 
              class="flex items-center gap-2 p-3 hover:bg-base-content/15"
            >
              <Icon name="material-symbols:inventory-2" size="18" />
              Items
            </NuxtLink>
          </li>
        </ul>
      </nav>
    </div>

    <!-- Main Content -->
    <div class="main-wrapper flex-1 overflow-auto">
      <div class="flex h-full flex-col">
        <!-- Top Bar -->
        <div class="navbar bg-base-100 px-4 shadow-sm">
          <div class="flex-1">
            <h1 class="text-xl font-semibold">Dashboard</h1>
          </div>
          <div class="flex-none gap-2">
            <button 
              class="btn btn-ghost btn-circle"
              @click="toggleTheme"
            >
              <Icon name="lucide:sun" v-if="isDarkMode" />
              <Icon name="lucide:moon" v-else />
            </button>
          </div>
          
          <template v-if="authStore.initialized">
            <div class="flex-none gap-2">
            
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
        </div>

        <!-- Page Content -->
        <div class="content-wrapper p-6">
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'

const isDarkMode = ref(false)
//
const authStore = useAuthStore()

console.log('layout initialized',authStore.initialized)


const toggleTheme = () => {
  isDarkMode.value = !isDarkMode.value
  document.documentElement.classList.toggle('dark')
}
</script>

<style scoped>
.leftmenu-wrapper {
  @apply w-64 bg-base-100 border-r border-base-content/10;
}

.main-wrapper {
  @apply flex-1;
}
</style>
