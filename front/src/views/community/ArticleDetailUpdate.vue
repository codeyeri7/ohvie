<template>
  <div>
      <v-container>
        <h2 class="text-center mb-0">Detail Update</h2>
        <v-row>
          <v-col>
              <div>
                <label>Title</label>
                <v-text-field v-model.trim="article.title" placeholder="Title" required="required"></v-text-field>
              </div>
              <div>
                <label>Content</label>
                <v-text-field v-model.trim="article.content" rows="5" placeholder="Content" required="required"></v-text-field>
              </div>
            <br />
            <div id="success"></div>
            <v-btn @click="articleDetailUpdate(article)" x-small color="primary" dark>Update</v-btn>
          </v-col>
        </v-row>
      </v-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ArticleDetailUpdate',
  props: {
    article_pk: Number,
  },
  data: function () {
    return {
      article: [],
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
    getArticle: function () {
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
    articleDetailUpdate: function (article) {
    const config = this.getToken()
    const article_pk = this.$route.params.article_pk
    const articleItem = {
      title: article.title,
      content: article.content
    }
    axios.put(`http://127.0.0.1:8000/community/article/${article_pk}/`, articleItem, config)
      .then((res) => {
        if (res.data.message) {
            alert("본인이 작성한 글만 수정 가능합니다!")
        }
        else {
            this.$router.push({ name: 'ArticleDetail', params: { article_pk: `${article_pk}` }})
        }
      })
      .catch((err) => {
          console.log(err)
      })
    },        
  },
  created: function () {
    this.getCommunity()
  }    
}
</script>

<style>
</style>