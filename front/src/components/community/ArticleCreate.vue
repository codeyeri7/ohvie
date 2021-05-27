<template>
  <div>
    <v-container>
      <h2>Community</h2>
      <v-row>
        <v-col>
          <label>Title</label>
          <v-text-field v-model.trim="title" rows="5" placeholder="Title" required="required"></v-text-field>
          <hr>
          <label>Content</label>
          <v-text-field v-model.trim="content" rows="5" placeholder="Content" required="required"></v-text-field>
          <br />
          <div id="success"></div>
          <v-btn @click="createArticle" x-small color="primary" dark>Add</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'
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
            this.$router.push({ name: 'ArticleView' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  },
}
</script>

<style>
</style>