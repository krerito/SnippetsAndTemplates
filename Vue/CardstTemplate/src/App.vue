<template>
  <v-app>
    <app-header
    @update-header-height="updateHeaderHeight"></app-header>
    <router-view
    :style="{ 'margin-top': headerHeight }"></router-view>
  </v-app>
</template>
<script>
import AppHeader from '@/components/AppHeader.vue'
export default {
  components: {
    AppHeader
  },
  data() {
    return {
      headerHeight: '0px'
    }
  },
  methods: {
    updateHeaderHeight(newHeight) {
      this.headerHeight = newHeight;
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
