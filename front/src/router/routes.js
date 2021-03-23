export const routes = [
  {
    path: "/",
    component: () => import("@/views/Home/HomePage.vue"),
  },
  
  {
    path: "/tasks",
    component: () => import("@/views/TaskList/TaskListPage.vue"),
  },
  {
    path: "/Aseo",
    component: () => import("@/views/Aseo/AseoPage.vue"),
  },
  {
    path: "/Ocio",
    component: () => import("@/views/Ocio/OcioPage.vue"),
  },
  {
    path: "/Alimentacion",
    component: () => import("@/views/Alimentacion/AlimentacionPage.vue"),
  },
  {
    path: "/AñadirTarea",
    component: () => import("@/views/AñadirTarea/AñadirTareaPage.vue"),
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
