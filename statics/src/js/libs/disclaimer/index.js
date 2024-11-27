import { getCookie, setCookie } from "../utils/index.js";
import { DisclaimerPopunder } from "../ads/disclaimer-popunder.js";

export class Disclaimer {
  #disclaimerCookieName = "disclaimer-shown";
  #disclaimerContainerId = "disclaimer-popup";
  #disclaimerContainer;
  #disclaimerAgreeButtonId = "disclaimer-agree-button";
  #disclaimerAgreeButton;
  #disclaimerPopunder;

  constructor() {
    this.#disclaimerContainer = document.getElementById(
      this.#disclaimerContainerId
    );
    this.#disclaimerAgreeButton = document.getElementById(
      this.#disclaimerAgreeButtonId
    );
    this.#disclaimerPopunder = new DisclaimerPopunder();
  }

  start() {
    if (getCookie(this.#disclaimerCookieName) !== "true") {
      this.#disclaimerAgreeButton.addEventListener("click", () => {
        this.updateCookie();
        this.#disclaimerContainer.style.display = "none";
        this.currentUrlOnNewTab();
        this.#disclaimerPopunder.exec();
      });
      // clickadu script integration on head django template site
      this.#disclaimerContainer.style.display = "block";
    }
  }

  updateCookie() {
    const dayInMs = 24 * 60 * 60 * 1000;
    const date = new Date();
    date.setTime(date.getTime() + dayInMs);
    setCookie(this.#disclaimerCookieName, true, {
      expires: date.toGMTString(),
      path: "/",
    });
  }

  currentUrlOnNewTab() {
    const newTab = window.open(window.location.href, "_blank");
    newTab.focus();
  }
}
