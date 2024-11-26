import { Survey } from "./Survey.js";
import { SurveyResult } from "./SurveyResult.js";
import { WebsiteDetail } from "./websiteDetail.js";
import { ContentEdit } from "./ContentEdit.js";
import { AiGame } from "./AiGame.js";

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
    case "website-detail":
      page = new WebsiteDetail();
      break;
    case "content-detail":
      page = new ContentEdit();
      break;
    case "ai-game":
      page = new AiGame();
      break;
  }

  if (page) {
    await page.start();
  }
};
