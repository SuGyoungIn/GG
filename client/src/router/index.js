import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CommunityView from '../views/CommunityView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import MyPage from '../pages/MyPage.vue'
import RecommendOne from '../pages/RecommendOne.vue'
import RecommendTwo from '../pages/RecommendTwo.vue'
import RecommendThree from '../pages/RecommendThree.vue'
import DetailPage from '../pages/DetailPage.vue'
import ArticlePage from '../pages/ArticlePage.vue'
import FindUser from '../pages/FindUser.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/mypage/:user_id',
    name: 'mypage',
    component: MyPage
  },
  {
    path: '/recommend1',
    name: 'recommend1',
    component: RecommendOne
  },
  {
    path: '/recommend2',
    name: 'recommend2',
    component: RecommendTwo
  },
  {
    path: '/recommend3',
    name: 'recommend3',
    component: RecommendThree
  },
  {
    path: '/detail/:movie_id',
    name: 'detail',
    component: DetailPage
  },
  {
    path: '/article/:article_id',
    name: 'article',
    component: ArticlePage
  },
  {
    path: '/finduser',
    name: 'finduser',
    component: FindUser
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to,from, next)=>{
  next()
})

export default router
