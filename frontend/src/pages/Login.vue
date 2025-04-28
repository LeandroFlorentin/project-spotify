<script setup>
import {useToast,Toast,Message,InputText,Password} from "primevue";
import { useRouter } from "vue-router";
import { Form } from "@primevue/forms";
import { reactive,ref,onUnmounted } from "vue";
import { Button } from "../components/index";
import http from "../utils/http.js"

const toast = useToast();
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
    }
}

onUnmounted(() => {
    message.value = ""
})

</script>
<template>
    <div class="wrapper">
        <div class="login-container surface-0 border-round-xl shadow-4 flex justify-content-center">
            <Toast />
            <Form v-slot="$form" :initialValues :resolver @submit="onFormSubmit" class="p-4 sm:w-10 md:w-8 lg:w-6 h-full flex flex-column justify-content-center">
                <div class="grid gap-3">
                    <div class="w-full flex flex-column gap-2">
                        <label for="username">Email o nombre de usuario</label>
                        <InputText name="username" type="text" placeholder="Usuario" class="w-full" @input="onChange"/>
                        <Message v-if="$form.username?.invalid" severity="error" size="small" variant="simple">
                            <i class="pi pi-exclamation-circle"></i> {{ $form.username.error?.message }}
                        </Message>
                    </div>
                    <div class="w-full flex flex-column gap-2">
                        <label for="password">Contraseña</label>
                        <Password @input="onChange" :feedback="false" name="password" type="password" placeholder="Contraseña" class="w-full" :toggleMask="true"/>
                        <Message v-if="$form.password?.invalid" severity="error" size="small" variant="simple">
                            <i class="pi pi-exclamation-circle"></i> {{ $form.password.error?.message }}
                        </Message>
                    </div>
                    <Message v-if="message" severity="error" size="small" variant="simple">{{ message }}</Message>
                    <div class="w-full">
                        <Button rounded type="submit" severity="success" class="w-full font-bold">Iniciar sesión</Button>
                    </div>
                </div>
            </Form>
        </div>
    </div>
</template>
<style scoped>
.wrapper{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100vh;
    background-color: black;
}

.login-container {
    width: 80%;
    height: 100vh;
    max-width: 700px;
    min-width: 300px;
}

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
