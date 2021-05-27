<template>
  <div>
    <v-card>
      <ArticleList :articles="articles"/>
      <v-layout row wrap justify-center>
        <v-flex text-center>
          <v-btn
              elevation="2"
              rounded
              outlined
              color="black"
              @click="movePage"
            >
            CREATE
          </v-btn>
        </v-flex>
      </v-layout>
    </v-card>
  </div>
</template>

<script>
import ArticleList from '../../components/community/ArticleList.vue'
import axios from 'axios'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
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
    },
    articlesUpdated: function () {
      this.getArticles()
    },
    movePage () {
      this.$router.push({ name: 'ArticleCreate' })
    }
  },
  created: function () {
    this.getArticles()
  },
}
</script>

<style>
</style>
