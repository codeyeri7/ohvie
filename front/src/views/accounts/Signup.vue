<template>
  <div id="app">
    <v-container>
      <v-layout row class="text-xs-center">
        <v-flex xs4 class="white lighten-4">
          <v-container style="position: relative; top: 20%; left: 100%;" class="text-xs-center">
            <v-card flat>
              <v-card-title primary-title>
                <h4>Signup</h4>
              </v-card-title>
              <v-form>
               <input type="text" placeholder="username" id="username" v-model="credentials.username" v-text-field prepend-icon="person" name="Username" label="Username" />
              <div>
                  -----------------------------------------------
              </div>
              <input type="password" placeholder="password" id="password" v-model="credentials.password" v-text-field prepend-icon="lock" name="Password" label="Password" />
              <div>
               <div>
                  -----------------------------------------------
              </div>
                <input type="password" placeholder="passwordConfirmation" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
              </div>
              <v-card-actions>
                <v-btn @click="signup(credentials)" primary large block>회원가입</v-btn>
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
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
