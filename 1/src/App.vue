<script>
import Form from './components/Form.vue';

export default {
  components: {
    Form
  },
  data() {
    return {
      runner: null,
      code: null,
      ready: false
    };
  },
  mounted() {
    const load = async () => {
      [this.runner, this.code] = await Promise.all([
        loadPyodide(),
        (await fetch('/main.py')).text()
      ]);
      await this.runner.loadPackage('numpy');
      this.runner.runPython(this.code);
      window.python = this.runner.runPython;
      this.ready = true;
    };
    load();
  }
};
</script>

<template>
  <Form v-if="ready" />
  <p v-else class="loading">loading…</p>
  <img class="python" src="https://abs-0.twimg.com/emoji/v2/svg/1f40d.svg" alt="python" />
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
  opacity: .5;
  transition: opacity .25s;
}

.python:hover {
  opacity: 1;
}
</style>
