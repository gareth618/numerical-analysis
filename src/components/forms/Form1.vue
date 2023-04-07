<script>
import Number from '../utils/Number.vue';
import Matrix from '../utils/Matrix.vue';

export default {
  components: {
    Number,
    Matrix
  },
  data() {
    return {
      dimension: 4,
      matrix1: this.createSquareMatrix(4),
      matrix2: this.createSquareMatrix(4)
    };
  },
  computed: {
    productStrassen() {
      return window.python('strassen(?, ?, 2).tolist()', [this.matrix1, this.matrix2]);
    },
    productNumpy() {
      return window.python('(? @ ?).tolist()', [this.matrix1, this.matrix2]);
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
    <Number v-model="dimension" label="Dimension" :min="2" :max="8" />
    <div class="matrices">
      <Matrix v-model="matrix1" label="Matrix #1" />
      <Matrix v-model="matrix2" label="Matrix #2" />
    </div>
    <div class="matrices">
      <Matrix v-if="productStrassen != null" v-model="productStrassen" label="Strassen" :disabled="true" />
      <Matrix v-if="productNumpy != null" v-model="productNumpy" label="NumPy" :disabled="true" />
      <p v-else>waiting for you to fill the cells</p>
    </div>
  </main>
</template>
