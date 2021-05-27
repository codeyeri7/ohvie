<template>
  <div>
    <!-- <ArticleCreate @articles-updated="articlesUpdated" style="margin-bottom: 30px"/> -->
    <ArticleList :articles="articles"/>
    <v-btn
        elevation="2"
        rounded
        outlined
        color="black"
        @click="movePage"
      >
      CREATE
    </v-btn>
  </div>
</template>

<script>
import ArticleList from '../../components/community/ArticleList.vue'
// import ArticleCreate from '../../components/community/ArticleCreate.vue'
import axios from 'axios'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
    // ArticleCreate,
  },
  data: function () {
    return {
      articles: [],
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
    getArticles: function () {
      axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/community/articles/',
          headers: this.getToken()
        })
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'ArticleView' })
          })
          .catch((err) => {
            console.log(err)
          })
      // const articleItem = {
      //   article: this.articles
      // }
      // if (articleItem.article) {
        
      // }
      // const config = this.getToken()
      // axios({
      //     method: 'post',
      //     url: 'http://127.0.0.1:8000/community/articles/',
      //     data: ,
      //     headers: this.getToken()
      //   })
      //   .then((res) => {
      //     this.articles = res.data
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   })
    },
    articlesUpdated: function () {
      this.getArticles()
      // 새로운 게시글이 추가됐음을 알리는 이벤트가 발생하면 getArticles 함수를 실행해준다.
    },
    movePage () {
      this.$router.push({ name: 'ArticleCreate' })
    }
  },
  created: function () {
    this.getArticles()
    // 페이지가 처음 로딩되자마자 getArticles 함수를 실행시켜 게시글 리스트를 쭈욱 보여준다.
  },
}
</script>

<style>
</style>
