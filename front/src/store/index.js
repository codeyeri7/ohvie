import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import router from '../router'
import DRF from '@/api/drf'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    allMovies: [],
    eachMovie: {},
    articles: [],
    reviewRate: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  },
  mutations: {
    SET_ALLVIDEOS: (state, movies) => { state.allMovies = movies},
    SET_EACH_MOVIE: (state, movie) => { state.eachMovie = movie },
    CREATE_Detail_Article(state, article) {
      state.articles.push(article)
    },
    CREATE_REVIEW(state, review) {
      state.review.push(review)
    }
  },
  actions: {
    fetchAllMovies({commit}) {
      const URL = 'http://127.0.0.1:8000/movies/'
      axios.get(URL)
      .then(res => commit('SET_ALLVIDEOS', res.data))
      .catch(err => console.error(err))
    },
    fetchReviews({ commit }) {
      axios.get(DRF.URL + DRF.ROUTES.reviews)
        .then(res => commit('SET_REVIEWS', res.data))
        .catch(err => console.error(err))
    },
    createDetatilArticle({ commit }, article) {
      commit('CREATE_Detail_Article',  article)
    },
    createReview({ commit }, review) {
      commit('CREATE_REVIEW', review)
    }
  },
  modules: {
  }
})