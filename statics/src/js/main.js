import "../scss/styles.scss";
import { initPages } from "./pages/index.js";
import "lazysizes";

window.addEventListener("DOMContentLoaded", async () => {
  await initPages();
});
