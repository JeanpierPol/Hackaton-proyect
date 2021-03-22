<template>
  <div id="nav">
    <header>
  <nav>
    <h1 class="logo">Hackatonf5</h1>
    
    <ul class="menu">
      <li><a href="">Aseo</a></li>
      <li><a href="">Ocio</a>
        <ul class="submenu">
          <li><a href="#">1</a></li>
          <li><a href="#">2</a></li>
          <li><a href="#">3</a>
            <ul class="submenu2">
              <li><a href="#">3.1</a></li>
              <li><a href="#">2</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li><a href="">Alimentacion</a></li>
      <li><a href="">Añadir Tareas</a></li>
      <li><router-link to="/">Home</router-link></li> |
      <li><router-link to="/about">About</router-link></li>
      
    </ul>
  </nav>
</header>


    
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
*{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Lato', sans-serif;
}
header{
  width: 100%;
  background-color: #38C1CA;
}
nav{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.logo{
  color: yellow;
  padding: 10px;
  font-size: 35px;
}
nav ul{
  list-style: none;
}
.menu > li {
  display: inline-block;
  padding: 10px;
  position: relative;
}
.menu > li > a{
  text-decoration: none;
  color: black;
  font-size: 20px;
  padding: 10px 14px;
}
.menu li:hover{
  background-color: #73CE52;
  color: white;
}
/*Submenu style*/
.submenu{
  list-style: none;
  background-color: #73CE52;
  width: 140px;
  position: absolute;
  left: 0;
  display: none;
  animation: slideup .3s ease;
}
.submenu > li{
  display: block;
  padding: 10px;
  text-align: center;
  position: relative;
}
.submenu > li > a{
  text-align: center;
  text-decoration: none;
  color: white;
}

.submenu li:hover{
  background-color:#38C1CA ;
  color: white;
}

/*Submenu2 style*/
.submenu2{
  display: none;
  background-color: #73CE52;
  width: 140px;
  position: absolute;
  left: 100%;
  top: 0;
  list-style: none;
  animation: slideleft .3s ease;
}

.submenu2 li{
  display: block;
  padding: 10px;
  text-align: center;
}
.submenu2 li a{
  color: white;
  text-decoration: none;
}

.submenu2 li:hover{
  background-color: #38C1CA;
  color: white;
}

/*Submenu and Submenu2 appear on hover*/

.menu > li:hover .submenu{
  display: block;
}
.submenu > li:hover .submenu2{
  display: block;
}

/*Animations*/
@keyframes slideup {
  0% {
    transform: translateY(18px);
    opacity: 0;
  }
  100% {
    transform: none;
    opacity: 1;
  }
}

@keyframes slideleft {
  0% {
    transform: translateX(18px);
    opacity: 0;
  }
  100% {
    transform: none;
    opacity: 1;
  }
}

</style>
