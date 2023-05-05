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
      degree: 5
    };
  },
  computed: {
    info() {
      return window.python('find_roots(?)', [this.degree]);
    }
  }
};
</script>

<template>
  <main>
    <h1>Tema #7</h1>
    <Number v-model="degree" label="Degree" :min="2" :max="10" />
    <RowVector v-model="info[0]" label="P" :disabled="true" />
    <Matrix v-model="info[1]" label="Roots" :disabled="true" />
  </main>
</template>

<style scoped>
.graphs {
  gap: 2rem;
}
</style>
