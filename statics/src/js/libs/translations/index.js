import surveyTranslations from "./survey.js";
import surveyResultTranslations from "./surveyResult.js";
import onlyfansBulletTranslations from "./onlyfansBullet.js";
import pornVideoTubesTranslations from "./PornVideoTubes.js";

const translations = {
  ...surveyTranslations,
  ...surveyResultTranslations,
  ...onlyfansBulletTranslations,
  ...pornVideoTubesTranslations,
};

export default function translate(id, data) {
  const translation = translations[id][document.documentElement.lang];
  if (translation) {
    if (data) {
      return translation.replace(/{(.*?)}/g, (_, key) => data[key]);
    }
    return translation;
  }
  throw Error(
    `Translation is missing for '${id}' for '${document.documentElement.lang}' lang`
  );
}
