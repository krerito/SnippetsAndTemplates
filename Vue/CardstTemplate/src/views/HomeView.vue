<template>
    <v-row>
      <v-col cols="12" sm="6" md="4" lg="3" v-for="(group, index) in groupedCards" :key="index">
        <v-row>
          <v-col cols="12" v-for="item in group" :key="item.id">
            <my-card :card="item"></my-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
</template>

<script>
import MyCard from '../components/Card/MyCard.vue';
import { cards } from '../components/Card/cardData.js';

export default {
  components: {
    MyCard
  },
  data() {
    return {
      cards: cards,
    };
  },
  computed: {
    groupedCards() {
      const grouped = [];
      for (let i = 0; i < this.cards.length; i += 2) {
        grouped.push(this.cards.slice(i, i + 2));
      }
      return grouped;
    }
  }
};
</script>

<style scoped>
.v-row{
  justify-content: center;
}
</style>