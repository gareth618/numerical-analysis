<script>
export default {
  props: ['modelValue', 'label', 'min', 'max'],
  emits: ['update:modelValue'],
  data() {
    return {
      number: this.modelValue
    };
  },
  watch: {
    number(newNumber) {
      this.$emit('update:modelValue', Math.min(Math.max(Math.floor(newNumber) || 0, this.min), this.max));
    }
  }
};
</script>

<template>
  <article>
    <label>{{ label }}</label>
    <input v-model="number" type="number" title="" :min="min" :max="max" />
  </article>
</template>
