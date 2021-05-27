<template>
  <v-app>
    <v-dialog
      v-model="dialog"
      width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-card
          :loading="loading"
          class="card scale mx-auto"
          style="width: 20rem;"
          max-width="374"
        >
          <v-img
            class="align-center"
            height="500"
            :src="imageUrlMain"
            v-bind="attrs"
            v-on="on"
          ></v-img>
        </v-card>
      </template>
    <!-- modal -->
    <v-card :id="`movie-${movieId}`">
      <v-card-title class="headline grey lighten-2">
        <h3 class="text-center">{{ movie.title }}</h3>
      </v-card-title>
        <v-card-text>
          <img :src="imageUrlDetail">
          <hr>
          <h5 style="margin-bottom:10px" class="title-font">영화 제목 : {{ movie.title }}</h5>
          <h5 style="margin-bottom:10px" class="content-font">평점 : {{ movie.vote_average }}점</h5>
          <h5 style="margin-bottom:10px" class="content-font">개봉 일자 : {{ movie.release_date }}</h5>
          <hr>
          <span v-if="movie.overview">{{ movie.overview }}</span>
          <span v-else>해당 영화의 overview는 비어있습니다.</span>
          <hr>
          <strong>[더 보고 싶은 영화]</strong>
          <hr>
          {{ movie.recommend }}
          <hr>
          <strong>[이 영화의 원작 소설]</strong>
          <hr>
          {{ movie.book_title }}
          <hr>
          <a v-bind:href="movie.book_link">책 좀 사볼까? [HERE]</a>
        </v-card-text>
        <v-divider></v-divider>
        <MovieReview 
          :movie="movie"
        />
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
import MovieReview from '@/components/movies/MovieReview'
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"

export default {
  name: 'MovieCard',
  components: {
    MovieReview
  },
  props: {
    movie: Object,
  },
  data() {
    return {
      show: false,
      imageUrlMain: "https://image.tmdb.org/t/p/w500" + this.movie.poster_path,
      imageUrlDetail: "https://image.tmdb.org/t/p/w300" + this.movie.poster_path,
      movieId: this.movie.id,
      dialog: false,
      reviews: [],
      me: [],
      liking: '',
      numLike: '',
      rating: Number(this.movie.vote_average),
    }
  },
  methods: {
    modalHandler: function () {
      this.is_show = !this.is_show;
    },
    movieDetail: function () {
      this.show = true
    },
    ratingToInt: function () {
      this.rating = Math.ceil(this.rating / 2)
    },
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getMyName: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      // console.log(VueJwtDecode.decode(hash))
      const info = VueJwtDecode.decode(hash)
      axios.post(`http:127.0.0.1:8000/accounts/myprofile/`, info, config)
      .then( (res) => {
        // console.log(res.data)
        this.me = res.data
        // console.log(this.me)
        if (this.me.like_movies.includes(this.movie.id)) {
          this.liking = true
        } else {
          this.liking = false
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    like: function () {
      const config = this.getToken()
      const item = {
        myId: this.me.id,
        movieId: this.movie.id,
      }
      axios.post(`http:127.0.0.1:8000/movies/${this.me.id}/${this.movie.title}/like/`, item, config)
      .then( () => {
        this.getMyName()
        this.check()
        // console.log(res)
      })
    },
    number: function () {
      this.numLike = this.movie.like_users.length
      // console.log(this.rating)
    },
    check: function () {
      if (this.liking) {
        this.numLike -= 1
      } else {
        this.numLike += 1
      }
    }
  },
  computed: {
    isLiking: function () {
      return this.liking
    },
  },
  created: function () {
    this.getMyName()
    this.number()
    this.ratingToInt()
  },
}
</script>

<style>
</style>