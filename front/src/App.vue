<template>
  <v-app>
    <v-app-bar
      app
      color="black"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Ohvie Logo"
          class="shrink mr-2"
          contain
          src="@/assets/ohvie_logo_middle.png"
          transition="scale-transition"
          width="60"
          v-on:click="mainPageRedirect"
        />
      </div>
      <v-spacer></v-spacer>
      <span v-if="isLogin">  
        <RouterLink :to="{ name: 'ArticleView' }">Community</RouterLink> |
        <RouterLink @click.native="logout" to="#">Logout</RouterLink>
      </span>
      <span v-else>
        <RouterLink :to="{ name: 'Signup' }">Signup</RouterLink> |
        <RouterLink :to="{ name: 'Login' }">Login</RouterLink> 
      </span>
    </v-app-bar>
    <v-content>
      <router-view @login="isLogin = true"/>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'App',

  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
    ...mapActions([ 'fetchAllMovies']),
    mainPageRedirect: function () {
      this.$router.push({ name: 'Main' })
    }
  },
  created: function () {
    this.fetchAllMovies()
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  },
};
</script>

<style scoped>
.router-link-exact-active {
  text-decoration: none;
}
</style>