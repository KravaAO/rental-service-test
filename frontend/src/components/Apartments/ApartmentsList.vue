<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Список квартир</h1>

    <!-- 🔍 Форма фільтрів -->
    <form @submit.prevent="applyFilters" class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
      <div>
        <label class="block text-sm font-medium">Ціна від</label>
        <input v-model="filters.priceFrom" type="number" class="w-full p-2 border rounded" />
      </div>
      <div>
        <label class="block text-sm font-medium">Ціна до</label>
        <input v-model="filters.priceTo" type="number" class="w-full p-2 border rounded" />
      </div>
      <div>
        <label class="block text-sm font-medium">Кількість кімнат</label>
        <input v-model="filters.rooms" type="number" class="w-full p-2 border rounded" />
      </div>
      <div class="flex items-center gap-2">
        <input v-model="filters.availability" type="checkbox" id="available" />
        <label for="available">Тільки доступні</label>
      </div>
      <div class="md:col-span-2">
        <label class="block text-sm font-medium">Пошук</label>
        <input
          v-model="filters.search"
          type="text"
          placeholder="назва або опис..."
          class="w-full p-2 border rounded"
        />
      </div>
      <div class="md:col-span-2 flex justify-end">
        <button
          type="submit"
          class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          Застосувати
        </button>
      </div>
    </form>

    <!-- 🏠 Список квартир -->
    <ul class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <li
        v-for="apartment in apartments"
        :key="apartment.slug"
        class="border p-4 rounded shadow hover:shadow-md transition"
      >
        <router-link
          :to="`/apartments/${apartment.slug}`"
          class="text-xl font-semibold text-blue-600 hover:underline"
        >
          {{ apartment.name }}
        </router-link>
        <p class="text-sm text-gray-600 mb-2">Власник: {{ apartment.owner }}</p>
        <p><strong>Ціна:</strong> {{ apartment.price }} грн</p>
        <p><strong>Кімнат:</strong> {{ apartment.number_of_rooms }}</p>
        <p><strong>Площа:</strong> {{ apartment.square }} м²</p>
        <p :class="apartment.availability ? 'text-green-600' : 'text-red-600'">
          {{ apartment.availability ? 'Доступна' : 'Недоступна' }}
        </p>
      </li>
    </ul>

    <!-- 🔁 Пагінація -->
    <div class="mt-6 flex justify-center items-center gap-4">
      <button
        @click="goToPage(currentPage - 1)"
        :disabled="currentPage === 1"
        class="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300 disabled:opacity-50"
      >
        Попередня
      </button>
      <span>Сторінка {{ currentPage }} з {{ totalPages }}</span>
      <button
        @click="goToPage(currentPage + 1)"
        :disabled="currentPage === totalPages"
        class="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300 disabled:opacity-50"
      >
        Наступна
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api/index.js'

const apartments = ref([])
const currentPage = ref(1)
const totalPages = ref(1)

const filters = ref({
  priceFrom: '',
  priceTo: '',
  rooms: '',
  availability: false,
  search: '',
})

async function fetchApartments(page = 1) {
  try {
    const params = {
      page,
      ...(filters.value.priceFrom && { price__gte: filters.value.priceFrom }),
      ...(filters.value.priceTo && { price__lte: filters.value.priceTo }),
      ...(filters.value.rooms && { number_of_rooms: filters.value.rooms }),
      ...(filters.value.availability && { availability: true }),
      ...(filters.value.search && { search: filters.value.search }),
    }

    const response = await api.get('apartments/', { params })
    apartments.value = response.data.results
    currentPage.value = page
    totalPages.value = Math.ceil(response.data.count / 10)
  } catch (err) {
    console.error('❌ Помилка завантаження:', err)
  }
}

function applyFilters() {
  fetchApartments(1)
}

function goToPage(page) {
  if (page >= 1 && page <= totalPages.value) {
    fetchApartments(page)
  }
}

onMounted(() => fetchApartments())
</script>
