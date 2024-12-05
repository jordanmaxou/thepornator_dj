import { Home } from "./home.js";
import { Survey } from "./Survey.js";
import { SurveyResult } from "./SurveyResult.js";
import { WebsiteDetail } from "./websiteDetail.js";
import { ContentEdit } from "./ContentEdit.js";
import { AiGame } from "./AiGame.js";
import { OnlyfansProfiles } from "./OnlyfansProfiles.js";
import { GlossaryDetail } from "./GlossaryDetail.js";
import { Statistics } from "./Statistics.js";
import { PornVideoTubes } from "./PornVideoTubes.js";
import { Commons } from "./Commons.js";

export const initPages = async () => {
  const body = document.querySelector("body");
  let page;

  switch (body.getAttribute("data-page")) {
    case "home":
      page = new Home();
      break;
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
    case "porn-videos-tubes":
      page = new PornVideoTubes();
      break;
    case "ai-game":
      page = new AiGame();
      break;
    case "onlyfans-profiles":
      page = new OnlyfansProfiles();
      break;
    case "glossary":
      page = new GlossaryDetail();
      break;
    case "statistics":
      page = new Statistics();
      break;
  }

  if (page) {
    await page.start();
  }
  const commons = new Commons();
  await commons.start();
};
