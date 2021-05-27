<template>
  <div id="app">
    <v-container>
      <v-layout row class="text-xs-center">
        <v-flex xs4 class="white lighten-4">
          <v-container style="position: relative; top: 20%; left: 100%;" class="text-xs-center">
            <v-card flat>
              <v-card-title primary-title>
                <h4>Login</h4>
              </v-card-title>
              <v-form>
               <input type="text" placeholder="username" id="username" v-model="credentials.username" v-text-field prepend-icon="person" name="Username" label="Username" />
              <div>
                  -----------------------------------------------
              </div>
              <input type="password" placeholder="password" id="password" v-model="credentials.password" v-text-field prepend-icon="lock" name="Password" label="Password" />
              <v-card-actions>
                <v-btn @click="login" primary large block>Login</v-btn>
              </v-card-actions>
              </v-form>
            </v-card>
          </v-container>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'Main' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>