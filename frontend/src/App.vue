<template>
  <Header />
  <router-view />
  <Footer />
</template>

<script setup>
console.log('App.vue loaded');
import Header from './components/layout/Header.vue'
import Footer from './components/layout/Footer.vue'

</script>
