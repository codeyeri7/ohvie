<template>
  <section class="page-section" id="contact">
    <v-container>
      <h2 class="page-section-heading text-center mb-0">REVIEW</h2>
      <v-row>
        <v-col>
          <div>
            <label>Movie Title: {{ movie.title }}</label>
          </div>
          <div>
            <label>Review Title</label>
              <v-text-field
                outlined
                v-model.trim="title"
                id="reviewTitle"
                placeholder="Title"
              ></v-text-field>
          </div>
          <div>
            <label>Review Content</label>
              <v-textarea
                v-model.trim="content"
                class="form-control"
                id="content"
                rows="5"
                outlined
                placeholder="Content"
              ></v-textarea>
          </div>
            <label style="margin-right: 15px" for="rank">My Rate</label>
            <div class="select-wrapper" style="margin-right: 15px; margin-bottom:15px">            
              <select name="rate" id="rate" v-model="myMovieRate">
                <option style="color: black;" :value="rate" v-for="(rate, idx) in this.$store.state.reviewRate" :key="idx">{{ rate }}</option>
              </select>
            </div>
          <br />
          <div id="success"></div>
          <v-btn
            class="mx-2"
            fab
            dark
            small
            color="black"
            @click="createReview"
          >
            <v-icon dark>
              mdi-pencil
            </v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
import axios from 'axios'
export default {
  name: "ReviewCreate",
  components: {
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
    createReview: function () {
      const config = this.getToken()
      const reviewItem = {
        title: this.title,
        content: this.content,
        rank: this.myMovieRate,
        movie: this.movie.id,
      }
      console.log(reviewItem)
      if (reviewItem.title) {
        axios.post(`http://127.0.0.1:8000/community/${this.movie.id}/review_list_create/`, reviewItem, config)
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

</style>