/* eslint-disable no-undef */
/* eslint-disable no-self-assign */
import { createApp, h } from "vue";
import { createInertiaApp, InertiaLink } from "@inertiajs/inertia-vue3";
import { InertiaProgress } from "@inertiajs/progress/src";

import "../../static/css/app.postcss"; // Importación del archivo app.postcss

let customRoute = (...args) => {
  args[0] = args[0];
  return window.reverseUrl(...args);
};

const pages = {
  Index: "Index.vue",
  Publications: "Publications.vue",
};

InertiaProgress.init();

createInertiaApp({
  page: JSON.parse(document.getElementById("page").textContent),
  resolve: (name) => require(`./Pages/${pages[name]}`),
  setup({ el, app, props, plugin }) {
    const appVue = createApp({ render: () => h(app, props) })
      .use(plugin)
      .mixin({ methods: { route: customRoute }})
      .component("inertia-link", InertiaLink);

    appVue.mount(el);
  },
});
