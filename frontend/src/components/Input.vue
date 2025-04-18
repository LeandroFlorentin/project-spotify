<script setup>
import InputText from 'primevue/inputtext';

const props = defineProps({
    placeholder: String,
    value: String,
    name: String,
    rounded: {
        type: Boolean,
        default: false
    },
    onInput: Function,
    className: String
})

</script>

<template>
    <InputText 
        :name="name"
        :value="value"
        @input="onInput"
        :placeholder="placeholder"
        :class="className"
    />
</template>