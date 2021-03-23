<template>
  <div>
    <div class="center">
      <h2>Registrate</h2>

      <div>
        <input
          v-model="username"
          placeholder="Nombre de usuario"
          type="text"
          v-on:keyup.enter="onLoginClick"
        />
      </div>
      <div>
        <input
          v-model="surname"
          placeholder="Apellido de usuario"
          type="text"
          v-on:keyup.enter="onLoginClick"
        />
      </div>
      <div>
        <input
          v-model="password"
          placeholder="Contraseña"
          type="password"
          v-on:keyup.enter="onLoginClick"
        />
      </div>
      <div>
        <input
          v-model="Cpassword"
          placeholder="Confirmar contraseña"
          type="password"
          v-on:keyup.enter="onLoginClick"
        />
      </div>
      <div><button @click="onLoginClick">Registar</button></div>
      <div class="error" v-if="showError">
        La contraseña o el usuario no es correcto.
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      surname: "",
      password: "",
      Cpassword: "",
      showError: false,
    };
  },
  methods: {
    async onLoginClick() {
      const loginData = { username: this.username, password: this.password };
      const ok = await this.$auth.login(loginData);
      if (ok) {
        this.$router.push("/admin");
      } else {
        this.showError = true;
      }
    },
  },
};
</script>

<style scoped>
.center {
  margin-top: 2%;
  margin-left: 80%;
}
input[type="text"],
input[type="password"] {
  width: 300px;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}
button {
  background-color: #38C1CA;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 300px;
}
button:hover {
  opacity: 0.8;
}
.error {
  border: 1px solid;
  margin: 10px auto;
  padding: 15px 0 15px 0;
  background-repeat: no-repeat;
  background-position: 10px center;
  width: 300px;
  font-size: 0.85rem;
}
.error {
  color: #d8000c;
  background-color: #ffbaba;
}
button:hover {
  opacity: 0.8;
}
</style>