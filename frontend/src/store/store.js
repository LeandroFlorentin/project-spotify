import { createStore } from 'vuex';
import http from '../utils/http';

export default createStore({
  state: {
    songs: {},
    loading: false,
  },
  mutations: {
    setSongs(state, songs) {
      state.songs = songs;
    },
    setLoading(state, value) {
      state.loading = value;
    },
  },
  actions: {
    async fetchSongs({ commit }, { query = 'Almafuerte', limit = 30, apiUrl }) {
      try {
        let token = localStorage.getItem('token');
        if (query === '') {
          query = 'Almafuerte';
        }
        const response = await http('GET', `${apiUrl}songs/get_songs?q=${query}&limit=${limit}`, {
          Authorization: `Bearer ${token}`,
        });
        commit('setSongs', response);
      } catch (error) {
        throw error;
      }
    },
    setLoading({ commit }, value) {
      commit('setLoading', value);
    },
  },
});
