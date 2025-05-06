<script setup>
    import { Card } from 'primevue';
</script>

<template>
  <Card>
    <template #header>
        <slot name="header" />
    </template>

    <template #title>
      <slot name="title" />
    </template>

    <template #subtitle>
        <slot name="subtitle"/>
    </template>

    <template #content>
      <slot />
    </template>

    <template #footer>
      <slot name="footer" />
    </template>
  </Card>
</template>

