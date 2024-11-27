import { beegBaseUrl, beegPathList } from "./utils/index.js";

export class DisclaimerPopunder {
  exec() {
    window.location.href = this.selectUrlRandomly();
  }

  getGroupWeights() {
    const lang = document.documentElement.lang;
    if (lang === "fr") {
      return {
        beeg: 40,
        jmtv: 0,
        unClothy: 0,
        pornxAi: 25,
        candy: 30,
        deepMode: 10,
      };
    }
    return {
      beeg: 40,
      jmtv: 0,
      unClothy: 0,
      pornxAi: 10,
      candy: 40,
      deepMode: 10,
    };
  }

  selectUrlsGroupRandomly(groupWeights) {
    const totalWeight = Object.values(groupWeights).reduce(
      (total, weight) => total + weight,
      0
    );
    let randomNum = Math.random() * totalWeight;

    for (const group in groupWeights) {
      randomNum -= groupWeights[group];
      if (randomNum <= 0) {
        return group;
      }
    }
  }

  selectUrlRandomly() {
    const group = this.selectUrlsGroupRandomly(this.getGroupWeights());
    return this.getRandomUrl(group);
  }

  getRandomUrl(group) {
    const simple = {
      jmtv: [
        "https://www.jacquieetmicheltv.net/?dscl=1&ab=0&utm_medium=traffic&utm_source=thepornator&utm_campaign=JMTV_Home_Popunder&affiliate=0f5d50f7-8900-4952-b9ad-815f31f86ef7",
      ],
      unClothy: [
        "https://unclothy.com/?utm_source=thepornator&utm_medium=referral&utm_campaign=june",
      ],
      deepMode: ["https://deepmode.com?fpr=thepornator"],
      pornxAi: [
        "https://pornx.ai/search?feed=trending&ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=popunder",
      ],
    };
    if (Object.keys(simple).includes(group)) {
      const urls = simple[group];
      const randomIndex = Math.floor(Math.random() * urls.length);
      return urls[randomIndex];
    } else if (group == "candy") {
      const urls = this.getCandyUrls();
      const randomIndex = Math.floor(Math.random() * urls.length);
      return urls[randomIndex];
    } else if (group == "beeg") {
      const randomIndex = Math.floor(Math.random() * beegPathList.length);
      return beegBaseUrl + beegPathList[randomIndex];
    }
    throw Error(
      `A problem occurs during popunder url retrieval. Unknown grou '${group}'`
    );
  }

  getCandyUrls() {
    const navigatorLang = navigator.language || navigator.userLanguage;
    const targetLanguages = [
      "fr-FR",
      "en-AU",
      "en-CA",
      "fr-CA",
      "de-DE",
      "it-IT",
      "ia-JP",
      "nl-NL",
      "en-NZ",
      "sv-SE",
      "en-GB",
      "en-US",
    ];
    if (targetLanguages.includes(navigatorLang)) {
      return [
        "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=popunder&sub2=base",
        "https://landing.candynetwork.ai/elara?var_1=cmai_realistic_01.jpg&var_2=cmai_anime_01.jpg&gender=female&uid=6&oid=2&affid=53&source_id=thepornator&sub1=popunder&sub2=funnel",
      ];
    }
    return ["https://candy.ai?via=maxime85"];
  }
}
