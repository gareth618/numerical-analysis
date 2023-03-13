<script>
export default {
  props: ['modelValue', 'label', 'min', 'max'],
  emits: ['update:modelValue'],
  data() {
    return {
      dimension: this.modelValue
    };
  },
  watch: {
    dimension(newDimension) {
      this.$emit('update:modelValue', Math.min(Math.max(Math.floor(newDimension) || 0, this.min), this.max));
    }
  }
};
</script>

<template>
  <article>
    <label>{{ label }}</label>
    <input v-model="dimension" type="number" title="" :min="min" :max="max" />
  </article>
</template>
