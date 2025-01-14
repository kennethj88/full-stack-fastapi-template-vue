<template>
  <div class="drawer lg:drawer-open">
    <!-- Drawer toggle for mobile -->
    <input id="main-drawer" type="checkbox" class="drawer-toggle" />
    
    <!-- Page content -->
    <div class="drawer-content flex flex-col">
      <!-- Navbar -->
      <div class="navbar bg-base-100 px-4 shadow-sm">
        <div class="flex-none lg:hidden">
          <label for="main-drawer" class="btn btn-square btn-ghost drawer-button">
            <Icon name="lucide:menu" size="24" />
          </label>
        </div>
        <div class="flex-1">
          <h1 class="text-xl font-semibold">Dashboard</h1>
        </div>
        <div class="flex-none gap-2">
          <button class="btn btn-ghost btn-circle" @click="toggleTheme">
            <Icon name="lucide:sun" v-if="isDarkMode" />
            <Icon name="lucide:moon" v-else />
          </button>
        </div>
        
        <template v-if="authStore.initialized">
          <div class="flex-none gap-2">
            <NuxtLink v-if="authStore.isAuthenticated" to="/logout" class="btn btn-ghost normal-case">
              logout
            </NuxtLink>
            <NuxtLink v-if="authStore.user" to="/dashboard/account" class="btn btn-ghost">
              welcome, {{ authStore.user.full_name }}
            </NuxtLink>
          </div>
        </template>
      </div>

      <!-- Main content -->
      <div class="content-wrapper p-6">
        <slot />
      </div>
    </div>

    <!-- Drawer sidebar -->
    <div class="drawer-side">
      <label for="main-drawer" class="drawer-overlay"></label>
      <div class="leftmenu-wrapper">
        <NuxtLink to="/dashboard" class="flex h-16 items-center justify-center">
          <!-- Logo section -->
          <div class="inline">
            <img alt="logo-dark" loading="lazy" class="hidden h-6 dark:inline" src="/assets/public/assets/images/logo/logo-dark.png" />
            <img alt="logo-light" loading="lazy" class="inline h-6 dark:hidden" src="/assets/public/assets/images/logo/logo-light.png" />
          </div>
        </NuxtLink>

        <div class="h-[calc(100vh-64px)] lg:h-[calc(100vh-230px)]">
          <ul class="menu mb-6">
            <!-- Dashboard -->
            <li class="mb-0.5">
              <NuxtLink to="/dashboard" class="hover:bg-base-content/15">
                <div class="flex items-center gap-2">
                  <Icon name="lucide:airplay" size="20" />
                  Dashboard
                </div>
              </NuxtLink>
            </li>

            <!-- Apps -->
            <li class="menu-title font-semibold">Apps</li>
            <li class="mb-0.5">
              <details>
                <summary>
                  <div class="flex items-center gap-2">
                    <Icon name="lucide:store" size="18" />
                    E-Commerce
                  </div>
                </summary>
                <ul>
                  <li class="mb-0.5">
                    <NuxtLink to="/dashboard/orders" class="hover:bg-base-content/15">
                      <div class="flex items-center gap-2">Orders</div>
                    </NuxtLink>
                  </li>
                  <li class="mb-0.5">
                    <NuxtLink to="/dashboard/items" class="hover:bg-base-content/15">
                      <div class="flex items-center gap-2">Products</div>
                    </NuxtLink>
                  </li>
                  <li class="mb-0.5">
                    <NuxtLink to="/dashboard/customers" class="hover:bg-base-content/15">
                      <div class="flex items-center gap-2">Customers</div>
                    </NuxtLink>
                  </li>
                </ul>
              </details>
            </li>
            <li class="mb-0.5">
              <NuxtLink to="/dashboard/chat" class="hover:bg-base-content/15">
                <div class="flex items-center gap-2">
                  <Icon name="lucide:messages-square" size="18" />
                  Chat
                </div>
              </NuxtLink>
            </li>

            <!-- Management -->
            <li class="menu-title font-semibold">Management</li>
            <li class="mb-0.5">
              <details>
                <summary>
                  <div class="flex items-center gap-2">
                    <Icon name="lucide:settings" size="18" />
                    Settings
                  </div>
                </summary>
                <ul>
                  <li class="mb-0.5">
                    <NuxtLink to="/dashboard/settings" class="hover:bg-base-content/15">
                      <div class="flex items-center gap-2">General</div>
                    </NuxtLink>
                  </li>
                  <li class="mb-0.5">
                    <NuxtLink to="/dashboard/profile" class="hover:bg-base-content/15">
                      <div class="flex items-center gap-2">Profile</div>
                    </NuxtLink>
                  </li>
                  <li class="mb-0.5">
                    <NuxtLink to="/dashboard/permissions" class="hover:bg-base-content/15">
                      <div class="flex items-center gap-2">Permissions</div>
                    </NuxtLink>
                  </li>
                </ul>
              </details>
            </li>
          </ul>
        </div>

        <!-- Premium Note -->
        <div class="mx-4 hidden rounded bg-base-200 px-3 py-4 lg:block">
          <p class="text-center text-base font-medium">Need Help?</p>
          <p class="mt-3 text-center text-sm">Contact support for assistance</p>
          <div class="mt-3 text-center">
            <NuxtLink to="/dashboard/support">
              <button class="btn btn-primary btn-sm">Support</button>
            </NuxtLink>
          </div>
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
