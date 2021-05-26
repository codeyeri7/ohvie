import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import router from '../router'
import DRF from '@/api/drf'


Vue.use(Vuex)

// API_KEY = 'f4e4ad237c7fb44ea8e4abb88193fa30'

export default new Vuex.Store({
  state: {
    allMovies: [],
    eachMovie: {},
    reviews: [],
  },
  getters: {
    reviews(state) {
      return state.reviews
    }
  //   imageUrl: (state) => "https://image.tmdb.org/t/p/w500" + state.eachMovie,
  },

  mutations: {
    SET_ALLVIDEOS: (state, movies) => { state.allMovies = movies},
    SET_EACH_MOVIE: (state, movie) => { state.eachMovie = movie },
    SET_REVIEWS: (state, reviews) => state.reviews = reviews
  },
  actions: {
    fetchAllMovies({commit}) {
      const URL = 'http://127.0.0.1:8000/movies/'
      axios.get(URL)
      .then(res => commit('SET_ALLVIDEOS', res.data))
      .catch(err => console.error(err))
    },
    selectMovie({ commit }, movieId) {
      const URL = 'http://127.0.0.1:8000/movies/' + movieId +'/'
      console.log('axios 보내기전')
      axios.get(URL)
      .then(res => {
        commit('SET_EACH_MOVIE', res.data)
        console.log('반환러ㅑ햐허')
      }) 
    },
    fetchReviews({ commit }) {
      axios.get(DRF.URL + DRF.ROUTES.reviews)
        .then(res => commit('SET_REVIEWS', res.data))
        .catch(err => console.error(err))
    },
  //   createReview ({ getters }, reviewData) {
  //     axios.post(DRF.URL + DRF.ROUTES.reviews, reviewData, getters.config)
  //       .then(() => router.push({ name: 'ReviewList' }))
  //       .catch(err => console.error(err))
  // }
  },
  modules: {
  }
})