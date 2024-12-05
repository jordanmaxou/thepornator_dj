import { BaseLineChart } from "./base-line-chart.js";

export class NbAiContentTagsUpdatedByDay extends BaseLineChart {
  constructor() {
    super();
    this.dataId = "nb-ai-content-tags-updated-by-day-data";
    this.canvasId = "nb-ai-content-tags-updated-by-day-chart";
  }
}
