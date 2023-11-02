<script>
export default {
  data() {
    return {
      headerHeight: '7%'
    };
  
  },
  mounted() {
    this.$emit('update-header-height', '7%'); 
  },
  methods: {
    goToLink() {
      //this.$router.push('/ruta')
      //primero definimos en nuestro index la ruta Atem
      this.$router.push('/Atem')
    }
  }
};
</script>
<template>
  <v-app-bar
    app
    :style="{ height: headerHeight, backgroundColor: '#255672' }"
  >
    <v-btn
      icon
      @click="goToLink"
    >
      <v-icon color="white">mdi-arrow-left</v-icon>
    </v-btn>

    <v-spacer></v-spacer>

    <div style="color: white;">
      <h2>
        Atematic Solutions
      </h2>
    </div>
    <v-spacer></v-spacer>
  </v-app-bar>
</template>
