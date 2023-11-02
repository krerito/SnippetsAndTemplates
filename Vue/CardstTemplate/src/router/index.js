import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: function () {
      return import(/* webpackChunkName: "home" */ '../views/LoginView.vue')
    },
  },
  {
    path: '/Printers',
    name: 'Printers',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "Printers" */ '../views/PrintersView.vue')
    },
  },
  {
    path: '/Atem',
    name:'Atem',
    //Aqui no se puede usar la funcion de componente, por eso usamos la funcion
    //window.location.href = "url" para poder hacer la conexion a algo externo
     beforeEnter(to, from, next) {
      window.location.href = "http://atem.net/Home/";
    }
  },
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
