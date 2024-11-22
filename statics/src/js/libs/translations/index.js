import surveyTranslations from "./survey.js";
import surveyResultTranslation from "./surveyResult.js";

const translations = {
  ...surveyTranslations,
  ...surveyResultTranslation,
};

export default function translate(id) {
  const translation = translations[id][document.documentElement.lang];
  if (translation) {
    return translation;
  }
  throw Error(
    `Translation is missing for '${id}' for '${document.documentElement.lang}' lang`
  );
}
