import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../components/HomeView.vue'
import user from '../views/users.vue'
import Manegre from '../views/manegre.vue'
// import manager from '../views/manegre.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'user',
      component: user
    },
    {
      path: '/maneger',
      name: 'maneger',
      component: Manegre
    },
    {
      path: '/about',
      name: 'about',
  
      component: () => import('../components/AboutView.vue')
    },
    {
      path: '/Login',
      name: 'Login',

      component: () => import('../components/Login.vue')
    }, {
      path: '/ragister',
      name: 'ragister',

      component: () => import('../components/ragister.vue')
    },
    {
      path: '/cart',
      name: 'Cart',
      component: () => import('../components/cart.vue')
    },
    {
      path: '/product',
      name: 'product',

      component: () => import('../components/product.vue')
    },
    {
      path: '/Category',
      name: 'Category',
  
      component: () => import('../components/category.vue')
    },
    {
      path: '/admin',
      name: 'admin',
 
      component: () => import('../views/admin.vue')
    }, {
      path: '/admindashbord',
      name: 'adminmain',

      component: () => import('../components/adminmain.vue')
    },
    {
      path: '/adminreq',
      name: 'adminreq',

      component: () => import('../components/adminreq.vue')
    },
    {
      path: '/search',
      name: 'search',

      component: () => import('../components/search.vue')
    }
    
    
  ]
})

export default router
