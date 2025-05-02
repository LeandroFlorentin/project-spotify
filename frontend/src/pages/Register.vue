<script setup>
import { onMounted } from 'vue';
import { Form } from "@primevue/forms";
import { Container,Input } from '../components';
import router from '../router';

onMounted(()=>{
    const token = localStorage.getItem("token");
    if(token){
        router.push("/home")
    }
})
</script>
<template>
    <Container>
        <Form class="p-4 sm:w-10 md:w-8 lg:w-6 h-full flex flex-column justify-content-center">
            <Input label="Usuario" />
        </Form>
    </Container>
</template>