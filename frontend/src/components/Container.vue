<script setup>
</script>

<template>
        <div class="wrapper">
            <div class="login-container surface-0 border-round-xl shadow-4 flex justify-content-center">
                <slot></slot>
            </div>
        </div>
</template>

<style scoped>
.login-container {
    width: 80%;
    height: 100vh;
    max-width: 700px;
    min-width: 300px;
}
.wrapper{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100vh;
    background-color: black;
}
</style>