<script setup lang="ts">
import { ref, onMounted } from 'vue'

definePageMeta({
    middleware: 'auth' // this should match the name of the file inside the middleware directory 
})

const authStore = useAuthStore()

import type { Item } from '~/types'
import { itemsApi } from '~/composables/api/items'

const items = ref<Item[]>([])
const totalCount = ref(0)
const isLoading = ref(true)
const showAddModal = ref(false)

// Form data for new item
const newItem = ref({
  title: '',
  description: ''
})

// Load items
const loadItems = async () => {
  try {
    isLoading.value = true
    const response = await itemsApi.getItems()
    items.value = response.data
    totalCount.value = response.count
  } catch (error) {
    console.error('Error loading items:', error)
  } finally {
    isLoading.value = false
  }
}

// Add new item
const handleAddItem = async () => {
  try {
    await itemsApi.createItem({
      title: newItem.value.title,
      description: newItem.value.description
    })
    // Reset form and close modal
    newItem.value = { title: '', description: '' }
    showAddModal.value = false
    // Reload items
    await loadItems()
  } catch (error) {
    console.error('Error creating item:', error)
  }
}

// Delete item
const handleDeleteItem = async (id: string) => {
  try {
    await itemsApi.deleteItem(id)
    await loadItems()
  } catch (error) {
    console.error('Error deleting item:', error)
  }
}

onMounted(() => {
  loadItems()
})
</script>

<template>
  <div class="container mx-auto px-4 py-8">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold">Items</h1>
      <button
        class="btn btn-primary"
        @click="showAddModal = true"
      >
        Add Item
      </button>
    </div>

    <!-- Loading state -->
    <div v-if="isLoading" class="flex justify-center py-8">
      <span class="loading loading-spinner loading-lg"></span>
    </div>

    <!-- Items list -->
    <div v-else-if="items.length > 0" class="grid gap-4">
      <div
        v-for="item in items"
        :key="item.id"
        class="card bg-base-100 shadow-xl"
      >
        <div class="card-body">
          <div class="flex justify-between items-start">
            <div>
              <h2 class="card-title">{{ item.title }}</h2>
              <p v-if="item.description" class="text-gray-600">
                {{ item.description }}
              </p>
            </div>
            <button
              class="btn btn-error btn-sm"
              @click="handleDeleteItem(item.id)"
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty state -->
    <div
      v-else
      class="text-center py-8 text-gray-500"
    >
      No items found. Click the Add Item button to create one.
    </div>

    <!-- Add Item Modal -->
    <dialog
      id="add_item_modal"
      class="modal"
      :open="showAddModal"
    >
      <div class="modal-box">
        <h3 class="font-bold text-lg mb-4">Add New Item</h3>
        <form @submit.prevent="handleAddItem">
          <div class="form-control">
            <label class="label">
              <span class="label-text">Title</span>
            </label>
            <input
              v-model="newItem.title"
              type="text"
              placeholder="Enter title"
              class="input input-bordered"
              required
            />
          </div>
          <div class="form-control mt-4">
            <label class="label">
              <span class="label-text">Description</span>
            </label>
            <textarea
              v-model="newItem.description"
              class="textarea textarea-bordered"
              placeholder="Enter description"
              rows="3"
            />
          </div>
          <div class="modal-action">
            <button
              type="button"
              class="btn"
              @click="showAddModal = false"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="btn btn-primary"
            >
              Add Item
            </button>
          </div>
        </form>
      </div>
      <div class="modal-backdrop">
        <button @click="showAddModal = false">close</button>
      </div>
    </dialog>
  </div>
</template> 