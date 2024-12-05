import { BaseLineChart } from "./base-line-chart.js";

export class ReliabilityByDay extends BaseLineChart {
  constructor() {
    super();
    this.dataId = "reliability-by-day-data";
    this.canvasId = "reliability-by-day-chart";
  }
}
