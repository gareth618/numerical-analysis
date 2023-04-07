<script>
import Form1 from './components/forms/Form1.vue';
import Form2 from './components/forms/Form2.vue';
import Form3 from './components/forms/Form3.vue';
import Form6 from './components/forms/Form6.vue';

export default {
  components: {
    Form1,
    Form2,
    Form3,
    Form6
  },
  data() {
    return {
      runner: null,
      codes: [],
      ready: false,
      currentForm: 0,
      forms: [1, 2, 3, 6],
      modules: ['numpy', 'scipy']
    };
  },
  mounted() {
    const load = async () => {
      this.runner = await loadPyodide();
      const results = await Promise.all(this.forms.map(file => fetch(`/python/${file}.py`)));
      this.codes = await Promise.all(results.map(result => result.text()));
      await Promise.all(this.modules.map(module => this.runner.loadPackage(module)));
      this.runner.runPython(this.codes[0]);

      const hasEmptyCells = array => {
        if (Array.isArray(array)) {
          for (const subarray of array) {
            if (hasEmptyCells(subarray)) return true;
          }
          return false;
        }
        return array == null || (typeof array === 'number' && isNaN(array));
      };

      window.python = (code, args) => {
        for (const arg of args) {
          if (hasEmptyCells(arg)) return;
          code = code.replace('?', Array.isArray(arg) ? `np.array(${JSON.stringify(arg)})` : arg);
        }
        return JSON.parse(this.runner.runPython(code));
      };
      this.ready = true;
    };
    load();
  },
  methods: {
    nextForm() {
      this.currentForm = (this.currentForm + 1) % this.forms.length;
      this.runner.runPython(this.codes[this.currentForm]);
    }
  }
};
</script>

<template>
  <p v-if="!ready" class="loading">loading…</p>
  <Form1 v-else-if="currentForm == 0" />
  <Form2 v-else-if="currentForm == 1" />
  <Form3 v-else-if="currentForm == 2" />
  <Form6 v-else-if="currentForm == 3" />
  <button class="python" @click="nextForm">
    <img src="https://abs-0.twimg.com/emoji/v2/svg/1f40d.svg" alt="python" />
  </button>
</template>

<style scoped>
.loading {
  font-size: 2rem;
}

.python {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 5rem;
  height: 5rem;
  opacity: .5;
  transition: opacity .25s;
}

.python:where(:hover, :focus-visible) {
  opacity: 1;
}
</style>
