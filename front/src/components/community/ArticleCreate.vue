<!--<template>
  <v-container>
    <v-card elevation="10" outlined width="100%" class="mx-auto">
      <v-card-title>
        <span class="mr-2">Create</span>
      </v-card-title>
    </v-card>
    <v-card-text>
      <v-text-field
        label="Title"
        :counter="100"
        v-model="reviewData.title"
      ></v-text-field>
      <v-textarea
        label="Content"
        v-model="reviewData.content"
      ></v-textarea>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        elevation="2"
        rounded
        outlined
        color="black"
        @click="createReview">SAVE</v-btn>
    </v-card-actions>
  </v-container>
</template>

<script>
import axios from'axios'
 

export default {
  name: 'ReviewCreate',
  data() {
    return {
      reviewData: { title: '', content: ''}
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createReview: function () {
      const reviewItem = {
        title: this.reviewData.title,
        content: this.reviewData.content,
      }

      if (reviewItem.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/community/articles/',
          data: reviewItem,
          headers: this.setToken()
        })
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'ArticleList' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  }
}
</script>

<style>

</style>-->

<template>
  <div>
    <section class="page-section" id="contact">
      <div class="container">
        <!-- Contact Section Heading-->
        <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Community</h2>
        <!-- Contact Section Form-->
        <div class="row">
          <div class="col-lg-8 mx-auto">
            <div class="control-group">
              <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                <label>Title</label>
                <input style="font-size: 30px" v-model.trim="title" class="form-control" id="title" type="text" placeholder="Title" required="required" data-validation-required-message="Please enter your title." />
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="control-group">
              <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                <label>Content</label>
                <textarea style="font-size: 30px" v-model.trim="content" class="form-control" id="content" rows="5" placeholder="Content" required="required" data-validation-required-message="Please enter a message."></textarea>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <br />
            <div id="success"></div>
            <div class="text-white st-font form-group"><button @click="createArticle" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">Add</button></div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// community 게시판 게시글 작성을 위한 컴퍼넌트 페이지입니다.
import axios from 'axios'
// const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'ArticleCreate',
  data: function () {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createArticle: function () {
      const articleItem = {
        title: this.title,
        content: this.content,
      }
      if (articleItem.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/community/articles/', 
          data: articleItem, 
          headers: this.getToken()
        })
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'ArticleList' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    //createCommunity 함수가 실행되면 입력된 제목과 콘텐츠 데이터를 params 형태로 만든뒤
    // createArticle: function () {
    //   const config = this.getToken()
    //   const articleItem = {
    //     title: this.title,
    //     content: this.content,
    //   }
    //   if (articleItem.title) {
    //     // axios post 요청을 장고에 데이터와 함께 보내줍니다.
    //     axios.post(`http://127.0.0.1:8000/community/articles/`, articleItem, config)
    //       .then(() => {
    //         this.$emit('articles-updated')
    //         // 때문에 emit을 사용해 글이 작성됐음을 알려주는 이벤트를 보내고
    //         this.title = "" // 사용자경험 향상을 위해 작성한 제목과 내용은 초기화.
    //         this.content = ""
    //       })
    //       .catch((err) => {
    //         console.log(err)
    //       })
    //   } 
    }
  },
}
</script>

<style>
</style>