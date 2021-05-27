<template>
  <section class="page-section" id="contact">
    <v-container>
      <h2 class="page-section-heading text-center text-uppercase text-white mb-0 title-font">REVIEW</h2>
      <v-row>
        <v-col>
          <div class="control-group">
            <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
              <label>Review Title</label>
                <v-text-field
                  label="Review Title"
                  single-line
                  solo
                  v-model.trim="title"
                  class="form-control"
                  id="reviewTitle"
                ></v-text-field>
                  <!-- <p class="help-block text-danger"></p> -->
            </div>
          </div>
          <div class="control-group">
            <div class="content-font form-group floating-label-form-group controls mb-0 pb-2">
              <label>Movie Title: {{ movie.title }}</label>
            </div>
          </div>
          <label style="margin-right: 15px" class="content-font" for="rank">내가 생각하는 영화 평점</label>
          <!-- <div class="select-wrapper" style="margin-right: 15px; margin-bottom:15px">             -->
            <StarRating v-bind:increment="0.5"
              v-bind:max-rating="10"
              v-bind:star-size="40"
              v-bind:active-on-click="true"/>
            <!-- <select name="rate" id="rate" v-model="myMovieRate" class="content-font">
              <option style="color: black;" class="content-font" :value="rate" v-for="(rate, idx) in this.$store.state.reviewRate" :key="idx">{{ rate }}</option>
            </select> -->
          <!-- </div> -->
          <div class="control-group">
            <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
              <label>리뷰 내용</label>
                <v-textarea
                  v-model.trim="content"
                  class="form-control"
                  id="content"
                  rows="5"
                  placeholder="Content"
                ></v-textarea>
                  <p class="help-block text-danger"></p>
            </div>
          </div>
          <br />
          <div id="success"></div>
          <div class="text-white st-font form-group"><button @click="createReview" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">작성 !</button></div>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'

export default {
  name: "ReviewCreate",
  components: {
    StarRating
  },
  props: {
    movie: {
      type: Object
    },
  },
  data: function () {
    return {
      title: '',
      content: '',
      myMovieRate: 0,
      rating: 0,
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
    setRating: function(rating){
      this.rating= rating;
    },
    createReview: function () {
      const config = this.getToken()
      const reviewItem = {
        title: this.title,
        content: this.content,
        rank: this.rating,
        movie: this.movie.id,
      }
      console.log(reviewItem)
      if (reviewItem.title) {
        axios.post(`http:127.0.0.1:8000/community/${this.movie.id}/review_list_create/`, reviewItem, config)
          .then(() => {
            this.$emit('reviews-updated')
            this.title = ""
            this.rank = 0
            this.content = ""
          })
          .catch((err) => {
            console.log(err)
          })
      } 
    },
  },
  created: function () {
  },
}
</script>

<style>
/* #reviewTitle {
  color: white;
  border: 2px solid white;
} */
#reviewRate {
  color: white;
}
#reviewContent {
  color: white;
  border: 2px solid white;
}
#movieRate {
  color: white;
}
</style>