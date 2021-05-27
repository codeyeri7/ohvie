<template>
  <div>
    <section class="page-section" id="contact">
      <div class="container">
        <!-- Contact Section Heading-->
        <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Detail Update</h2>
        <!-- Contact Section Form-->
        <div class="row">
          <div class="col-lg-8 mx-auto">
              <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19.-->
            <div class="control-group">
              <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                <label>Title</label>
                <input style="font-size: 30px" v-model.trim="article.title" class="form-control" id="title" type="text" placeholder="Title" required="required" data-validation-required-message="Please enter your title." />
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="control-group">
              <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                <label>Content</label>
                <textarea style="font-size: 30px" v-model.trim="article.content" class="form-control" id="content" rows="5" placeholder="Content" required="required" data-validation-required-message="Please enter a message."></textarea>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <br />
            <div id="success"></div>
            <div class="text-white st-font form-group"><button @click="articleDetailUpdate(article)" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">Update</button></div>
          </div>
        </div>
      </div>
    </section>
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
      // console.log(res)
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