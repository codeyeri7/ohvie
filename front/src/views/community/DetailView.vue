<template>
  <div>
    <v-container>
      <h3>{{article.userName}}님의 게시글</h3>
      <hr>
      <div style="margin-bottom:30px">
        <span style="cursor:pointer;">작성자: {{ article.userName }} | </span>  
        <span>글 생성시간: {{ article.created_at }} | </span>
        <span>글 수정시간: {{ article.updated_at }}</span>  
      </div>
      <div>
        <p>제목: {{ article.title }}</p>
        <p>내용: {{ article.content }}</p>
      </div>
      <v-container>
        <v-col justify-center>
          <v-btn 
            @click="moveToDetailUpdate(article)"
            tile 
            x-small 
            color="success"
          >
            <v-icon left>
              mdi-pencil
            </v-icon>
              Edit
            </v-btn>
          <v-btn @click="deleteArticle(article)" x-small color="error" dark>DELETE</v-btn>
        </v-col>
      </v-container>
    </v-container>
    <br>
    <section class="page-section" id="contact">
      <v-container>
        <v-row>
          <v-col>
            <p>댓글 작성</p>
            <v-text-field v-model.trim="comment_content" rows="5" placeholder="Comment" required="required"></v-text-field>
            <hr>
            <v-btn @click="createComment" x-small color="success" dark>COMMENT</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </section>
    <br>
    <v-container v-for="(comment, idx) in commentsList" :key="idx">
      <v-row>
        <v-col>
          <div>
              <b style="cursor:pointer;">{{comment.userName}}</b>
              님의 댓글
          </div>
          <h6 class="text-muted time">{{comment.created_at}}</h6>
          <div> 
              <p>{{comment.content}}</p>
          </div>
          <v-btn @click="deleteComment(article, comment)" x-small color="error" dark>DELETE</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"

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
      axios.get(`http://127.0.0.1:8000/community/detail/${article_pk}/`, config)
        .then((res) => {
          this.article = res.data
        })
        .catch((err) => {
          console.log(err)
        })    
    },
    getMyName: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`http://127.0.0.1:8000/accounts/myprofile/`, info, config)
      .then( (res) => {
        this.user = res.data
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
</style>