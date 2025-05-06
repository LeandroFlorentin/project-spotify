<script setup>
    import { Image } from "primevue"
    const props = defineProps({
        src:String,
        alt:String,
        width:String,
        height:String,
        preview:Boolean
    })
</script>
<template>
    <Image :src="src" :alt="alt" :width="width" :height="height" :preview="preview"/>
</template>