<template>
  <v-container>
    <v-row>
      <MovieCard v-for="(movie, idx) in allMovies" :key='idx' :movie='movie' class='col-12 col-md-6 col-lg-3'/>
    </v-row>
  </v-container>
</template>

<script>
import MovieCard from '../../components/movies/MovieCard.vue'
import { mapActions, mapState } from 'vuex'

export default {
  name : 'Main',
  components: { MovieCard,},
  methods: {
    ...mapActions(['fetchAllMovies',]),
  },
  computed: {
    ...mapState(['allMovies'])
  }
}
</script>

<style>

</style>