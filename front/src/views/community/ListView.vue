<template>
  <div>
    <ReviewList />
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
import ReviewList from '../../components/community/ReviewList.vue'

export default {
  name: 'ListView',
  components: {
    ReviewList
  },
  methods: {
    movePage () {
      this.$router.push({name: 'ReviewCreate'})
    }
  }
}
</script>

<style>

</style>