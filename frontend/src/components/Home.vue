<template>
  <div>
    <h1>Home</h1>
    <p>Count: {{ counter.count }}</p>
    <button @click="counter.increment">Increment</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '../stores/counter';

const counter = useCounterStore();
</script>
