<script>
import Matrix from './Matrix.vue';

export default {
  props: ['modelValue', 'label', 'disabled'],
  emits: ['update:modelValue'],
  components: {
    Matrix
  },
  computed: {
    matrix: {
      get() {
        return [this.modelValue];
      },
      set(matrix) {
        this.$emit('update:modelValue', matrix[0]);
      }
    }
  }
};
</script>

<template>
  <Matrix v-model="matrix" :label="label" :disabled="disabled" />
</template>
