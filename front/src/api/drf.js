// api/drf.js
export default {
  URL: 'http://127.0.0.1:8000/',
  ROUTES: {
    signup: 'rest-auth/signup/',
    login: 'rest-auth/login/',
    logout: 'rest-auth/logout/',
    reviews: 'community/articles/',
    review: `community/articles/`
  }
}