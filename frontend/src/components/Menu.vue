<script setup>
    import { Menu } from 'primevue';
    import { ref } from 'vue';

    const props = defineProps({
        id:String,
        model:Object,
        popup:Boolean
    })

    const menuRef = ref();
    defineExpose({
        toggle: (event) => menuRef.value?.toggle?.(event)
    });
</script>

<template>
    <Menu ref="menuRef" :id="id" :model="model" :popup="popup"/>
</template>