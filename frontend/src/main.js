import { createApp } from 'vue';
import PrimeVue from 'primevue/config';
import ToastService from 'primevue/toastservice';
import Aura from '@primeuix/themes/aura';
import App from './App.vue';
import router from './router';
import store from './store/store';
import 'primeflex/primeflex.css';
const app = createApp(App);
app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
});
app.use(ToastService);
app.use(router);
app.use(store);
app.mount('#app');
