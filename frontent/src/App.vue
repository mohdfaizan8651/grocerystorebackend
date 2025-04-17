<script>
import { RouterLink, RouterView } from "vue-router";
import { mapActions } from "vuex";
export default {
  computed: {
    state() {
      return this.$store.state;
    },
  },
  methods: {
    handlelogout() {
      sessionStorage.clear();
      this.$store.commit("logout");
      this.$router.push("/Login");
    },
  },
};
</script>

<template>
  <div>
    <nav
      class="navbar navbar-expand-lg navbar-light"
      style="background-color: seagreen">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Grocery Store</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink
                class="nav-link"
                aria-current="page"
                v-if="state.role === 'user' && state.loggedIn"
                to="/"
                >Home</RouterLink
              >
            </li>
            <li class="nav-item">
              <RouterLink
                class="nav-link"
                v-if="state.role === 'ADMIN' && state.loggedIn"
                to="/admindashbord"
                >Home</RouterLink
              >
            </li>
            <li class="nav-item">
              <RouterLink
                class="nav-link"
                v-if="state.role === 'manager' && state.loggedIn"
                to="/maneger"
                >Home</RouterLink
              >
            </li>
            <li class="nav-item">
              <RouterLink
                class="nav-link"
                v-if="state.role === 'ADMIN' && state.loggedIn"
                to="/adminreq"
                >Requests</RouterLink
              >
            </li>
            <li class="nav-item">
              <RouterLink
                class="nav-link"
                v-if="state.role === 'manager' && state.loggedIn"
                to="/product"
                >Add Product</RouterLink
              >
            </li>
            <li class="nav-item">
              <RouterLink
                class="nav-link"
                v-if="state.role === 'manager' && state.loggedIn"
                to="/category"
                >Add Category</RouterLink
              >
            </li>
            <li class="nav-item">
              <RouterLink
                class="nav-link"
                v-if="state.role === 'user' && state.loggedIn"
                to="/about"
                >About</RouterLink
              >
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" v-if="!state.loggedIn" to="/Login"
                >Login</RouterLink
              >
            </li>
            <li class="nav-item">
              <RouterLink
                class="nav-link"
                v-if="state.role === 'user' && state.loggedIn"
                to="/cart"
                >Cart</RouterLink
              >
            </li>
          </ul>
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <button
                v-if="state.loggedIn"
                v-on:click="handlelogout()"
                class="btn btn-outline-warning"
                type="submit">
                Logout
              </button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- <header class="header">
      <div class="wrapper">
        <nav class="nav">
          <RouterLink
            class="link"
            v-if="state.role === 'user' && state.loggedIn"
            to="/"
            >Home</RouterLink
          >
          <RouterLink
            class="link"
            v-if="state.role === 'ADMIN' && state.loggedIn"
            to="/admindashbord"
            >Home</RouterLink
          >
          <RouterLink
            class="link"
            v-if="state.role === 'manager' && state.loggedIn"
            to="/maneger"
            >Home</RouterLink
          >
          <RouterLink
            class="link"
            v-if="state.role === 'ADMIN' && state.loggedIn"
            to="/adminreq"
            >Requests</RouterLink
          >

          <RouterLink
            class="link"
            v-if="state.role === 'manager' && state.loggedIn"
            to="/product"
            >Add Product</RouterLink
          >
          <RouterLink
            class="link"
            v-if="state.role === 'manager' && state.loggedIn"
            to="/category"
            >Add Category</RouterLink
          >
          <RouterLink
            class="link"
            v-if="state.role === 'user' && state.loggedIn"
            to="/about"
            >About</RouterLink
          >
          <RouterLink class="link" v-if="!state.loggedIn" to="/Login"
            >Login</RouterLink
          >
          <RouterLink
            class="link"
            v-if="state.role === 'user' && state.loggedIn"
            to="/cart"
            >Cart</RouterLink
          >
          <button
            class="logout-btn"
            v-if="state.loggedIn"
            v-on:click="handlelogout()">
            Logout
          </button>
        </nav>
      </div>
    </header> -->

    <RouterView />
  </div>
</template>

<style>
.navbar-nav .nav-item .nav-link {
  color: rgba(255, 255, 255, 0.6);
  transition: color 0.3s ease-in-out;
}
.navbar-nav .nav-item .nav-link:hover {
  color: rgba(255, 255, 255, 0.8);
}
.navbar .navbar-brand {
  color: white;
}
.navbar .navbar-brand:hover {
  color: white;
}
.router-link-active {
  color: white !important;
}
.error {
  text-align: center;
  margin-top: 10px;
  color: red;
  font-weight: 500;
}
.wrapper {
  background-color: seagreen;
  height: 50px;
  
}

.nav {
  font-size: larger;
  display: flex;
  justify-content: right;
  align-items: center;
  height: 50px;
  font-size: larger;
}
.nav .link {
  color: white;
  margin-right: 1rem;
  text-decoration: none;
  padding: 1px 5px;
  border: none;
  border-radius: 5px;
  transition-duration: 5ms;
}
.nav .link:hover {
  outline: 1px solid white;
}

.nav .logout-btn {
  margin-right: 1rem;
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  background-color: antiquewhite;
  cursor: pointer;
}
.nav .logout-btn:hover {
  background-color: rgb(221, 153, 64);
}
.search-component {
  max-width: 100%;
  margin: 7px;
}

.search-component input {
  width: 100%;
  padding: 10px 17px;
  font-size: 14px;
  box-sizing: border-box;
  outline: none;
  border: none;
  border-radius: 20px;
  box-shadow: 1px 2px 4px 2px rgba(0, 0, 0, 0.1);
}
</style>
