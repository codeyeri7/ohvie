<!--<template>
  <v-container>
    <v-card elevation="10" outlined width="100%" class="mx-auto">
      <v-card-title>
        Community
          <v-spacer></v-spacer>
          <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
        </v-card-title>
        <v-data-table
        :headers="headers"
        :items="moviereviews"
        :loading="loading"
        :search="search">
        <template slot="items" slot-scope="props">
          <td :class="headers[0].class">{{ id2date(props.item._id)}}</td>
          <td :class="headers[1].class">{{ props.item.name }}</td>
          <td :class="headers[2].class">{{ props.item.title }}</td>
          <td :class="headers[3].class">{{ props.item._user ? props.item._user.id : 'Guest' }}</td>
          <td :class="headers[4].class">{{ props.item.cnt.rating }}</td>
          <td :class="headers[5].class">{{ props.item.cnt.comment }}</td>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template> -->

<!--<template>
  <div>
    <ul>
      <li v-for="(review, idx) in reviews" :key="idx">
        <span @click="updateReviewStatus(todo)" :class="{ completed: review.completed }">{{ review.title }}</span>
        <button @click="deleteReview(todo)" class="review-btn">X</button>
      </li>
    </ul>
  </div>
</template>-->

<!--
<script>
import axios from 'axios'

export default {
  name: 'ReviewList',
  data: function () {
    return {
      search: '',
      headers: [
        { text: 'Date', value: '_id', sortable: true, class: 'hidden-sm-and-down' },
        { text: 'Movie', value: 'name', sortable: true,},
        { text: 'Title', value: 'title', sortable: true},
        { text: 'Writer', value: '_user', sortable: false },
        { text: 'Rating', value: 'rating', sortable: true},
        { text: 'Comment', value: 'comment', sortable: true},
      ],
      moviereviews: [],
      loading: false
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
    getReviews: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/articles/',
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.moviereviews = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReview: function (review) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/articles/${review.id}/`,
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.getReviews()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateReviewStatus: function (review) {
      const reviewItem = {
        ...review,
        completed: !review.completed
      }

      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/community/articles/${review.id}/`,
        data: reviewItem,
        headers: this.setToken(),
      })
        .then((res) => {
          console.log(res)
          review.completed = !review.completed
        })
      },
    },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getReviews()
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
-->

<template>
  <div>
  <div class="container">
    <h2 class="st-font" style="margin-bottom:30px">Community</h2>
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <div class="post-preview" style="cursor:pointer;" v-for="(article, idx) in articles" :key="idx">
          <h3 class="title-font" @click="DetailArticle(article)">{{article.id}}번 글</h3>
          <h2 class="title-font" @click="DetailArticle(article)">
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
      </div>
    </div>
  </div>

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

  // props: {
  //   articles: [Array, Object]
  // },
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