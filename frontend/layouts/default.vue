<template>
  <div class="fixed inset-x-0 top-0 z-[60] border-transparent backdrop-blur-sm transition-all duration-500"
    id="landing_top_bar">
    <div class="container">
      <div role="navigation" aria-label="Navbar" class="navbar px-0">
        <div class="navbar-start gap-2">
          <!-- Mobile Menu Button - Only visible on mobile -->
          <div class="flex-none lg:hidden">
            <div class="drawer drawer-start">
              <input id="side_drawer_toggle" type="checkbox" class="drawer-toggle" />
              <div class="drawer-content">
                <label for="side_drawer_toggle" class="btn btn-square btn-ghost">
                  <Icon icon="lucide:menu" height="20" class="inline-block text-xl" />
                </label>
              </div>
              <div class="drawer-side">
                <label for="side_drawer_toggle" class="drawer-overlay"></label>
                <ul class="menu min-h-full w-80 gap-2 bg-base-100 p-4 text-base-content">
                  <li class="font-medium">
                    <div class="inline">
                      <img alt="logo-dark" loading="lazy" width="86" height="24" class="hidden dark:inline"
                        src="/assets/public/assets/images/logo/logo-dark.svg" />
                      <img alt="logo-light" loading="lazy" width="86" height="24" class="inline dark:hidden"
                        src="/assets/public/assets/images/logo/logo-light.svg" />
                    </div>
                  </li>
                  <li class="font-medium"><NuxtLink to="/">Home</NuxtLink></li>
                  <li class="font-medium"><NuxtLink to="/dashboard">Dashboard</NuxtLink></li>
                  <li class="font-medium"><NuxtLink to="/login">Login</NuxtLink></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Logo -->
          <div class="inline">
            <img alt="logo-dark" loading="lazy" width="86" height="24" class="hidden dark:inline"
              src="/assets/public/assets/images/logo/logo-dark.svg" />
            <img alt="logo-light" loading="lazy" width="86" height="24" class="inline dark:hidden"
              src="/assets/public/assets/images/logo/logo-light.svg" />
          </div>
        </div>

        <div class="navbar-end gap-3">
          <!-- Desktop Navigation Menu -->
          <ul class="menu menu-horizontal menu-sm hidden gap-2 px-1 lg:flex">
            <li class="font-medium"><NuxtLink to="/">Home</NuxtLink></li>
            <li class="font-medium"><NuxtLink to="/dashboard">Dashboard</NuxtLink></li>
            <li class="font-medium"><NuxtLink to="/login">Login</NuxtLink></li>
          </ul>

          <!-- Auth Buttons -->
          <ClientOnly>
            <template #default>
              <template v-if="authStore.initialized">
                <template v-if="authStore.isAuthenticated">
                  <NuxtLink to="/logout" class="btn btn-ghost btn-sm normal-case">
                    logout
                  </NuxtLink>
                  <NuxtLink v-if="authStore.user" to="/dashboard/account" class="btn btn-ghost btn-sm">
                    welcome, {{ authStore.user.full_name }}
                  </NuxtLink>
                </template>
                <NuxtLink v-else to="/login" class="btn btn-primary btn-sm">
                  Login
                </NuxtLink>
              </template>
              <template v-else>
                <div class="h-10 w-32"></div>
              </template>
            </template>
          </ClientOnly>
        </div>
      </div>
    </div>
  </div>

  
  <!-- Main content -->
  <main class="container relative z-10 py-20 xl:py-48">
    <slot />
  </main>

  <!-- Footer -->
  <div>
    <div class="container py-16">
      <div class="mt-12 text-center">
        🌼 Made with
        <a class="link-hover link" target="_blank" href="https://daisyui.com">daisyUI</a>
      </div>
    </div>
  </div>

  <!-- Theme Toggle -->
  <div class="fixed bottom-5 end-5 z-10">
    <button aria-label="Theme toggler" data-action="theme-toggle"
      class="btn btn-circle btn-ghost border border-base-content/10 text-base-content/70 hover:bg-base-content/10">
      <Icon icon="lucide:sun" height="20" class="hidden dark:inline" />
      <Icon icon="lucide:moon" height="20" class="inline dark:hidden" />
    </button>
  </div>
</template>

<script setup lang="ts">
import { Icon } from '@iconify/vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
</script>
