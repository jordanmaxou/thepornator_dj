export class Navbar {
  #headerId = "header";
  #header;
  #navBarId = "navbar";
  #navBar;
  #mobileNavBarButton;
  #mobileNarBarMobileDropdownButtons;

  constructor() {
    this.#header = document.getElementById(this.#headerId);
    this.#navBar = document.getElementById(this.#navBarId);
    this.#mobileNavBarButton = document.querySelector(".mobile-nav-toggle");
    this.#mobileNarBarMobileDropdownButtons = document.querySelectorAll(
      ".navbar .dropdown > a"
    );
  }

  start() {
    this.initNavbarTransparencyAction();
    this.initMobileNavbar();
  }

  initNavbarTransparencyAction() {
    document.addEventListener("scroll", () => {
      if (window.scrollY > 100) {
        this.#header.classList.add("header-scrolled");
      } else {
        this.#header.classList.remove("header-scrolled");
      }
    });
  }

  initMobileNavbar() {
    this.#mobileNavBarButton.addEventListener("click", () => {
      this.#navBar.classList.toggle("navbar-mobile");
      this.#mobileNavBarButton.classList.toggle("bx-x-circle");
    });
    Array.from(this.#mobileNarBarMobileDropdownButtons).forEach((button) => {
      button.addEventListener("click", (e) => {
        if (this.#navBar.classList.contains("navbar-mobile")) {
          e.preventDefault();
          button.nextElementSibling.classList.toggle("dropdown-active");
        }
      });
    });
  }
}
