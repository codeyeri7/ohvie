<template>
  <div>
    <ReviewCreate 
      @reviews-updated="reviewsUpdated"
      :movie="movie"
      style="margin-bottom:30px"
    />
    <ReviewList 
      :reviews="reviews"
      :movie="movie"
      @deleteReview="getReviews"
      @reviews-updated="reviewsUpdated"
    />
  </div>
</template>

<script>
import ReviewList from '@/components/movies/ReviewList'
import ReviewCreate from '@/components/movies/ReviewCreate.vue'
import axios from 'axios'

export default {
  name: 'Review',
  components: {
    ReviewCreate,
    ReviewList,
  },
  props: {
    movie: {
      type: Object,
    }
  },
  data: function () {
    return {
      reviews: [],
    }
  }, 
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getReviews: function () {
      const config = this.getToken()
      axios.get(`http://127.0.0.1:8000/community/${this.movie.id}/review_list_create/`, config)
      .then((res) => {
        // console.log(res)
        this.reviews = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    reviewsUpdated: function () {
      this.getReviews()
    },
  },
  created: function () {
    this.getReviews()
  },
}
</script>

<style>
</style>