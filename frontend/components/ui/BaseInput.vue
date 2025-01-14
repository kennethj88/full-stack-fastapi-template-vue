<script setup lang="ts">
const props = defineProps<{
  modelValue: string
  labelTxt?: string
  iconifyIcon?: string
  type?: string
  id?: string
  required?: boolean
  placeholder?: string
  autocomplete?: string
  class?: string
  error?: string
}>()

import { Icon } from '@iconify/vue'
import { computed, ref } from 'vue'

const emit = defineEmits<{
  'update:modelValue': [value: string]
}>()

// Add ref for password visibility
const isPasswordVisible = ref(false)

// Toggle password visibility
const togglePasswordVisibility = () => {
  isPasswordVisible.value = !isPasswordVisible.value
}

// Compute the input type based on password visibility
const inputType = computed(() => 
  props.type === 'password' && isPasswordVisible.value ? 'text' : props.type || 'text'
)

// Add computed property for wrapper class
const wrapperClass = computed(() => 
  props.iconifyIcon 
    ? 'flex flex-row items-center rounded-box border border-base-content/20 ps-3 pe-3'
    : 'form-control'
)
</script>

<template>
  <div class="form-control">
    <label v-if="labelTxt" :for="id" class="label">
      <span class="label-text cursor-pointer">{{labelTxt}}</span>
    </label>

    <div :class="wrapperClass">
      <Icon v-if="iconifyIcon"
          :icon="iconifyIcon"
          height="18"
          class="text-base-content/80"></Icon>
      <input
        :value="modelValue"
        @input="emit('update:modelValue', ($event.target as HTMLInputElement).value)"
        :type="inputType"
        :id="id"
        :required="required"
        :placeholder="placeholder"
        :autocomplete="autocomplete"
        class="input input-sm w-full transition-all focus:border-transparent focus:outline-0 focus:outline-offset-0"
        :class="class" />

      <button v-if="type === 'password'"
          @click="togglePasswordVisibility"
          type="button"
          :data-slot-value="isPasswordVisible ? 'show' : 'hide'"
          data-slot="visibility-toggle"
          aria-label="Show/Hide password"
          class="group btn btn-circle btn-ghost btn-xs hover:bg-base-content/10">
          <Icon
              icon="lucide:eye"
              height="16"
              class="inline text-base-content/80 group-data-[slot-value=show]:hidden"></Icon>
          <Icon
              icon="lucide:eye-off"
              height="16"
              class="inline text-base-content/80 group-data-[slot-value=hide]:hidden"></Icon>
      </button>

      <label v-if="error" class="label">
        <span class="label-text-alt text-error">{{ error }}</span>
      </label>
    </div>
  </div>
</template> 