<template>
  <div class="max-w-md mx-auto p-6 bg-white rounded shadow mt-10">
    <h1 class="text-2xl font-bold mb-4 text-center">Вхід</h1>

    <form @submit.prevent="login">
      <div class="mb-4">
        <label class="block mb-1">Email</label>
        <input
          v-model="email"
          type="email"
          class="w-full border px-3 py-2 rounded"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1">Пароль</label>
        <input
          v-model="password"
          type="password"
          class="w-full border px-3 py-2 rounded"
          required
        />
      </div>

      <div v-if="error" class="text-red-500 text-sm mb-4">{{ error }}</div>

      <button
        type="submit"
        class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
      >
        Увійти
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const login = async () => {
  error.value = ''

  try {
    const response = await axios.post(
      import.meta.env.VITE_API_URL + 'users/api/token/',
      {
        email: email.value,
        password: password.value,
      },
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
    )

    localStorage.setItem('access', response.data.access)
    localStorage.setItem('refresh', response.data.refresh)
    localStorage.setItem('username', email.value)

    router.push('/')
  } catch (err) {
    error.value =
      err.response?.data?.detail || 'Невірний email або пароль'
  }
}
</script>
