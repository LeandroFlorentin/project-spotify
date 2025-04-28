<script setup>
import { onMounted, computed, watch } from 'vue';
import { useStore } from 'vuex';

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
      <div v-if="songs.tracks" class="songs-container">
        <div v-for="song in songs.tracks.items" :key="song.id" class="song-item">
          <div class="song-name">{{ song.name }}</div>
          <div class="song-artist">{{ song.artists[0].name }}</div>
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
    height: 100vh;
    background-color: black;
    color: white;
  }

  .songs-container {
    width: 80%;
    max-height: 80vh;
    overflow-y: auto;
    padding: 20px;
  }

  .song-item {
    padding: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
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