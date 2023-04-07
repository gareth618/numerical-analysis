<script>
import Number from '../utils/Number.vue';
import Matrix from '../utils/Matrix.vue';
import RowVector from '../utils/RowVector.vue';
import ColVector from '../utils/ColVector.vue';

const exampleA = [
  [0, 0, 4],
  [1, 2, 3],
  [0, 1, 2]
];
const exampleS = [3, 2, 1];

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
      s: exampleS
    };
  },
  computed: {
    b() {
      return window.python('(? @ ?).tolist()', [this.a, this.s]);
    },
    xHH() {
      return window.python('solve_system(*householder(?, ?), ?).tolist()', [this.a, this.b, this.b]);
    },
    xQR() {
      return window.python('solve_system(*np.linalg.qr(?), ?).tolist()', [this.a, this.b]);
    },
    invHH() {
      return window.python('inverse(*householder(?)).tolist()', [this.a]);
    },
    invNP() {
      return window.python('np.linalg.inv(?).tolist()', [this.a]);
    }
  },
  watch: {
    dimension(newDimension) {
      const [a, _, s] = window.python('[array.tolist() for array in random_system(?)]', [newDimension]);
      this.a = a;
      this.s = s;
    }
  }
};
</script>

<template>
  <main>
    <h1>Tema #3</h1>
    <Number v-model="dimension" label="Dimension" :min="2" :max="8" />
    <div class="matrices">
      <Matrix v-model="a" label="A" />
      <ColVector v-model="s" label="s" />
      <ColVector v-if="b != null" v-model="b" label="b" :disabled="true" />
    </div>
    <div class="matrices">
      <RowVector v-if="xHH != null" v-model="xHH" label="xHH" :disabled="true" />
      <RowVector v-if="xQR != null" v-model="xQR" label="xQR" :disabled="true" />
      <p v-else>waiting for you to fill the cells</p>
    </div>
    <div class="matrices">
      <Matrix v-if="invHH != null" v-model="invHH" label="HH inverse" :disabled="true" />
      <Matrix v-if="invNP != null" v-model="invNP" label="NP inverse" :disabled="true" />
    </div>
  </main>
</template>
