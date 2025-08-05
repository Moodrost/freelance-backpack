<template>
  <div>
    <h1>About</h1>
    <p>Shared count: {{ counter.count }}</p>
  </div>
</template>

<script setup>
import { useCounterStore } from '../stores/counter';

const counter = useCounterStore();
</script>
