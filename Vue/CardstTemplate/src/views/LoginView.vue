<template>
  <img src="" alt="">
  <div class="d-flex align-center justify-center" style="height: 100vh">
    <v-sheet width="400" class="mx-auto">
      <v-form fast-fail @submit.prevent="login">
        <v-text-field v-model="username" label="User Name"></v-text-field>
        <v-text-field v-model="password" label="password"></v-text-field>
        <v-btn type="submit" color="primary" block class="mt-2">Sign in</v-btn>
      </v-form>
    </v-sheet>
  </div>
</template>
<script>
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      const correctUsername = 'kerim';
      const correctPassword = 'atem11';

      if (this.username === correctUsername && this.password === correctPassword) {
        alert('Inicio de sesión exitoso. Bienvenido!');
        this.$router.push('/')
      } else {
        alert('Nombre de usuario o contraseña incorrectos. Por favor, intente de nuevo.');
      }

    },
  },
}
</script>