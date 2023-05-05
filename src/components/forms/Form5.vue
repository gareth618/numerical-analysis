<script>
import Number from '../utils/Number.vue';
import Matrix from '../utils/Matrix.vue';
import RowVector from '../utils/RowVector.vue';
import ColVector from '../utils/ColVector.vue';

export default {
  components: {
    Number,
    Matrix,
    RowVector,
    ColVector
  },
  data() {
    return {
      d: 3,
      m: 4,
      n: 3
    };
  },
  computed: {
    info1() {
      return window.python('first_task(?)', [this.d]);
    },
    info2() {
      return window.python('second_task(?, ?)', [Math.max(this.m, this.n), Math.min(this.m, this.n)]);
    }
  }
};
</script>

<template>
  <main>
    <h1>Tema #5</h1>
    <Number v-model="d" label="Dimension" :min="2" :max="8" />
    <Matrix v-model="info1[0]" label="A" :disabled="true" />
    <p>lambda: {{ info1[1] }}</p>
    <div class="matrices">
      <Number v-model="m" label="Rows" :min="2" :max="8" />
      <Number v-model="n" label="Cols" :min="2" :max="8" />
    </div>
    <Matrix v-model="info2[0]" label="A" :disabled="true" />
    <RowVector v-model="info2[1]" label="Singular values" :disabled="true" />
    <p>Rank: {{ info2[2] }}</p>
    <p>Condition number: {{ info2[3] }}</p>
    <Matrix v-model="info2[4]" label="Moore-Penrose pseudoinverse" :disabled="true" />
    <RowVector v-model="info2[5]" label="x" :disabled="true" />
    <p>norm(b - ax): {{ info2[6] }}</p>
    <p>norm(aj - ai): {{ info2[7] }}</p>
  </main>
</template>
