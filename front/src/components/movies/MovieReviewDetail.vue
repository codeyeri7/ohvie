<template>
  <div>
    <v-row>
      <v-col>
        <div>
          <h4 class="title-font">Review Title | {{ review.title }}</h4>
          <h5 class="content-font">Wrtier | {{ review.userName }}</h5>
          <h5 class="content-font">Review Content | {{ review.content }}</h5>
          <h5 class="st-font">Rate | {{ review.rank }}point</h5>
          <v-dialog v-model="dialog" width="500">
            <template v-slot:activator="{ on, attrs }">
              <v-btn v-bind="attrs" v-on="on" tile x-small color="success">
                <v-icon left>
                  mdi-pencil
                </v-icon>
                Edit
              </v-btn>
              <v-btn @click="deleteReview(review)" x-small color="error" dark>DELETE</v-btn>
            </template>
            <v-container>
            <h2 class="page-section-heading text-center mb-0">REVIEW UPDATE</h2>
            <v-row>
              <v-col>
                <div>
                  <label>Review Title:</label>
                  <input v-model.trim="title" class="form-control" type="text" :placeholder="review.title" required="required" />
                </div>
                <div>
                  <label>Movie Title</label>
                  <v-text-fields label="Outlined">{{ movie.title }}</v-text-fields>                  
                </div>
                <label style="margin-right: 15px" for="rank">My Rate</label>
                <div class="select-wrapper" style="margin-right: 15px">            
                  <select name="rate" id="rate" v-model="myMovieRate2" class="content-font">
                    <option class="content-font" style="color:black" :value="rate" v-for="(rate, idx) in this.$store.state.reviewRate" :key="idx">{{ rate }}</option>
                  </select>
                </div>
                <div>
                  <label>Review Content</label>
                  <v-textarea v-model.trim="content" outlined class="form-control" id="content" rows="5" :placeholder="review.content" required="required"></v-textarea>
                </div>
                <br />
                <div id="success"></div>
                <v-btn @click="update(review)" x-small color="success" dark>EDIT !</v-btn>
              </v-col>
            </v-row>
            <div>
              <v-btn color="primary" text @click="dialog = false">close</v-btn>
            </div>
            </v-container>
          </v-dialog>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "MovieReviewDetail",
  props: {
    review: {
      type: Object
    },
    movie: {
      type: Object
    },
  },
  data: function () {
    return {
      dialog: false,
      comment_content: '',
      comments: [],
      myMovieRate: 0,
      title: '',
      content: '',
      myMovieRate2: 0,
      show: false,
    }
  },
  methods: {
    close: function () {
      this.show = false
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
    deleteReview: function (review) {
      const config = this.getToken()
      axios.delete(`http://127.0.0.1:8000/community/review/${review.id}/`, config)
        .then((res) => {
          // console.log(res)
          if (res.data.message) {
            alert("본인이 작성한 글만 삭제 가능합니다!")
          }
          else {
            this.$emit('deleteReview')
          }
        })
    },
    update: function (review) {
      const config = this.getToken()
      const reviewItem = {
        title: this.title,
        content: this.content,
        rank: this.myMovieRate2,
        movie: review.movie,
      }
      axios.put(`http://127.0.0.1:8000/community/review/${review.id}/`, reviewItem, config)
      .then( (res) => {
        if (res.data.message) {
          alert("본인이 작성한 글만 수정 가능합니다!")
        }
        else {
          this.close()
          this.$emit("reviews-updated")
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    }
  },
  computed: {
    commentsList: function () {
      return this.comments
    },
  },
  created: function () {
    // this.getMyName()
    this.getComments()
  }
  
}
</script>

<style>
</style>