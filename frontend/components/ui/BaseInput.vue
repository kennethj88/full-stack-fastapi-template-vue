<script setup lang="ts">
defineProps<{
  modelValue: string
  type?: string
  id?: string
  required?: boolean
  placeholder?: string
  autocomplete?: string
  class?: string
  error?: string
}>()

import { defineEmits } from "vue";


const emit = defineEmits<{
  'update:modelValue': [value: string]
}>()
</script>

<template>
  <div class="form-control w-full">
    <input
      :value="modelValue"
      @input="emit('update:modelValue', ($event.target as HTMLInputElement).value)"
      :type="type || 'text'"
      :id="id"
      :required="required"
      :placeholder="placeholder"
      :autocomplete="autocomplete"
       class="input input-bordered focus:outline-offset-0"
       :class="class" />
    <label v-if="error" class="label">
      <span class="label-text-alt text-error">{{ error }}</span>
    </label>
  </div>
</template> 