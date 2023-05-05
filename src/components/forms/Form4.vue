<script>
import Number from '../utils/Number.vue';
import Matrix from '../utils/Matrix.vue';
import RowVector from '../utils/RowVector.vue';
import ColVector from '../utils/ColVector.vue';

const exampleA = [
  [102.5, 0.0, 2.5, 0.0, 0.0],
  [3.5, 104.88, 1.05, 0.0, 0.33],
  [0.0, 0.0, 100.0, 0.0, 0.0],
  [0.0, 1.3, 0.0, 101.3, 0.0],
  [0.73, 0.0, 0.0, 1.5, 102.23]
];

const exampleB = [6, 7, 8, 9, 1];

export default {
  components: {
    Number,
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
    x() {
      return window.python('solve_system(?, ?).tolist()', [this.a, this.b]);
    }
  },
  watch: {
    dimension(newDimension) {
      [this.a, this.b] = window.python('[array.tolist() for array in random_system(?)]', [newDimension]);
    }
  }
};
</script>

<template>
  <main>
    <h1>Tema #4</h1>
    <Number v-model="dimension" label="Dimension" :min="2" :max="8" />
    <div class="matrices">
      <Matrix v-model="a" label="A" :disabled="true" />
      <ColVector v-model="b" label="b" :disabled="true" />
    </div>
    <div class="matrices">
      <RowVector v-model="x" label="x" :disabled="true" v-if="x.length > 0" />
      <p v-else>divergence</p>
    </div>
  </main>
</template>
