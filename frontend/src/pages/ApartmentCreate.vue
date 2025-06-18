<template>
  <div class="max-w-xl mx-auto p-6 bg-white rounded shadow mt-10">
    <h2 class="text-2xl font-bold mb-4">Додати нову квартиру</h2>

    <form @submit.prevent="createApartment">
      <div class="mb-4">
        <label class="block mb-1">Назва</label>
        <input v-model="name" class="w-full border px-3 py-2 rounded" required />
      </div>

      <div class="mb-4">
        <label class="block mb-1">Опис</label>
        <textarea v-model="description" class="w-full border px-3 py-2 rounded" required></textarea>
      </div>

      <div class="mb-4">
        <label class="block mb-1">Ціна</label>
        <input type="number" v-model.number="price" class="w-full border px-3 py-2 rounded" required />
      </div>

      <div class="mb-4">
        <label class="block mb-1">Кількість кімнат</label>
        <input type="number" v-model.number="number_of_rooms" class="w-full border px-3 py-2 rounded" required />
      </div>

      <div class="mb-4">
        <label class="block mb-1">Площа (м²)</label>
        <input type="number" v-model.number="square" class="w-full border px-3 py-2 rounded" required />
      </div>

      <div class="mb-4">
        <label class="block mb-1">Доступність</label>
        <select v-model="availability" class="w-full border px-3 py-2 rounded">
          <option :value="true">Доступна</option>
          <option :value="false">Недоступна</option>
        </select>
      </div>

      <div v-if="error" class="text-red-500 text-sm mb-4">{{ error }}</div>

      <button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
        Створити
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/api/index.js'

const name = ref('')
const description = ref('')
const price = ref(null)
const number_of_rooms = ref(null)
const square = ref(null)
const availability = ref(true)
const error = ref('')
const router = useRouter()

const createApartment = async () => {
  try {
    const token = localStorage.getItem('access')

    const response = await api.post(
      '/apartments/',
      {
        name: name.value,
        description: description.value,
        price: price.value,
        number_of_rooms: number_of_rooms.value,
        square: square.value,
        availability: availability.value,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    )

    router.push(`/apartments/${response.data.slug}`)
  } catch (err) {
    error.value = err.response?.data?.detail || 'Не вдалося створити квартиру'
  }
}

</script>
