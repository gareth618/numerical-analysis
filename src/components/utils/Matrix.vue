<script>
export default {
  props: ['modelValue', 'label', 'disabled'],
  emits: ['update:modelValue'],
  data() {
    return {
      matrix: JSON.parse(JSON.stringify(this.modelValue))
    };
  },
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
      matrix[i][j] = parseFloat(value);
      return matrix;
    }
  },
  watch: {
    modelValue(newModelValue) {
      for (const row of newModelValue) {
        for (const cell of row) {
          if (isNaN(cell)) return;
        }
      }
      this.matrix = JSON.parse(JSON.stringify(newModelValue));
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
        title=""
        :class="{ wrong: isNaN(parseFloat(matrix[i][j])) }"
        :disabled="disabled"
        v-model="matrix[i][j]"
        @input="$emit('update:modelValue', updateMatrix(i, j, $event.target.value))"
      />
    </div>
  </article>
</template>

<style scoped>
.matrix {
  display: grid;
  gap: .25rem;
  grid-template-columns: repeat(v-bind(cols), 1fr);
}

.wrong {
  outline-color: var(--red);
}
</style>
