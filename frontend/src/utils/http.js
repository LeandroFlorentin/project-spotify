import axios from 'axios';
import store from '../store/store.js';

const { VITE_APP_URL_API } = import.meta.env;

const instance = axios.create({
  baseURL: VITE_APP_URL_API,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
});

instance.interceptors.response.use(
  (config) => {
    return config;
  },
  (error) => {
    console.log('ERROR', error);
    if (error?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default async function http(method, url, headers = {}, body = null, rawResponse = false, throwOnError = true) {
  try {
    store.dispatch('setLoading', true);
    const options = {
      method,
      url,
      headers: {
        ...headers,
      },
    };

    if (body) {
      options.data = body;
    }
    const response = await instance(options);
    console.log('RESPONSE', response);
    return response?.data;
  } catch (error) {
    console.error('Hubo un problema en la petición:', error.message);
    throw error;
  } finally {
    store.dispatch('setLoading', false);
  }
}
