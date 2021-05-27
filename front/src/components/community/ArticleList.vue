<template>
  <div>
    <v-container>
      <h2 class="text-center" style="margin-bottom:30px">Community</h2>
      <v-row>
        <v-col>
          <div class="post-preview" v-for="(article, idx) in articles" :key="idx">
            <h3 @click="DetailArticle(article)">{{article.id}}번 글</h3>
            <h2 @click="DetailArticle(article)">
              {{ article.title }}
            </h2>
            <h4 class="content-font">
              {{ article.content }}
            </h4>
            <p>
              {{ article.userName }}
            </p>
          <hr>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'ArticleList',
  data: function () {
    return {
      articles: null,
    }
  },
  methods: {
    DetailArticle: function (article) {
      this.$router.push({ name: 'ArticleDetail', params: { article_pk: `${article.id}` }})
    },  
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getArticles: function() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/articles/',
        headers: this.getToken()
      })
        .then((res) => {
          console.log(res)
          this.articles = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getArticles()
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style>
</style>