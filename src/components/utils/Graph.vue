<script>
export default {
  props: ['label', 'dimension', 'points'],
  computed: {
    chosenPoints() {
      return this.points.filter(point => {
        if (!(-this.dimension <= point[0] && point[0] <= this.dimension)) return false;
        if (!(-this.dimension <= point[1] && point[1] <= this.dimension)) return false;
        return true;
      });
    }
  }
};
</script>

<template>
  <article>
    <label>{{ label }}</label>
    <svg :viewBox="`${-dimension} ${-dimension} ${2 * dimension} ${2 * dimension}`">
      <line :x1="-dimension" :y1="0" :x2="dimension" :y2="0" />
      <line :y1="-dimension" :x1="0" :y2="dimension" :x2="0" />
      <circle v-for="point of chosenPoints" :cx="point[0]" :cy="-point[1]" :r=".25" />
    </svg>
  </article>
</template>

<style scoped>
svg {
  height: 300px;
  border: 2px solid #666;
}

line {
  stroke: #999;
  stroke-width: .1;
  stroke-dasharray: .25;
}

circle {
  fill: var(--green);
}
</style>
