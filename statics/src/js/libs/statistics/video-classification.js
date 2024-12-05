import { BasePieChart } from "./base-pie-chart.js";

export class VideoClassification extends BasePieChart {
  constructor() {
    super();
    this.dataId = "video-classification-data";
    this.canvasId = "video-classification-chart";
  }
}
