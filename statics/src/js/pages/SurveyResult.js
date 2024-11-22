import Chart from "chart.js/auto";
import translations from "../libs/translations/index.js";

export class SurveyResult {
  #isValidBlockId = "wthf-yes-no";
  #isValidBlock;
  #updateSurveyUrl;
  #updateSurveyButtons;
  #radarChartBlockId = "result-data-chart";
  #radarDataBlockId = "chart-radar-data";
  #radarData;
  #chartCtx;

  constructor() {
    this.#chartCtx = document
      .getElementById(this.#radarChartBlockId)
      .getContext("2d");
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
    this.#isValidBlock = document.getElementById(this.#isValidBlockId);
    if (this.#isValidBlock) {
      this.#updateSurveyUrl = this.#isValidBlock.dataset.url;
      this.#updateSurveyButtons =
        this.#isValidBlock.querySelectorAll("span[data-value]");
    }
  }

  start() {
    this.displayChart();
    this.attachUpdateSurveyListeners();
  }

  attachUpdateSurveyListeners() {
    this.#updateSurveyButtons.forEach((button) => {
      button.addEventListener("click", async () => {
        try {
          const csrftoken = document.querySelector(
            "[name=csrfmiddlewaretoken]"
          ).value;
          const response = await fetch(this.#updateSurveyUrl, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": csrftoken,
            },
            mode: "same-origin",
            body: JSON.stringify({
              is_valid: Boolean(button.dataset.value),
            }),
          });

          if (response.ok) {
            this.removeUpdateSurveyBlock();
          }
        } catch (error) {
          console.error("An error occurred during result update", error);
        }
      });
    });
  }

  removeUpdateSurveyBlock() {
    if (this.#isValidBlock.parentElement) {
      this.#isValidBlock.parentElement.remove();
    }
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
              text: translations("idealsitecomparison"),
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
