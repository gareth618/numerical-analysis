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
      polynomialId: 5
    };
  },
  computed: {
    info() {
      return window.python('min_max_points(?)', [this.polynomialId]);
    }
  }
};
</script>

<template>
  <main>
    <h1>Tema #8</h1>
    <ol>
      <li>f(x) = 1/3x^3 - 2x^2 + 2x + 3</li>
      <li>f(x) = x^4 - 6x^3 + 13x^2 - 12x + 4</li>
    </ol>
    <Number v-model="polynomialId" label="Polynomial" :min="1" :max="2" />
    <ul>
      <li>1st method: {{ info[0] }} <template v-if="info[0] !== 6186186181">({{ info[1] == 6186186182 ? 'minimum' : 'maximum' }} point)</template></li>
      <li>2nd method: {{ info[2] }} <template v-if="info[2] !== 6186186181">({{ info[3] == 6186186182 ? 'minimum' : 'maximum' }} point)</template></li>
    </ul>
  </main>
</template>

<style scoped>
.graphs {
  gap: 2rem;
}
</style>
