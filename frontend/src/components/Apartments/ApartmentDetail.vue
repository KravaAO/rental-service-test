<template>
  <div class="p-6" v-if="apartment">
    <h1 class="text-2xl font-bold mb-4">{{ apartment.name }}</h1>
    <p><strong>Власник:</strong> {{ apartment.owner }}</p>
    <p><strong>Ціна:</strong> {{ apartment.price }} грн</p>
    <p><strong>Кімнат:</strong> {{ apartment.number_of_rooms }}</p>
    <p><strong>Площа:</strong> {{ apartment.square }} м²</p>
    <p :class="apartment.availability ? 'text-green-600' : 'text-red-600'">
      {{ apartment.availability ? 'Доступна' : 'Недоступна' }}
    </p>

    <button
      v-if="isOwner"
      @click="deleteApartment"
      class="mt-4 px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
    >
      Видалити
    </button>
    <router-link
      v-if="isOwner"
      :to="`/apartments/${apartment.slug}/edit`"
      class="ml-4 px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600"
    >
      Редагувати
    </router-link>
  </div>

  <div v-else class="p-6">Завантаження...</div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/index.js'

const apartment = ref(null)
const route = useRoute()
const router = useRouter()

const username = localStorage.getItem('username')

const isOwner = computed(() => apartment.value?.owner === username)

const deleteApartment = async () => {
  if (!confirm('Ви впевнені, що хочете видалити цю квартиру?')) return
  try {
    await api.delete(`apartments/${route.params.slug}/`)
    alert('Квартиру видалено успішно.')
    router.push('/')
  } catch (error) {
    console.error('Помилка видалення:', error)
    alert('Не вдалося видалити квартиру.')
  }
}

onMounted(async () => {
  try {
    const slug = route.params.slug
    const response = await api.get(`apartments/${slug}/`)
    apartment.value = response.data
  } catch (error) {
    console.error('Помилка завантаження квартири:', error)
  }
})
</script>

