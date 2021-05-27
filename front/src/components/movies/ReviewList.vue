<template>
  <div>
    <h2 class="text-center" style="margin-bottom:30px">Review List</h2>   
    <ul>
      <div style="cursor:pointer;" v-for="(review, idx) in reviews" :key="idx">
        <MovieReviewDetail 
          :review="review"
          :movie="movie"
          @deleteReview="deleteReview"
          @reviews-updated="updateRiview"
        />
        <hr>
      </div>
    </ul>
  </div>
</template>

<script>
import MovieReviewDetail from '@/components/movies/MovieReviewDetail'

export default {
  name: "ReviewList",
  components: {
    MovieReviewDetail,
  },
  props: {
    reviews: {
      type: [Array, Object],
    },
    movie: {
      type: Object,
    },
  },
  data: function () {
    return {
    }
  },
  methods: {
    deleteReview: function () {
      this.$emit('deleteReview')
    },
    updateRiview: function () {
      this.$emit('reviews-updated')
    }
  },
}
</script>

<style>
</style>