<script>
export default {
  props: ['modelValue', 'disabled', 'label'],
  emits: ['update:modelValue'],
  computed: {
    rows() {
      return this.modelValue.length;
    },
    cols() {
      return this.modelValue[0].length;
    }
  },
  methods: {
    *cells() {
      for (let i = 0; i < this.rows; i++) {
        for (let j = 0; j < this.cols; j++) {
          yield [i, j];
        }
      }
    },
    updateMatrix(i, j, value) {
      const matrix = JSON.parse(JSON.stringify(this.modelValue));
      matrix[i][j] = parseInt(value);
      return matrix;
    }
  }
};
</script>

<template>
  <article>
    <label>{{ label }}</label>
    <div class="matrix">
      <input
        v-for="[i, j] in cells()"
        type="number"
        :disabled="disabled"
        :value="modelValue[i][j]"
        @input="$emit('update:modelValue', updateMatrix(i, j, $event.target.value))"
      />
    </div>
  </article>
</template>

<style scoped>
article {
  min-width: 100px;
}

.matrix {
  display: grid;
  gap: .25rem;
  grid-template-columns: repeat(v-bind(cols), 1fr);
}

input {
  width: 2rem;
  height: 2rem;
  text-align: center;
}
</style>
