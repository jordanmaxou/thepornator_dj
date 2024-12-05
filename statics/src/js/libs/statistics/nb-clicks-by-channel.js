import { BaseHorizontalBar } from "./base-horizontal-bar.js";

export class NbClicksByChannel extends BaseHorizontalBar {
  constructor() {
    super();
    this.dataId = "nb-clicks-by-channel-data";
    this.canvasId = "nb-clicks-by-channel-chart";
  }
}
