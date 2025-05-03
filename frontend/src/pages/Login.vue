<script setup>
import {Toast,Message} from "primevue";
import { useRouter } from "vue-router";
import { Form } from "@primevue/forms";
import { reactive,ref,onUnmounted,onMounted } from "vue";
import { Button,Input,Container } from "../components";
import {Inputs} from "../data/Login.js"
import http from "../utils/http.js"

const router = useRouter()
const initialValues = reactive({
    username:"",
    password:""
})

const message = ref("")

const resolver = ({values}) =>{
    const errors = {};

    if(!values.username){
        errors.username = [{ message: "El usuario es requerido" }];
    }
    if(!values.password){
        errors.password = [{ message: "La contraseña es requerida" }];
    }

    return {
        values,
        errors
    }
}

const onChange = (e) => {
    const { name, value } = e.target;
    initialValues[name] = value;
}

const onFormSubmit = async ({valid}) =>{
    if(valid){
        try {
            const response = await http("POST","/auth/login",null,{
                username:initialValues.username,
                password:initialValues.password
            })
            localStorage.setItem("token",response.data.access_token)
            router.push("/home")
        } catch (error) {
            let msg = error?.message?.split(" - ")[1]
            if(msg){
                message.value = JSON.parse(msg).message
            }
            throw error;
        }
    }else{
        throw "El formulario no es valido."
    }
}

onUnmounted(() => {
    message.value = ""
})

onMounted(()=>{
    const token = localStorage.getItem("token");
    if(token){
        router.push("/home")
    }
})

</script>
<template>
        <Container>
            <Toast />
            <Form v-slot="$form" :initialValues :resolver @submit="onFormSubmit" class="p-4 sm:w-10 md:w-8 lg:w-6 h-full flex flex-column justify-content-center">
                <div class="grid gap-3">

                    <div v-for="(input,index) in Inputs" :key="index" class="w-full flex flex-column gap-2">
                        <Input :form="$form" :label=input.label :name=input.name :type=input.type :placeholder=input.placeholder @input="onChange" :password=input.password />
                    </div>
                    <Message v-if="message" severity="error" size="small" variant="simple">{{ message }}</Message>
                    <div class="w-full">
                        <Button rounded type="submit" severity="success" class="w-full font-bold">Iniciar sesión</Button>
                    </div>
                </div>
                <div class="w-full flex justify-content-center">
                    <p>No tenes una cuenta? <a class="text-primary" href="/register">Registrate</a></p>
                </div>
            </Form>
        </Container>
</template>
