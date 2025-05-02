<script setup>
import {InputText,Message,Password} from 'primevue';

const props = defineProps({
    placeholder: String,
    value: String,
    name: String,
    rounded: {
        type: Boolean,
        default: false
    },
    onInput: Function,
    className: String,
    password:Boolean,
    type:String,
    label:String,
    form:Object
})

</script>

<template>
    <div class="w-full flex flex-column gap-2">
        <label :for="name">{{label}}</label>
        <Password v-if="password" @input="onInput" :feedback="false" :name="name" type="password" :placeholder="placeholder" class="w-full" :toggleMask="true"/>
        <InputText v-else :name="name" :type="type" :placeholder="placeholder" class="w-full" @input="onInput"/>
        <div v-if="form">
            <Message v-if="form[name]?.invalid" severity="error" size="small" variant="simple">
                <i class="pi pi-exclamation-circle"></i> {{ form[name].error?.message }}
            </Message>
        </div>
    </div>
</template>

<style scoped>
:deep(.p-password) {
    width: 100%;
}

:deep(.p-password-input) {
    width: 100% !important;
}

:deep(.p-password .p-inputtext) {
    width: 100%;
}

</style>