import {
  SurveysByDay,
  ReliabilityByDay,
  SurveysBestWebsiteResults,
  NbClicksBySite,
  NbClicksByModel,
  AipornPictureClassification,
  AiOrNotAiByDate,
  // NbAiContentTagsUpdatedByDay,
  NbClicksByChannel,
  VideoClassification,
} from "../libs/statistics/index.js";

export class Statistics {
  #surveysByDayChart;
  #reliabilityByDay;
  #surveysBestWebsiteResults;
  #nbClicksBySite;
  #nbClicksByModel;
  #aipornPictureClassification;
  #aiOrNotAiByDate;
  // #nbAiContentTagsUpdatedByDay;
  #nbClicksByChannel;
  #videoClassification;

  constructor() {
    this.#surveysByDayChart = new SurveysByDay();
    this.#reliabilityByDay = new ReliabilityByDay();
    this.#surveysBestWebsiteResults = new SurveysBestWebsiteResults();
    this.#nbClicksBySite = new NbClicksBySite();
    this.#nbClicksByModel = new NbClicksByModel();
    this.#aipornPictureClassification = new AipornPictureClassification();
    this.#aiOrNotAiByDate = new AiOrNotAiByDate();
    // this.#nbAiContentTagsUpdatedByDay = new NbAiContentTagsUpdatedByDay();
    this.#nbClicksByChannel = new NbClicksByChannel();
    this.#videoClassification = new VideoClassification();
  }

  start() {
    this.#surveysByDayChart.build();
    this.#reliabilityByDay.build();
    this.#surveysBestWebsiteResults.build();
    this.#nbClicksBySite.build();
    this.#nbClicksByModel.build();
    this.#aipornPictureClassification.build();
    this.#aiOrNotAiByDate.build();
    // this.#nbAiContentTagsUpdatedByDay.build();
    this.#nbClicksByChannel.build();
    this.#videoClassification.build();
  }
}
