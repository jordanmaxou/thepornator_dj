import { OnlyfansBullet, Banner } from "../libs/ads/index.js";
import { Disclaimer } from "../libs/disclaimer/index.js";
import { Navbar } from "../libs/navbar/index.js";

export class Commons {
  constructor() {
    this.onlyfansBullet = new OnlyfansBullet();
    this.banner = new Banner();
    this.disclaimer = new Disclaimer();
    this.navbar = new Navbar();
  }
  async start() {
    await this.onlyfansBullet.start();
    await this.banner.start();
    this.disclaimer.start();
    this.navbar.start();
  }
}
