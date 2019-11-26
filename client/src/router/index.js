import Vue from "vue";
import VueRouter from "vue-router";
import ScheduleMeeting from "../views/ScheduleMeeting.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "schedule-meeting",
    component: ScheduleMeeting
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
