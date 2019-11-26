import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import VuePhoneNumberInput from 'vue-phone-number-input';
import 'vue-phone-number-input/dist/vue-phone-number-input.css';
import "./registerServiceWorker";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import locale from "element-ui/lib/locale/lang/en";
import VeeValidate from 'vee-validate';

Vue.use(VeeValidate, {
  inject: true,
  fieldsBagName: 'veeFields'
})
Vue.use(ElementUI, { locale });
Vue.component('vue-phone-number-input', VuePhoneNumberInput);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
