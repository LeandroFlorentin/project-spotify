<script setup>
import { onMounted, reactive } from 'vue';
import { Form } from "@primevue/forms";
import { Container,Input,Button } from '../components';
import {Inputs} from "../data/Register.js"
import router from '../router';
import http from '../utils/http'

const initialValues = reactive({
    username:"",
    email:"",
    password:"",
    role:[
        "USER"
    ]
})

const resolver = ({values}) =>{
    const errors = {};

    if(!values.username){
        errors.username = [{ message: "El usuario es requerido" }];
    }

    if(!values.email){
        errors.email = [{message:"El email es requerido"}]
    }

    if(!values.password){
        errors.password = [{ message: "La contraseña es requerida" }];
    }

    return {
        values,
        errors
    }
}

function onChange(e){
    const {name,value}= e.target;
    console.log(name,value)
    initialValues[name] = value
}

async function onFormSubmit({valid}){
    if(valid){
        try {
            await http("POST","users/create",null,{
                username:initialValues.username,
                password:initialValues.password,
                email:initialValues.email,
                role:initialValues.role
            })
            router.push("/login")
        } catch (error) {
            console.log("ERROR",error)
            throw error;
        }

    }else{
        throw "El formulario no es valido."
    }
}

onMounted(()=>{
    const token = localStorage.getItem("token");
    if(token){
        router.push("/home")
    }
})
</script>
<template>
    <Container>
        <Form v-slot="$form" :initialValues :resolver @submit="onFormSubmit" class="p-4 sm:w-10 md:w-8 lg:w-6 h-full flex flex-column justify-content-center">
            <div v-for="(input,index) in Inputs" :key="index">
                <Input @input="onChange" :form="$form" :name="input.name" :label="input.label" :type="input.type" :placeholder="input.placeholder" :password="input.password" />
            </div>
            <div class="w-full">
                <Button rounded type="submit" severity="success" class="w-full font-bold">Registrar</Button>
            </div>
        </Form>
    </Container>
</template>