<script setup>
import { onMounted, computed } from 'vue';
import { useStore } from 'vuex';
import { Card, Image, Message, Button } from "../components"
import { Paginator } from 'primevue';

const {VITE_APP_URL_API} = import.meta.env
  
const store = useStore();
const songs = computed(() => store.state.songs);

onMounted(async () => {
  console.log(songs.length)
  if(!songs.length){
    await store.dispatch('fetchSongs', { apiUrl: VITE_APP_URL_API });
  }
});

async function navigatePages(url_songs){
  if (!url_songs) return;
  try {
    console.log("URL válida:", url_songs);
    await store.dispatch('navigatePages', { url_songs: url_songs });
  } catch (err) {
    console.error("Error al navegar:", err);
  }
}

async function onPage(e){
  console.log(e)
}
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
        <Paginator :rows="10" :totalRecords="songs.tracks.total_pages" @page="onPage"></Paginator>
        <Button @click="() => navigatePages(songs.tracks.previous)" :disabled="!songs.tracks.previous">Anterior</Button>
        <Button @click="() => navigatePages(songs.tracks.next)" :disabled="!songs.tracks.next">Siguiente</Button>
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