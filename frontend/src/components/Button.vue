<script setup>
import Button from 'primevue/button';
import 'primeicons/primeicons.css';

defineProps({
    icon: String,
    label: String,
    iconPos: {
        type: String,
        default: "right",
        validator: (value) => ["right", "top", "bottom", "left"].includes(value)
    },
    className: String,
    loading: String,
    click: Function,
    as: String,
    href: String,
    target: String,
    disabled: Boolean,
    severity: {
        type: String,
        default: "secondary"
    },
    outlined: Boolean,
    rounded: Boolean,
    text: Boolean,
    size: String,
    style:Object
})
</script>

<template>
    <Button 
        :icon="icon" 
        :label="label" 
        :iconPos="iconPos" 
        :loading="loading" 
        :style="style" 
        @click="click" 
        :as="as" 
        :href="href" 
        :target="target" 
        :disabled="disabled" 
        :severity="severity" 
        :outlined="outlined" 
        :rounded="rounded" 
        :text="text"
        :class="className"
        :size="size"
    >
        <slot />
    </Button>
</template>