<template>
  <header class="bg-blue-600 text-white px-4 py-3 flex justify-between items-center">
    <h1 class="text-xl font-bold">
      <router-link to="/">Rental Service</router-link>
    </h1>

    <nav class="flex items-center gap-4">
     <template v-if="isAuthenticated">
      <router-link v-if="isAuthenticated" to="/apartments/create" class="bg-green-500 px-3 py-1 rounded hover:bg-green-600">
        Додати квартиру
      </router-link>
      </template>

       <div>
          <template v-if="isAuthenticated">
            <span class="mr-4">{{ username }}</span>
            <button @click="logout" class="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600">
              Вийти
            </button>
          </template>

          <template v-else>
            <router-link to="/login" class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">
              Увійти
            </router-link>
          </template>
        </div>
    </nav>
  </header>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const isAuthenticated = computed(() => {
  return !!localStorage.getItem('access')
})

const logout = () => {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  localStorage.removeItem('username')
  router.push('/login')
}
</script>
