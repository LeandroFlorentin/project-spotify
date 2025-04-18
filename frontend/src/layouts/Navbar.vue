<script setup>
    import { RouterView, useRouter } from 'vue-router';
    import { Button, Input } from '../components/index.js';
    import { InputGroup,InputGroupAddon } from 'primevue';
    import { ref, watch } from 'vue';
    
    const router = useRouter();
    const search = ref({
        name:"",
        password:""
    });
    
    const goToHome = () => {
        router.push('/home');
    };

    const handleInput = (event) => {
        const {name,value} = event.target;
        search.value[name] = value
    };
    
    watch(search.value, (newValue) => {
        console.log('Nuevo valor:', newValue);
    });
</script>

<template>
    <div class="navbar grid">
        <div class="col-2 flex align-items-center gap-2 justify-content-center">
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
        <div class="col-4 flex pt-2">
            <InputGroup class="search-group">
                <InputGroupAddon class="search-addon">
                    <i class="pi pi-search" style="font-size: 1.4rem;"></i>
                </InputGroupAddon>
                <Input 
                    name="name"
                    :value="search.name"
                    :onInput="handleInput"
                    placeholder="Que cancion quieres buscar?"
                    rounded
                    className="search-input"
                />
            </InputGroup>
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

.pointer {
    cursor: pointer;
}
</style>