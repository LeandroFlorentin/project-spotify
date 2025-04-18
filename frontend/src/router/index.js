import { createRouter, createWebHistory } from 'vue-router';
import Home from '../pages/Home.vue';
import Login from '../pages/Login.vue';
import Navbar from '../layouts/Navbar.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: '',
      component: Navbar,
      children: [
        {
          path: '/',
          component: Home,
        },
      ],
    },
    {
      path: '/home',
      name: 'home',
      component: Navbar,
      children: [
        {
          path: '/home',
          component: Home,
        },
      ],
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
  ],
});

export default router;
