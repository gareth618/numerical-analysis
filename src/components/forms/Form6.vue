<script>
import Number from '../utils/Number.vue';
import Matrix from '../utils/Matrix.vue';
import RowVector from '../utils/RowVector.vue';
import ColVector from '../utils/ColVector.vue';
import Graph from '../utils/Graph.vue';

export default {
  components: {
    Number,
    Matrix,
    RowVector,
    ColVector,
    Graph
  },
  data() {
    return {
      polynomialId: 1,
      pointCount: 5
    };
  },
  computed: {
    points() {
      return window.python('interpolate(?, ?)', [this.polynomialId - 1, this.pointCount]);
    }
  }
};
</script>

<template>
  <main>
    <h1>Tema #6</h1>
    <ol>
      <li>f(x) = x^2 - 12x + 30</li>
      <li>f(x) = sin(x) - cos(x)</li>
      <li>f(x) = 2x^3 - 3x + 15</li>
    </ol>
    <div class="matrices">
      <Number v-model="polynomialId" label="Polynomial" :min="1" :max="3" />
      <Number v-model="pointCount" label="Points" :min="2" :max="100" />
    </div>
    <div class="matrices graphs">
      <Graph label="function" :dimension="20" :points="points[0].map((x, i) => [x, points[1][i]])" />
      <Graph label="Lagrange" :dimension="20" :points="points[2].map((x, i) => [x, points[3][i]])" />
      <Graph label="Least Squares" :dimension="20" :points="points[4].map((x, i) => [x, points[5][i]])" />
    </div>
  </main>
</template>

<style scoped>
.graphs {
  gap: 2rem;
}
</style>
