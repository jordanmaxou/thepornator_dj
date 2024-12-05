import Chart from "chart.js/auto";
import { BaseChart } from "./base-chart.js";

export class BaseHorizontalBar extends BaseChart {
  build() {
    if (this.init()) {
      const ctx = this.canvas.getContext("2d");
      new Chart(ctx, {
        type: "bar",
        data: {
          labels: this.data.labels,
          datasets: [
            {
              label: this.data?.label ?? "",
              data: this.data.data,
              borderColor: "rgba(37, 71, 169, 1)",
              backgroundColor: "rgba(37, 71, 169, 1)",
            },
          ],
        },
        options: {
          indexAxis: "y",
          elements: {
            bar: {
              borderWidth: 2,
            },
          },
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
          scales: {
            x: {
              min: 0,
              ticks: {
                stepSize: 1,
              },
            },
          },
        },
      });
    }
  }
}
