<script>
import Dimension from '../utils/Dimension.vue';
import Matrix from '../utils/Matrix.vue';
import RowVector from '../utils/RowVector.vue';
import ColVector from '../utils/ColVector.vue';

const exampleA = [
  [1, 2.5, 3],
  [2.5, 8.25, 15.5],
  [3, 15.5, 43]
];
const exampleB = [12, 38, 68];

export default {
  components: {
    Dimension,
    Matrix,
    RowVector,
    ColVector
  },
  data() {
    return {
      dimension: 3,
      a: exampleA,
      b: exampleB
    };
  },
  computed: {
    isDiagonalDominant() {
      let isExample = true;
      if (JSON.stringify(this.a) !== JSON.stringify(exampleA)) isExample = false;
      if (JSON.stringify(this.b) !== JSON.stringify(exampleB)) isExample = false;
      return isExample || window.python('is_diagonal_dominant(?)', [this.a]);
    },
    xChol() {
      return window.python('cholesky(?, ?).tolist()', [this.a, this.b]);
    },
    xPLU() {
      return window.python('plu(?, ?).tolist()', [this.a, this.b]);
    }
  },
  watch: {
    dimension(newDimension) {
      [this.a, this.b] = window.python('[array.tolist() for array in generate(?)]', [newDimension]);
    },
    a(newA, oldA) {
      if (newA.length !== oldA.length) return;
      for (let i = 0; i < this.dimension; i++) {
        for (let j = 0; j < this.dimension; j++) {
          if (newA[i][j] !== oldA[i][j]) {
            newA[j][i] = newA[i][j];
          }
        }
      }
    }
  }
};
</script>

<template>
  <main>
    <h1>Tema #2</h1>
    <Dimension v-model="dimension" label="Dimension" :min="2" :max="8" />
    <div class="matrices">
      <Matrix v-model="a" label="A" />
      <ColVector v-model="b" label="b" />
    </div>
    <div class="matrices">
      <RowVector v-if="isDiagonalDominant && xChol != null" v-model="xChol" label="Cholesky" :disabled="true" />
      <RowVector v-if="isDiagonalDominant && xPLU != null" v-model="xPLU" label="PLU" :disabled="true" />
      <p v-if="isDiagonalDominant === false">A is not diagonal dominant</p>
      <p v-if="isDiagonalDominant == null">waiting for you to fill the cells</p>
    </div>
  </main>
</template>
