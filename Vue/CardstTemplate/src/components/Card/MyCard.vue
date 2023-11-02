<template>
  <v-card class="mx-auto" max-width="344">
    <v-img :src="card.image" height="200px" cover></v-img>

    <v-card-title>
      {{ card.title }}
    </v-card-title>

    <v-card-subtitle>
      {{ card.subtitle }}
    </v-card-subtitle>

    <v-card-actions>
      <v-btn :color="card.buttonColor" variant="text" @click="handleButtonClick">
        {{ card.buttonText }}
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="show = !show"></v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          {{ card.text }}
        </v-card-text>
      </div>
    </v-expand-transition>

    <!-- Diálogo para mostrar el mensaje -->
    <v-dialog v-model="dialogVisible" max-width="600px">
      <v-card>
        <v-card-title>Aun desarrollando</v-card-title>
        <v-card-text>
          <img :src="catImage" alt="Gatito" class="dialog-cat-image">
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialogVisible = false">Cerrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Diálogo de confirmación para la tarjeta con id 7 -->
    <v-dialog v-model="confirmDialogVisible" max-width="600px" persistent>
      <v-card>
        <v-card-title>Advertencia</v-card-title>
        <v-card-text>
          ATENCIÓN: Este script cerrará las aplicaciones de Office 365 y OneDrive. ¿Estás seguro de que deseas continuar?
        </v-card-text>
        <v-card-actions>
          <v-btn color="green" @click="proceedWithDownload">Sí, continuar</v-btn>
          <v-btn color="red" @click="confirmDialogVisible = false">Cancelar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
export default {
  methods: {
    handleButtonClick() {
      if (this.card.id === 7) {
        this.confirmDialogVisible = true;
      } else if (this.card.downloadLink) {
        window.location.href = this.card.downloadLink;
      } else if (this.card.onwork === true) {
        this.dialogVisible = true;
      }
    },
    proceedWithDownload() {
      this.confirmDialogVisible = false;
      window.location.href = this.card.downloadLink;
    }
  },
  props: ['card'],
  data: () => ({
    show: false,
    dialogVisible: false,
    confirmDialogVisible: false, // Nueva variable reactiva para el diálogo de confirmación
    catImage: "/images/cat.jpg"
  }),
}
</script>
