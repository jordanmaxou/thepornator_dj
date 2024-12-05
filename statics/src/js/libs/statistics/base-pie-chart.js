import Chart from "chart.js/auto";
import { BaseChart } from "./base-chart.js";

export class BasePieChart extends BaseChart {
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
          type: "pie",
          data: {
            labels: this.data.labels,
            datasets: [
              {
                label: this.data?.label ?? "",
                data: this.data.data,
                backgroundColor: this.data.colors,
                borderColor: this.data.colors,
                borderWidth: 1,
              },
            ],
          },
          options: {
            responsive: true,
            plugins: {
              legend: {
                position: "top",
              },
              title: {
                display: true,
                text: this.data.title,
              },
              tooltip: {
                callbacks: {
                  label: function (tooltipItem, data) {
                    return tooltipItem.label;
                  },
                },
              },
            },
          },
        });
      }
    }
  }
}
