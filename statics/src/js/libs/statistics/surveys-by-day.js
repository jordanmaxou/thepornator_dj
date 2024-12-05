import { BaseLineChart } from "./base-line-chart.js";

export class SurveysByDay extends BaseLineChart {
  constructor() {
    super();
    this.dataId = "surveys-by-day-data";
    this.canvasId = "surveys-by-day-chart";
  }
}
