import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/movies/Main.vue'
import ArticleView from '../views/community/ArticleView.vue'
import ArticleList from '../components/community/ArticleList.vue'
import ArticleCreate from '../components/community/ArticleCreate.vue'
import DetailView from '../views/community/DetailView.vue'
import ArticleDetailUpdate from '../views/community/ArticleDetailUpdate.vue'
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
    path: '/articleview',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/articlelist',
    name: 'ArticleList',
    component: ArticleList
  },
  {
    path: '/articlecreate',
    name: 'ArticleCreate',
    component: ArticleCreate
  },
  {
    path: '/articledetail/:article_pk',
    name: 'ArticleDetail',
    component: DetailView
  },
  {
    path: '/articleupdate/:article_pk',
    name: 'ArticleUpdate',
    component: ArticleDetailUpdate
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
