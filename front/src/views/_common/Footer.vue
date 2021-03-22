<template>
  <div id="footer">
    <!-- <Nav /> -->
   <div class="container">
  <span><img src="https://img.icons8.com/nolan/64/facebook-new.png"/></span>
  <span><img src="https://img.icons8.com/cute-clipart/64/000000/instagram-new.png"/><img src="https://img.icons8.com/cute-clipart/64/000000/twitter.png"/></span>
</div> 
  </div>
</template>
<style scoped>
#footer{
  width: 100%;
  background-color: #38C1CA;
}

.container img{
  width: 30px;
  margin: 15px;
  cursor:pointer;
}
</style>

<script>
// import Nav from "./Nav.vue";

export default {
  name: "Footer",
  // components: { Nav },
};
</script>
