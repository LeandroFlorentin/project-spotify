<script setup>
import { onMounted, computed, watch } from 'vue';
import { useStore } from 'vuex';
import { Card, Image, Message } from "../components"

const {VITE_APP_URL_API} = import.meta.env
  
const store = useStore();
const songs = computed(() => store.state.songs);

watch(songs, (newSongs) => {
  console.log('Canciones actualizadas:', newSongs);
});

onMounted(async () => {
  await store.dispatch('fetchSongs', { apiUrl: VITE_APP_URL_API });
});
</script>

<template>
    <div id="app" class="wrapper">
      <div v-if="songs.tracks" class="flex w-full flex-wrap justify-content-center gap-2">
        <div v-for="song in songs.tracks.items" :key="song.id" class="song-item">
          <Card>
            <template #header><Image style="cursor:pointer" :src="song.album.images[1].url" :alt="song.title"/></template>
            <template #title>{{ song.title }}</template>
            <template #subtitle>
              <div class="flex">
                <div v-for="artist in song.artist">Artistas 
                <Message severity="success"><span class="ml-2">{{ artist.name }}</span></Message>
              </div>
              </div>
            </template>
          </Card>
        </div>
      </div>
      <div v-else>
        No hay canciones disponibles
      </div>
    </div>
</template>

<style scoped>
  .wrapper{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    background-color: black;
    color: white;
  }

  .songs-container {
    width: 80%;
    max-height: 80vh;
    padding: 20px;
  }

  .song-name {
    font-size: 1.1rem;
    font-weight: bold;
  }

  .song-artist {
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.7);
  }
</style>