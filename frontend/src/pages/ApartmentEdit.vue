<template>
  <div class="p-6" v-if="apartment">
    <h1 class="text-2xl font-bold mb-4">Редагувати квартиру</h1>
    <form @submit.prevent="updateApartment">
      <div class="mb-4">
        <label class="block mb-1">Назва</label>
        <input v-model="form.name" class="w-full border px-3 py-2 rounded" required />
      </div>
      <div class="mb-4">
        <label class="block mb-1">Опис</label>
        <textarea v-model="form.description" class="w-full border px-3 py-2 rounded" required></textarea>
      </div>
      <div class="mb-4">
        <label class="block mb-1">Ціна</label>
        <input type="number" v-model.number="form.price" class="w-full border px-3 py-2 rounded" required />
      </div>
      <div class="mb-4">
        <label class="block mb-1">Кількість кімнат</label>
        <input type="number" v-model.number="form.number_of_rooms" class="w-full border px-3 py-2 rounded" required />
      </div>
      <div class="mb-4">
        <label class="block mb-1">Площа (м²)</label>
        <input type="number" v-model.number="form.square" class="w-full border px-3 py-2 rounded" required />
      </div>
      <div class="mb-4">
        <label class="block mb-1">Доступність</label>
        <select v-model="form.availability" class="w-full border px-3 py-2 rounded">
          <option :value="true">Доступна</option>
          <option :value="false">Недоступна</option>
        </select>
      </div>
      <div v-if="error" class="text-red-500 text-sm mb-4">{{ error }}</div>
      <button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Зберегти</button>
    </form>
  </div>
  <div v-else class="p-6">Завантаження...</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/index.js'

const apartment = ref(null)
const form = ref({})
const error = ref('')
const route = useRoute()
const router = useRouter()

onMounted(async () => {
  try {
    const slug = route.params.slug
    const response = await api.get(`apartments/${slug}/`)
    apartment.value = response.data
    form.value = {
      name: response.data.name,
      description: response.data.description,
      price: response.data.price,
      number_of_rooms: response.data.number_of_rooms,
      square: response.data.square,
      availability: response.data.availability,
    }
  } catch (err) {
    error.value = 'Не вдалося завантажити дані.'
  }
})

const updateApartment = async () => {
  try {
    const slug = route.params.slug
    await api.patch(`apartments/${slug}/`, form.value)
    router.push(`/apartments/${slug}`)
  } catch (err) {
    error.value = err.response?.data?.detail || 'Не вдалося оновити квартиру.'
  }
}
</script>
