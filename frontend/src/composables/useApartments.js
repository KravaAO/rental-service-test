import { ref } from 'vue'
import api from '../api'

export function useApartments() {
  const apartments = ref([])
  const fetchApartments = async () => {
    const res = await api.get('apartments/')
    apartments.value = res.data.results || res.data
  }
  return { apartments, fetchApartments }
}
