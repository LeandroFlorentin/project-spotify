<script setup>
    import {Message} from "primevue"
    import {Avatar} from "./index"
    const props = defineProps({
        severity:String,
        image:String,
        shape:String
    })
</script>
<template>
    <Message :severity="severity">
        <slot/>
    </Message>
</template>