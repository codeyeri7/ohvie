<template>
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
            this.$router.push({ name: 'ReviewList' })
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

</style>