<template>
  <div>
    <h1>Movie Detail</h1>
    {{ eachMovie }}
    <h2>why!!</h2>
    <!-- <h2>{{ movieId }}</h2> -->
    <MovieInfo />
  </div>
</template>

<script>
import MovieInfo from '../../components/movies/MovieInfo.vue'
// import { mapActions } from 'vuex'
import { mapState, mapActions } from 'vuex'



export default {
  name: 'MovieDetail',
  components: {
    MovieInfo,
  },
  created() {
      console.log(this.$store.state.eachMovie)
      console.log('created')
  },
  mounted() {
    console.log(this.$store.state.eachMovie)
    console.log('mounted')
  },
  updated() {
    console.log(this.$store.state.eachMovie)
    console.log('updated')
  },
  // Main에서 받아온 개별 데이터를 쏜다
  props: {
    movie: Object
  },
  methods: {
    ...mapActions(['selectMovie']),
      // this.fetchAllMovies()
  },
  computed: {
    ...mapState(['eachMovie'])
  },


}
</script>

<style>

</style>