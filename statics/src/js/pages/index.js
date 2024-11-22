import { Survey } from "./Survey.js";
import { SurveyResult } from "./SurveyResult.js";

export const initPages = async () => {
  const body = document.querySelector("body");
  let page;

  switch (body.getAttribute("data-page")) {
    case "survey-questions":
      page = new Survey();
      break;
    case "survey-results":
      page = new SurveyResult();
      break;
  }

  if (page) {
    await page.start();
  }
};
