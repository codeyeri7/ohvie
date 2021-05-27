<template>
  <div>
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <div class="post-preview" style="cursor:pointer;">
            <h4 class="title-font">리뷰 제목 | {{ review.title }}</h4>
            <h5 class="content-font">작성자 | {{ review.userName }}</h5>
            <h5 class="content-font">리뷰 내용 | {{ review.content }}</h5>
            <h5 class="st-font">남긴 평점 | {{ review.rank }}점</h5>
            <v-dialog
              v-model="dialog"
              width="500">
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  color="primary"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                  수정
                </v-btn>
                <v-btn
                  @click="deleteReview(review)"
                  color="primary"
                  dark
                >
                  삭제
                </v-btn>
              </template>
              <v-container>
              <!-- Contact Section Heading-->
              <h2 class="title-font page-section-heading text-center text-uppercase text-white mb-0">리뷰 수정</h2>
              <!-- Contact Section Form-->
              <v-row>
                <v-col>
                  <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                      <label>리뷰 제목:</label>
                      <input v-model.trim="title" class="form-control" id="reviewTitle" type="text" :placeholder="review.title" required="required" />
                      <p class="help-block text-danger"></p>
                  </div>
                  <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                      <label>영화 제목: {{ movie.title }}</label>
                      <!-- <p class="help-block text-danger"></p> -->
                  </div>
                  <label style="margin-right: 15px" class="st-font" for="rank">내가 생각하는 영화 평점</label>
                  <div class="select-wrapper" style="margin-right: 15px">            
                    <select name="rate" id="rate" v-model="myMovieRate2" class="content-font">
                      <option class="content-font" style="color:black" :value="rate" v-for="(rate, idx) in this.$store.state.reviewRate" :key="idx">{{ rate }}</option>
                    </select>
                  </div>
                  <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                    <label>리뷰 내용</label>
                    <textarea v-model.trim="content" class="form-control" id="content" rows="5" :placeholder="review.content" required="required"></textarea>
                    <p class="help-block text-danger"></p>
                  </div>
                  <br />
                  <div id="success"></div>
                  <div class="text-white st-font form-group"><button @click="update(review)" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">수정 !</button></div>
                </v-col>
              </v-row>
              <div class="text-white st-font form-group">
                <v-btn
                  color="primary"
                  text
                  @click="dialog = false"
                >
                  close
                </v-btn></div>
                <!-- <button @click="close" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">창 닫기</button> -->
              </v-container>
            </v-dialog>
          </div>
            <!-- <button @click="updateReview(review)" type="button" class="st-font btn btn-secondary text-white" style="margin-right:10px">수정</button> -->
            <!-- <button @click="deleteReview(review)" type="button" class="st-font btn btn-secondary text-white" style="margin-right:10px">삭제</button> -->
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios'
// import VueJwtDecode from "vue-jwt-decode"
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
      show: false,
      // variants: ["light", "dark"],
      comment_content: '',
      comments: [],
      myMovieRate: 0,
      title: '',
      content: '',
      myMovieRate2: 0,
    }
  },
  methods: {
    updateReview: function () {
      this.show = true
    },
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
#reviewComment {
  color: darkslategray !important
}
#myImg {
  display: block;
  margin: 0px auto;
}
#reviewBtn {
  margin-left: 60px;
  padding: 1px;
  color: white;
  border: 2px solid darkkhaki;
}
</style>