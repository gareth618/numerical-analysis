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
        await loadPyodide(),
        await (await fetch('/main.py')).text()
      ]);
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
  position: absolute;
  top: 2rem;
  right: 2rem;
  width: 5rem;
  opacity: .5;
  transition: opacity .25s;
  animation: rotate 5s ease-in-out infinite;
}

.python:hover {
  opacity: 1;
}

@keyframes rotate {
  0% {
    rotate: 0deg;
  }
  80% {
    rotate: 0deg;
  }
  100% {
    rotate: 360deg;
  }
}
</style>

<style>
* {
  box-sizing: border-box;
}

html {
  color: #ddd;
  line-height: 1.2;
  font-family: 'Source Code Pro', monospace;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
}

body {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
  height: 100vh;
  background-color: #222;
}

:where(h1, p) {
  margin: 0;
}

input {
  padding: .25rem;
  font-size: 1rem;
  font-family: inherit;
  color: #222;
  background-color: #ddd;
  border: none;
}

input:focus {
  outline: .2rem solid #77b255;
}

input::selection {
  background-color: #77b255;
}
</style>
