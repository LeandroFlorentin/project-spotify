<script setup>
    import { Avatar } from 'primevue';
    const props = defineProps({
        image:String,
        shape:String
    })
</script>
<template>
    <Avatar :image="image" :shape="shape" />
</template>