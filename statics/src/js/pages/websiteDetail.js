import Chart from "chart.js/auto";

export class WebsiteDetail {
  #radarChartBlockId = "result-data-chart";
  #radarDataBlockId = "chart-radar-data";
  #radarData;
  #chartBlock;
  #chartCtx;

  constructor() {
    this.#chartBlock = document.getElementById(this.#radarChartBlockId);
    this.#chartCtx = this.#chartBlock.getContext("2d");
    const rawRadardData = document.getElementById(
      this.#radarDataBlockId
    )?.textContent;
    if (rawRadardData) {
      try {
        this.#radarData = JSON.parse(rawRadardData);
      } catch {
        console.warn("A problem occurs during radar data retrieval");
      }
    }
  }

  start() {
    this.displayChart();
  }

  displayChart() {
    if (this.#chartCtx && this.#radarData) {
      new Chart(this.#chartCtx, {
        type: "radar",
        data: this.#radarData,
        options: {
          responsive: true,
          plugins: {
            legend: {
              display: true,
            },
            title: {
              display: true,
              text: this.#chartBlock.dataset.title,
            },
          },
          elements: {
            line: {
              borderWidth: 3,
            },
          },
          scales: {
            r: {
              min: 0,
              max: 5,
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
