export const routes = [
  {
    path: "/",
    component: () => import("@/views/Home/HomePage.vue"),
  },
  // {
  //   path: "/about",
  //   component: () => import("@/views/About/AboutPage.vue"),
  // },
  {
    path: "/tasks",
    component: () => import("@/views/TaskList/TaskListPage.vue"),
  },
  {
    path: "/Login",
    component: () => import("@/views/Login/LoginPage.vue"),
  },
  {
    path: "/Register",
    component: () => import("@/views/Register/RegisterPage.vue"),
  },
];
