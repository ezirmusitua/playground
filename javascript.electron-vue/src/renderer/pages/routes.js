import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'landing-page',
      component: require('@/pages/LandingPage').default,
    },
    {
      path: '*',
      redirect: '/',
    },
    {
      path: '/HelloWorld',
      name: 'hello-world',
      component: require('@/pages/HelloWorld').default,
    },
  ],
});
