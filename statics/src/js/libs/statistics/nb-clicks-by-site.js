import { BaseHorizontalBar } from "./base-horizontal-bar.js";

export class NbClicksBySite extends BaseHorizontalBar {
  constructor() {
    super();
    this.dataId = "nb-clicks-by-site-data";
    this.canvasId = "nb-clicks-by-site-chart";
  }
}
