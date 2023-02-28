<script>
export default {
  data() {
    return {
      input1: 0,
      input2: 0
    };
  },
  computed: {
    output() {
      return window.python(`fun(${this.input1 || 0}, ${this.input2 || 0})`);
    }
  }
};
</script>

<template>
  <main>
    <h1>Tema #1</h1>
    <div class="inputs">
      <input v-model="input1" type="number" />
      <input v-model="input2" type="number" />
    </div>
    <p>{{ output }}</p>
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
  margin-bottom: 1rem;
  font-size: 3rem;
  color: #77b255;
  text-decoration: .1em dashed underline;
  text-underline-offset: .25em;
}

.inputs {
  display: flex;
  gap: .5rem;
}
</style>
