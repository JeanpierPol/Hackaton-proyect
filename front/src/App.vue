<template>
  <div id="app">
      
    <Nav></Nav>
    <div id="main">
      <router-view />
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
// @ is an alias to /src
import Nav from "@/views/_common/Nav.vue";
import Footer from "@/views/_common/Footer.vue";

export default {
  name: "App",
  components: {
    Nav,
    Footer,
  },
};
</script>

<style>
#main {
  flex: 1;
  background-image: url(https://longevitta.mx/wp-content/uploads/2020/02/EFEMERIDES-05-scaled.jpg);
  background-size: cover;
  margin-left: 8rem;
  width:75%;
}

</style>
