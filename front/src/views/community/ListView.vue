<template>
  <div>
    <ArticleList />
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

export default {
  name: 'ListView',
  components: {
    ArticleList
  },
  methods: {
    movePage () {
      this.$router.push({ name: 'ArticleCreate' })
    }
  }
}
</script>

<style>

</style>