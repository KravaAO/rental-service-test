import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import ApartmentPage from '../pages/ApartmentPage.vue'
import ApartmentCreate from '../pages/ApartmentCreate.vue'
import Login from '../pages/Login.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/apartments/create', name: 'ApartmentCreate', component: ApartmentCreate },
  { path: '/apartments/:slug', name: 'ApartmentPage', component: ApartmentPage },
  { path: '/apartments/:slug/edit', name: 'ApartmentEdit', component: () => import('../pages/ApartmentEdit.vue') },
]

export default createRouter({ history: createWebHistory(), routes })
