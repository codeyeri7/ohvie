<template>
  <div>
    <div class="container">
      <div>
        <h2 class="title-font">{{article.userName}}님의 게시글</h2>
        <hr>
        <div class="st-font" style="margin-bottom:30px">
          <span style="cursor:pointer;">작성자: {{ article.userName }} | </span>  
          <span>글 생성시간: {{ article.created_at }} | </span>
          <span>글 수정시간: {{ article.updated_at }}</span>  
        </div>
        <div>
          <p class="title-font" style="font-size: 40px">제목: {{ article.title }}</p>
          <p class="content-font" style="font-size: 50px">내용: {{ article.content }}</p>
        </div>
      </div>
      <button @click="moveToDetailUpdate(article)" type="button" class="st-font btn btn-secondary text-white" style="margin-right:10px">수정</button>
      <button @click="deleteArticle(article)" type="button" class="st-font btn btn-secondary text-white" style="margin-right:10px">삭제</button>
    </div>
    <br>
    <section class="page-section" id="contact">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 mx-auto">
                  <div class="control-group">
                      <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                          <label>댓글 작성</label>
                          <textarea v-model.trim="comment_content" style="font-size: 30px" class="form-control" id="content" rows="5" placeholder="Comment" required="required" data-validation-required-message="Please writer a comment."></textarea>
                          <p class="help-block text-danger"></p>
                      </div>
                  </div>
                  <div id="success"></div>
                  <div class="text-white st-font form-group" style="font-weight"><button @click="createComment" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">댓글 작성</button></div>
                </div>
            </div>
        </div>
    </section>
    <br>
    <div class="container" v-for="(comment, idx) in commentsList" :key="idx">
        <div class="row">
            <div class="col-8">
                <div class="card card-white post">
                    <div class="post-heading">
                        <div class="float-left meta">
                            <div class="title h5 st-font">
                                <b style="cursor:pointer;">{{comment.userName}}</b>
                                님이 댓글을 작성하셨습니다.
                            </div>
                            <h6 class="title-font text-muted time">{{comment.created_at}}</h6>
                        </div>
                    </div> 
                    <div style="font-size:30px" class="content-font post-description"> 
                        <p>{{comment.content}}</p>
                    </div>
                <button class="st-font button1" style="cursor:pointer;" @click="deleteComment(article, comment)">삭제</button>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"
// const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'DetailView',
  props: {
    article_pk: Number,
  },
  data: function () {
    return {
      article: [],
      comment_content: '',
      comments: [],
      user: [],
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
    getArticles: function () {
      const config = this.getToken()
      const article_pk = this.$route.params.article_pk
      // 장고 서버에 get 요청을 보내 전체 게시글 데이터를 가져온다.
      axios.get(`http://127.0.0.1:8000/community/detail/${article_pk}/`, config)
        .then((res) => {
          // console.log(res)
          this.article = res.data
        })
        .catch((err) => {
          console.log(err)
        })    
    },
    // getMyName: function () {
    //   this.user = res.data
    // },
    getMyName: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`http://127.0.0.1:8000/accounts/myprofile/`, info, config)
      .then( (res) => {
        this.user = res.data
        // console.log(this.user)
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    getComments: function () {
      const config = this.getToken()
      const article_pk = this.$route.params.article_pk
      axios.get(`http://127.0.0.1:8000/community/comments/${article_pk}`, config)
        .then((res) => {
          this.comments = res.data
          // console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createComment: function () {
      const config = this.getToken()
      const commentItem = {
        content: this.comment_content,
      }
      if (commentItem.content) {
        axios.post(`http://127.0.0.1:8000/community/${this.article.id}/comment/`, commentItem, config)
          .then( () => {
            // console.log(res)
          this.getComments()
          this.comment_content = ''
          })
        }
    },
    deleteArticle: function (article) {
      const config = this.getToken()
      axios.delete(`http://127.0.0.1:8000/community/article/${article.id}/`, config)
        .then((res) => {
          // console.log(res)
          if (res.data.message) {
            alert("본인이 작성한 글만 삭제 가능합니다!")
          }
          else {
            this.$router.push({ name: 'ArticleList' })
          }
        })
    },
    deleteComment: function (article, comment) {
      const config = this.getToken()
      axios.delete(`http://127.0.0.1:8000/community/comment/${article.id}/${comment.id}/`, config)
        .then((res) => {
          // console.log(res)
          if (res.data.message) {
            alert("본인이 작성한 댓글만 삭제 가능합니다!")
          }
          else {
            this.getComments()
          }
        })
    },
     moveToDetailUpdate: function (article) {
      console.log(this.user)
      if (this.user.username === article.userName) {
        console.log(article.id)
        this.$router.push({ name: 'ArticleUpdate', params: { article_pk: `${article.id}` }})
      } else {
        alert("본인이 작성한 글만 수정 가능합니다!")
      }
      
    },
    // moveToDetailUpdate: function (article) {
    //   const config = this.getToken()
    //   axios.put(`http://127.0.0.1:8000/community/article/${article.id}/`, config)
    //   .then((res) => {
    //     if (res.data.message) {
    //       this.$router.push({ name: 'ArticleUpdate', params: { article_pk: `${article.id}` }})
    //     } else {
    //       alert("본인이 작성한 글만 수정 가능합니다!")
    //     }
    //   })
    // },
    // moveToProfile: function (article) {
    //   // console.log(community.userName)
    //   this.$router.push({ name: "Profile", params: { user_pk: `${article.user}`, username: `${article.userName}` }})
    // },   
  },
  computed: {
    commentsList: function () {
      return this.comments
    }
  },
  created: function () {
    this.getArticles()
    this.getComments()
    this.getMyName()
  }
}
</script>

<style>
/* .button1 {
  background-color: white;
  color: black;
  border: 2px solid #050505;
}
.button5 {background-color: #555555;} */
</style>