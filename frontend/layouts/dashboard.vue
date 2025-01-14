<template>
  <div class="drawer lg:drawer-open">
    <!-- Drawer toggle for mobile -->
    <input id="main-drawer" type="checkbox" class="drawer-toggle" />
    
    <!-- Page content -->
    <div class="drawer-content flex flex-col bg-[--main-content-background]">
      <!-- Navbar -->
      <div class="navbar bg-[--topbar-background] px-4 border-b border-base-content/10">
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
            <Icon 
              :name="isDarkMode ? 'lucide:sun' : 'lucide:moon'" 
              size="24"
            />
          </button>
          <!-- Notifications Dropdown -->
          <div class="dropdown dropdown-end">
            <label tabindex="0" class="btn btn-ghost btn-circle">
              <div class="indicator">
                <Icon name="lucide:bell" size="24" />
                <span class="badge badge-sm indicator-item badge-primary">3</span>
              </div>
            </label>
            <ul tabindex="0" class="mt-4 z-[1] card card-compact dropdown-content w-80 bg-base-100 shadow">
              <div class="card-body">
                <div class="flex items-center justify-between mb-2">
                  <span class="text-lg font-bold">Notifications</span>
                  <span class="text-info text-sm">Mark all as read</span>
                </div>
                <!-- Notification Items -->
                <ul class="space-y-3">
                  <li class="flex gap-4 items-start">
                    <div class="avatar">
                      <div class="w-10 h-10 rounded-full">
                        <img src="/assets/public/assets/images/avatars/1.png" alt="avatar" />
                      </div>
                    </div>
                    <div class="flex-1">
                      <p class="text-sm"><span class="font-medium">James Smith</span> commented on your post</p>
                      <span class="text-xs text-base-content/60">2 hours ago</span>
                    </div>
                    <div class="w-2 h-2 bg-primary rounded-full"></div>
                  </li>
                  <li class="flex gap-4 items-start">
                    <div class="avatar">
                      <div class="w-10 h-10 rounded-full">
                        <img src="/assets/public/assets/images/avatars/2.png" alt="avatar" />
                      </div>
                    </div>
                    <div class="flex-1">
                      <p class="text-sm"><span class="font-medium">Sarah Johnson</span> mentioned you in a comment</p>
                      <span class="text-xs text-base-content/60">5 hours ago</span>
                    </div>
                  </li>
                  <li class="flex gap-4 items-start">
                    <div class="avatar">
                      <div class="w-10 h-10 rounded-full">
                        <img src="/assets/public/assets/images/avatars/3.png" alt="avatar" />
                      </div>
                    </div>
                    <div class="flex-1">
                      <p class="text-sm"><span class="font-medium">Michael Brown</span> liked your post</p>
                      <span class="text-xs text-base-content/60">10 hours ago</span>
                    </div>
                  </li>
                </ul>
              </div>
            </ul>
          </div>
        </div>
        
        <template v-if="authStore.initialized">
          <div class="dropdown dropdown-end dropdown-bottom">
            <label tabindex="0" class="btn btn-ghost rounded-btn px-1.5 hover:bg-base-content/20">
              <div class="flex items-center gap-2">
                <div class="avatar">
                  <div class="mask mask-squircle w-[30px] h-[30px]">
                    <img src="/assets/public/assets/images/avatars/1.png" alt="Avatar" />
                  </div>
                </div>
                <div class="flex flex-col items-start">
                  <p class="text-sm/none">{{ authStore.user?.full_name || 'Deep' }}</p>
                  <p class="mt-1 text-xs/none text-primary">Edit</p>
                </div>
              </div>
            </label>
            <ul tabindex="0" class="menu dropdown-content mt-4 w-52 rounded-box bg-base-100 p-2 shadow">
              <li>
                <NuxtLink to="/dashboard/account/">
                  <Icon name="lucide:user" size="16" />
                  My Profile
                </NuxtLink>
              </li>
              <li>
                <NuxtLink to="/dashboard/">
                  <Icon name="lucide:bell" size="16" />
                  Notifications
                </NuxtLink>
              </li>
              <hr class="-mx-2 my-1 border-base-content/10" />
              <li>
                <NuxtLink to="/logout" class="text-error">
                  <Icon name="lucide:log-out" size="16" />
                  Logout
                </NuxtLink>
              </li>
            </ul>
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
                    <NuxtLink to="/dashboard/" class="hover:bg-base-content/15">
                      <div class="flex items-center gap-2">Orders</div>
                    </NuxtLink>
                  </li>
                  <li class="mb-0.5">
                    <NuxtLink to="/dashboard/items" class="hover:bg-base-content/15">
                      <div class="flex items-center gap-2">Products</div>
                    </NuxtLink>
                  </li>
                  <li class="mb-0.5">
                    <NuxtLink to="/dashboard/" class="hover:bg-base-content/15">
                      <div class="flex items-center gap-2">Customers</div>
                    </NuxtLink>
                  </li>
                </ul>
              </details>
            </li>
            <li class="mb-0.5">
              <NuxtLink to="/dashboard/" class="hover:bg-base-content/15">
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
                    <NuxtLink to="/dashboard/account/" class="hover:bg-base-content/15">
                      <div class="flex items-center gap-2">General</div>
                    </NuxtLink>
                  </li>
                  <li class="mb-0.5">
                    <NuxtLink to="/dashboard/account/" class="hover:bg-base-content/15">
                      <div class="flex items-center gap-2">Profile</div>
                    </NuxtLink>
                  </li>
                  <li class="mb-0.5">
                    <NuxtLink to="/dashboard/" class="hover:bg-base-content/15">
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
            <NuxtLink to="/">
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
  @apply w-64 bg-[--leftmenu-background] border-r border-base-content/10;
}

.main-wrapper {
  @apply flex-1;
}
</style>
