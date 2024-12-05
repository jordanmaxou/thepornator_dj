import { BaseHorizontalBar } from "./base-horizontal-bar.js";

export class NbClicksByModel extends BaseHorizontalBar {
  constructor() {
    super();
    this.canvasId = "nb-clicks-by-model-chart";
    this.dataId = "nb-clicks-by-model-data";
  }
}
