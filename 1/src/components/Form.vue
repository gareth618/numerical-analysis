<script>
import Matrix from './Matrix.vue';

export default {
  components: {
    Matrix
  },
  data() {
    return {
      inputDimension: 4,
      matrix1: this.createSquareMatrix(4),
      matrix2: this.createSquareMatrix(4)
    };
  },
  computed: {
    dimension() {
      return Math.min(Math.max(this.inputDimension || 0, 2), 8);
    },
    product() {
      if (this.hasEmptyCells(this.matrix1)) return;
      if (this.hasEmptyCells(this.matrix2)) return;
      const pyMatrix1 = `np.array(${JSON.stringify(this.matrix1)})`;
      const pyMatrix2 = `np.array(${JSON.stringify(this.matrix2)})`;
      return JSON.parse(window.python(`strassen(${pyMatrix1}, ${pyMatrix2}, 2).tolist()`));
    }
  },
  methods: {
    createSquareMatrix(dimension) {
      const matrix = [];
      for (let i = 0; i < dimension; i++) {
        matrix.push([]);
        for (let j = 0; j < dimension; j++) {
          matrix[i].push(Math.floor(Math.random() * 10));
        }
      }
      return matrix;
    },
    hasEmptyCells(matrix) {
      for (const row of matrix) {
        for (const cell of row) {
          if (isNaN(cell)) return true;
        }
      }
      return false;
    }
  },
  watch: {
    dimension(newDimension) {
      this.matrix1 = this.createSquareMatrix(newDimension);
      this.matrix2 = this.createSquareMatrix(newDimension);
    }
  }
};
</script>

<template>
  <main>
    <h1>Tema #1</h1>
    <input
      v-model="inputDimension"
      class="arrows dimension"
      type="number" min="2" max="8"
    />
    <div class="matrices">
      <Matrix v-model="matrix1" />
      <Matrix v-model="matrix2" />
    </div>
    <div class="matrices">
      <Matrix v-if="product != null" v-model="product" :disabled="true" />
      <p v-else>waiting for you to fill the cells</p>
    </div>
  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

h1 {
  margin-bottom: 2rem;
  font-size: 3rem;
  color: var(--green);
  text-decoration: .1em dashed underline;
  text-underline-offset: .25em;
}

.dimension {
  width: 7rem;
  text-align: center;
}

.matrices {
  display: flex;
  gap: 3rem;
}

.matrices:deep(input) {
  font-size: .75rem;
}
</style>
