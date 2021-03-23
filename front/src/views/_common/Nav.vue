<template>
  <div id="nav">
    <header>
  <nav>
    
    <img src="https://aspergerasturias.org/wp-content/uploads/2016/03/Logo-AAA_horizontal2_smll1.jpg" height="80" width="250">
    
    <ul class="menu">
      <li><router-link to="/Aseo">Aseo</router-link></li>
         <!-- <ul class="submenu">
          <li><a href="#">Ducharse</a></li>
          <li><a href="#">Cepillarse los dientes</a></li>
          <li><a href="#">Vestirse</a></li>
         </ul> -->
      
      <li><router-link to="/Ocio">Ocio</router-link></li>
         <!-- <ul class="submenu">
             <li><a href="#">Ir al colegio</a></li>
             <li><a href="#">Deportes</a></li>
              <li><a href="#">Musica</a></li>
             <li><a href="#">Juego</a></li>
         </ul> -->
      
      <li><router-link to="/Alimentacion">Alimentacion</router-link></li>
          <!-- <ul class="submenu">
             <li><a href="#">Desayuno</a></li>
             <li><a href="#">Media mañana</a></li>
              <li><a href="#">Comida</a></li>
             <li><a href="#">Merienda</a></li>
             <li><a href="#">Cena</a></li>
         </ul> -->
      
      <li><router-link to="/AñadirTareas">Añadir Tareas</router-link></li>
      <li><router-link to="/">Home</router-link></li> |
      <li><router-link to="/Login">Login</router-link></li>
      <li><router-link to="/Register">Register</router-link></li>
      
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
  background-color: #9BC734;
  color: white;
}
/*Submenu style*/
.submenu{
  list-style: none;
  background-color: #9BC734;
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
  background-color: #9BC734;
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
