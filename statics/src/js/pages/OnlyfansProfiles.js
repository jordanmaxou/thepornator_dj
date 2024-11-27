import { OnlyfansProfilesLoader } from "../libs/ads/index.js";

export class OnlyfansProfiles {
  constructor() {
    this.onlyfansProfilesLoader = new OnlyfansProfilesLoader();
  }

  start() {
    this.onlyfansProfilesLoader.start();
  }
}
