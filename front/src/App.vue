<template>
  <div>
    <v-app-bar color="black" dark>
    <span v-if="isLogin">
      <!-- <v-toolbar-title>Page title</v-toolbar-title> -->

      <!-- <div class="d-flex align-center">
      </div> -->
      <!-- <v-img
        alt="Ohvie Logo"
        class="shrink mr-2"
        contain
        src="@/assets/ohvie_logo_middle.png"
        transition="scale-transition"
        width="60"
        v-on:click="mainPageRedirect" 
      /> -->
      <v-spacer></v-spacer>
      <RouterLink :to="{ name: 'ArticleList' }">Community</RouterLink>
      <RouterLink @click.native="logout" to="#">Logout</RouterLink>
    </span>
    <span v-else>
      <RouterLink :to="{ name: 'Signup' }">Signup</RouterLink> |
      <RouterLink :to="{ name: 'Login' }">Login</RouterLink> 
    </span>
    </v-app-bar>
    <!-- <router-view></router-view> -->
    <router-view @login="isLogin = true"/>
  </div>
</template>

<!--<template>
  <div id="app">
    <div id="nav">
      <v-app>
        <span v-if="isLogin">  
          <v-app-bar app color="black" dark>
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
          </v-app-bar>
            <RouterLink :to="{ name: 'ArticleList' }">Community</RouterLink>
            <RouterLink @click.native="logout" to="#">Logout</RouterLink>
          </span>
          <span v-else>
            <RouterLink :to="{ name: 'Signup' }">Signup</RouterLink> |
            <RouterLink :to="{ name: 'Login' }">Login</RouterLink> 
          </span>
        </v-app>
          <v-btn icon><v-icon>mdi-heart</v-icon></v-btn>
          <v-btn icon><v-icon>mdi-magnify</v-icon></v-btn>
          <v-content>
            <router-view @login="isLogin = true"/>
          </v-content>
     </div>
  </div>
</template>-->

<!--<template>
  <div id="app">
    <div id="nav">
      <span v-if="isLogin">
        <router-link :to="{ name: 'ArticleList' }">Community</router-link> | 
        <router-link @click.native="logout" to="#">Logout</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>
    </div>
    <router-view @login="isLogin = true"/>
  </div>
</template>-->

<script>
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
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>