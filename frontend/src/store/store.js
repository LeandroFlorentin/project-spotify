import { createStore } from 'vuex';
import http from '../utils/http';

export default createStore({
  state: {
    songs: {},
  },
  mutations: {
    setSongs(state, songs) {
      state.songs = songs;
    },
  },
  actions: {
    async fetchSongs({ commit }, { query = 'Almafuerte', limit = 30, apiUrl }) {
      try {
        if (query === '') {
          query = 'Almafuerte';
        }
        const response = await http('GET', `${apiUrl}songs/get_songs?q=${query}&limit=${limit}`, {
          Authorization: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImlkIjoxLCJ1c2VybmFtZSI6IkpvaG4gZG9lIiwiZW1haWwiOiJKb2huRG9lQGhvdG1haWwuY29tIiwicm9sZSI6WyJBRE1JTiJdLCJkaXNhYmxlZCI6MH0sImlhdCI6MTc0NTI1MDkyMSwiZXhwIjoxNzQ1MjU0NTIxfQ.vrQX0gwo6vOTrXVCnDGbvSbTbDaThe5xjKMxKk9WobY`,
        });
        commit('setSongs', response);
      } catch (error) {
        throw error;
      }
    },
  },
});
