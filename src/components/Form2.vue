<script>
import Matrix from './Matrix.vue';

export default {
  components: {
    Matrix
  },
  data() {
    return {
      inputDimension: 3,
      a: [
        [1, 2.5, 3],
        [2.5, 8.25, 15.5],
        [3, 15.5, 43]
      ],
      b: [[12], [38], [68]]
    };
  },
  computed: {
    dimension() {
      return Math.min(Math.max(this.inputDimension || 0, 2), 8);
    },
    xChol() {
      return this.solution((a, b) => `cholesky(${a}, ${b}).tolist()`)
    },
    xPLU() {
      return this.solution((a, b) => `plu(${a}, ${b}).tolist()`)
    }
  },
  methods: {
    hasEmptyCells(matrix) {
      for (const row of matrix) {
        for (const cell of row) {
          if (isNaN(cell)) return true;
        }
      }
      return false;
    },
    solution(solve) {
      if (this.hasEmptyCells(this.a)) return;
      if (this.hasEmptyCells(this.b)) return;
      const a = `np.array(${JSON.stringify(this.a)})`;
      const b = `np.array(${JSON.stringify(this.b.map(([value]) => value))})`;
      return [JSON.parse(window.python(solve(a, b)))];
    }
  },
  watch: {
    dimension(newDimension) {
      [this.a, this.b] = JSON.parse(window.python(`[array.tolist() for array in generate(${newDimension})]`));
      this.b = this.b.map(value => [value]);
    },
    a(newA, oldA) {
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
    <article>
      <label>Dimension</label>
      <input
        v-model="inputDimension"
        type="number" min="2" max="8"
      />
    </article>
    <div class="matrices">
      <Matrix v-model="a" label="A" />
      <Matrix v-model="b" label="b" />
    </div>
    <div class="matrices">
      <Matrix v-if="xChol != null" v-model="xChol" label="Cholesky" :disabled="true" />
      <Matrix v-if="xPLU != null" v-model="xPLU" label="PLU" :disabled="true" />
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

.matrices {
  display: flex;
  gap: 3.75rem;
}

.matrices:deep(input) {
  font-size: .75rem;
}
</style>
