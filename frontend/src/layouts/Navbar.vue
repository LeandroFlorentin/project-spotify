<script setup>
import { RouterView, useRouter } from 'vue-router';
import { Button, Input, Menu } from '../components/index.js';
import { InputGroup, InputGroupAddon } from 'primevue';
import { ref, watch } from 'vue';
import debounce from 'lodash.debounce';
import { useStore } from 'vuex';

const { VITE_APP_URL_API } = import.meta.env;

const menu = ref(null);

const items = ref([
    {
        items: [
            {
                label: 'Mi perfil',
                icon: 'pi pi-user',
                command: () => {
                    router.push("/mi_perfil");
                }
            },
            {
                label: 'Cerrar sesión',
                icon: 'pi pi-sign-out',
                command: () => {
                    localStorage.removeItem("token");
                    router.push("/login");
                }
            }
        ]
    }
]);

const router = useRouter();
const store = useStore();
const search = ref("");

const goToHome = () => {
    router.push('/home');
};

const searchSong = async () => {
    try {
        await store.dispatch('fetchSongs', {
            query: search.value,
            apiUrl: VITE_APP_URL_API
        });
    } catch (error) {
        throw error;
    }
};

const debouncedProcessInput = debounce(searchSong, 2000);

const handleInput = (event) => {
    const { value } = event.target;
    search.value = value;
    debouncedProcessInput();
};

const toggle = (event) => menu.value?.toggle?.(event);
</script>

<template>
    <div class="flex justify-content-between navbar grid">
        <div class="col-3 md:col-3 lg:col-2 flex align-items-center gap-2 justify-content-center">
            <div @click="goToHome" class="pointer">
                <img alt="spotify" src="../assets/spotify_white.png" width="42" height="42"/>
            </div>
            <Button
                icon="pi pi-home"
                text
                rounded
                className="btn-home"
                @click="goToHome"
            />
        </div>
        <div class="col-6 md:col-6 lg:col-4 flex pt-2">
            <InputGroup class="search-group">
                <InputGroupAddon class="search-addon">
                    <i class="pi pi-search" style="font-size: 1.4rem;"></i>
                </InputGroupAddon>
                <Input
                    :value="search"
                    placeholder="Que cancion quieres buscar?"
                    :onInput="handleInput"
                    rounded
                    className="search-input"
                />
            </InputGroup>
        </div>
        <div class="col-3 md:col-3 lg:col-3 flex justify-content-end">
            <Button
                type="button"
                icon="pi pi-align-justify"
                @click="toggle($event)"
                aria-haspopup="true"
                aria-controls="overlay_menu"
            />
            <Menu ref="menu" id="overlay_menu" :model="items" popup="true" />
        </div>
    </div>
    <RouterView />
</template>

<style scoped>
.navbar{
    width: 100%;
    height: 64px;
    background-color: #000;
    padding: 0 0px;
    z-index: 9999999999;
    position: sticky;
    top: 0;
    left: 0;
}

:deep(.btn-home) {
    background-color: rgba(255, 255, 255, 0.1) !important;
    border: none !important;
    width: 50px !important;
    height: 50px !important;
}

:deep(.btn-home:hover) {
    background-color: rgba(255, 255, 255, 0.2) !important;
    scale: 1.05;
}

:deep(.btn-home:hover .p-button-icon) {
    scale: 1.1;
}

:deep(.p-button-icon) {
    font-size: 1.5rem;
    transition: font-size 0.1s ease;
}

:deep(.search-group) {
    width: 100%;
    background-color: rgba(255, 255, 255, 0.1) !important;
    border-radius: 50px !important;
    border: 2px solid transparent !important;
    padding: 0 !important;
    transition: border 0.3s ease;
}

:deep(.search-group:focus-within) {
    border: 2px solid white !important;
}

:deep(.search-group:hover .search-addon) {
    color: white !important;
}

:deep(.search-addon) {
    background-color: transparent !important;
    border: none !important;
    color: rgba(255, 255, 255, 0.5) !important;
    padding: 0 0 0 10px !important;
    transition: color 0.3s ease;
}

:deep(.search-input) {
    width: 100%;
    background-color: transparent !important;
    border: none !important;
    color: white !important;
    height: 42px !important;
    padding: 0 0.5rem !important;
}

:deep(.search-input:focus) {
    box-shadow: none !important;
    border-color: transparent !important;
}

:deep(.search-input:enabled:focus) {
    box-shadow: none !important;
    border-color: transparent !important;
}

:deep(.p-inputgroup) {
    display: flex !important;
    align-items: center !important;
}

:deep(.p-inputtext){
    border:1px solid transparent;
    background-color: transparent;
}

:deep(.p-inputtext:focus){
    border:1px solid transparent !important;
}

:deep(.p-inputtext:hover){
    border:1px solid transparent !important;
}

.pointer {
    cursor: pointer;
}
</style>
