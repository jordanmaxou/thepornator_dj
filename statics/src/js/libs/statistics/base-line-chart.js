import Chart from "chart.js/auto";
import { BaseChart } from "./base-chart.js";

export class BaseLineChart extends BaseChart {
  build() {
    if (this.init()) {
      if (
        this.canvas &&
        this.data?.labels &&
        this.data?.data &&
        this.data?.title
      ) {
        const ctx = this.canvas.getContext("2d");
        new Chart(ctx, {
          type: "line",
          data: {
            labels: this.data.labels,
            datasets: [
              {
                data: this.data.data,
                borderColor: "rgba(37, 71, 169, 1)",
                backgroundColor: "rgba(37, 71, 169, 1)",
                borderWidth: 1,
              },
            ],
          },
          options: {
            responsive: true,
            plugins: {
              legend: {
                display: false,
              },
              title: {
                display: true,
                text: this.data.title,
              },
            },
          },
          scales: {
            y: {
              min: 0,
              max: 10000,
            },
          },
        });
      }
    }
  }
}
