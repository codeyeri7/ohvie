import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/movies/Main.vue'
import CreateView from '../views/community/CreateView.vue'
import ListView from '../views/community/ListView.vue'
import DetailView from '../views/community/DetailView.vue'
import Signup from '../views/accounts/Signup.vue'
import Login from '../views/accounts/Login.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/articlecreate',
    name: 'ArticleCreate',
    component: CreateView
  },
  {
    path: '/articlelist',
    name: 'ArticleList',
    component: ListView
  },
  {
    path: '/articledetail',
    name: 'ArticleDetail',
    component: DetailView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
