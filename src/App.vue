<script>
import Form1 from './components/Form1.vue';
import Form2 from './components/Form2.vue';

export default {
  components: {
    Form1,
    Form2
  },
  data() {
    return {
      runner: null,
      code: null,
      ready: false,
      currentForm: 0,
      forms: [1, 2],
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
      window.python = this.runner.runPython;
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
