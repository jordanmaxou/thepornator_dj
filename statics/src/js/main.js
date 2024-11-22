import "../scss/styles.scss";
// import * as bootstrap from "bootstrap";
import { initPages } from "./pages/index.js";

const deepmodeTargetUrl = "https://deepmode.com?fpr=thepornator";
const pornxaiTargetUrl =
  "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner";
const pornxaiTargetUrl_feed =
  "https://pornx.ai/search?ref=nmzkmjl&tap_s=4004563-883473&feed=trending&tm_campaign=banner";
const eroplayaiTargetUrl = "https://eroplay.ai/?via=maxime";
const pornworksTargetUrl = "https://pornworks.ai/?refid=thepornator_com";
const candyaiTargetUrl = "https://candy.ai?via=maxime85";
var candyaiEverflowclientTargetUrl1 =
  "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base";
var candyaiEverflowclientTargetUrl2 =
  "https://landing.candynetwork.ai/elara?var_1=cmai_realistic_01.jpg&var_2=cmai_anime_01.jpg&gender=female&uid=6&oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=funnel";
const bestfaceswapTargetUrl =
  "https://www.bestfaceswap.ai/?utm_source=aff-tpnator&utm_campaign=banner";
const createpornTargetUrl =
  "https://www.createporn.com?ref=8a5816867207e9e547064c96ccb73fa5";
const userLanguage = navigator.language || navigator.userLanguage;
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
if (!targetLanguages.includes(userLanguage)) {
  candyaiEverflowclientTargetUrl1 = candyaiTargetUrl;
  candyaiEverflowclientTargetUrl2 = candyaiTargetUrl;
}
var arrayBanners = [
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://links.verotel.com/resellerbanner?vercode=9804000001034858%3A9804000001357861&websitenr=106321",
    imagename: "en_mobile_cumshotbox1.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai1.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai2.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai3.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai4.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai5.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai6.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai7.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures1.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures2.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://www.createporn.com?ref=8a5816867207e9e547064c96ccb73fa5",
    imagename: "en_mobile_xpictures3.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures4.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures5.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures6.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://www.createporn.com?ref=8a5816867207e9e547064c96ccb73fa5",
    imagename: "en_mobile_xpictures7.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures8.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://www.createporn.com?ref=8a5816867207e9e547064c96ccb73fa5",
    imagename: "en_mobile_xpictures9.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures10.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures11.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures12.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl: "https://pornworks.ai/?refid=thepornator_com",
    imagename: "en_mobile_xpictures13.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures14.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures15.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures16.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl: "https://pornworks.ai/?refid=thepornator_com",
    imagename: "en_mobile_xpictures17.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures18.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl: "https://pornworks.ai/?refid=thepornator_com",
    imagename: "en_mobile_xpictures19.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures20.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures21.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl: "https://pornworks.ai/?refid=thepornator_com",
    imagename: "en_mobile_xpictures22.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures23.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures24.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures18.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures19.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures20.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures21.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://www.createporn.com?ref=8a5816867207e9e547064c96ccb73fa5",
    imagename: "en_mobile_xpictures22.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures23.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_xpictures24.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai_custom1.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_pornxai_custom1.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_pornxai1.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_pornxai2.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_pornxai3.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_pornxai4.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_pornxai5.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_pornxai6.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_xpictures1.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_xpictures2.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_xpictures3.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_xpictures4.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_xpictures5.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_xpictures6.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_xpictures7.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_xpictures8.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_xpictures9.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl: "https://deepmode.com?fpr=thepornator",
    imagename: "en_desktop_porngenart1.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_desktop_porngenart2.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl: "https://deepmode.com?fpr=thepornator",
    imagename: "en_desktop_porngenart3.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl: "https://pornworks.ai/?refid=thepornator_com",
    imagename: "en_desktop_porngenart4.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl: "https://pornworks.ai/?refid=thepornator_com",
    imagename: "en_desktop_porngenart5.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl: "https://pornworks.ai/?refid=thepornator_com",
    imagename: "en_mobile_porngenart1.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl: "https://pornworks.ai/?refid=thepornator_com",
    imagename: "en_mobile_porngenart2.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle",
    targetUrl: "https://pornworks.ai/?refid=thepornator_com",
    imagename: "en_mobile_porngenart3.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl: "https://pornworks.ai/?refid=thepornator_com",
    imagename: "en_mobile_porngenart4.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl: "https://pornworks.ai/?refid=thepornator_com",
    imagename: "en_mobile_porngenart5.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai10.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai11.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai12.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai13.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai14.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://pornx.ai/?ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=banner",
    imagename: "en_mobile_pornxai15.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base",
    imagename: "en_mobile_candy1.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base",
    imagename: "en_mobile_candy2.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://landing.candynetwork.ai/elara?var_1=cmai_realistic_01.jpg&var_2=cmai_anime_01.jpg&gender=female&uid=6&oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=funnel",
    imagename: "en_mobile_candy3.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://landing.candynetwork.ai/elara?var_1=cmai_realistic_01.jpg&var_2=cmai_anime_01.jpg&gender=female&uid=6&oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=funnel",
    imagename: "en_mobile_candy4.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base",
    imagename: "en_mobile_candy5.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base",
    imagename: "en_mobile_candy6.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base",
    imagename: "en_mobile_candy7.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://landing.candynetwork.ai/elara?var_1=cmai_realistic_01.jpg&var_2=cmai_anime_01.jpg&gender=female&uid=6&oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=funnel",
    imagename: "en_mobile_candy8.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base",
    imagename: "en_mobile_candy9.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://landing.candynetwork.ai/elara?var_1=cmai_realistic_01.jpg&var_2=cmai_anime_01.jpg&gender=female&uid=6&oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=funnel",
    imagename: "en_mobile_candy10.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl:
      "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base",
    imagename: "en_mobile_candy11.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle|bottom",
    targetUrl:
      "https://landing.candynetwork.ai/elara?var_1=cmai_realistic_01.jpg&var_2=cmai_anime_01.jpg&gender=female&uid=6&oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=funnel",
    imagename: "en_desktop_candy1.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle|bottom",
    targetUrl:
      "https://landing.candynetwork.ai/elara?var_1=cmai_realistic_01.jpg&var_2=cmai_anime_01.jpg&gender=female&uid=6&oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=funnel",
    imagename: "en_desktop_candy2.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle|bottom",
    targetUrl:
      "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base",
    imagename: "en_desktop_candy3.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle|bottom",
    targetUrl:
      "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base",
    imagename: "en_desktop_candy4.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle|bottom",
    targetUrl:
      "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base",
    imagename: "en_desktop_candy5.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=base",
    imagename: "en_desktop_candy6.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://landing.candynetwork.ai/elara?var_1=cmai_realistic_01.jpg&var_2=cmai_anime_01.jpg&gender=female&uid=6&oid=2&affid=53&source_id=thepornator&sub1=banner&sub2=funnel",
    imagename: "en_desktop_candy7.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl: "https://eroplay.ai/?via=maxime",
    imagename: "en_mobile_europlayai1.jpg",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "middle|bottom",
    targetUrl: "https://eroplay.ai/?via=maxime",
    imagename: "en_mobile_europlayai2.jpg",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle|bottom",
    targetUrl: "https://eroplay.ai/?via=maxime",
    imagename: "en_all_europlayai1.jpg",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle|bottom",
    targetUrl: "https://eroplay.ai/?via=maxime",
    imagename: "en_all_europlayai2.jpg",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl: "https://eroplay.ai/?via=maxime",
    imagename: "en_all_europlayai1.jpg",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl: "https://eroplay.ai/?via=maxime",
    imagename: "en_all_europlayai2.jpg",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://www.bestfaceswap.ai/?utm_source=aff-tpnator&utm_campaign=banner",
    imagename: "en_desktop_bestfaceswap1.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle|bottom",
    targetUrl:
      "https://www.bestfaceswap.ai/?utm_source=aff-tpnator&utm_campaign=banner",
    imagename: "en_mobile_bestfaceswap1.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle|bottom",
    targetUrl:
      "https://www.bestfaceswap.ai/?utm_source=aff-tpnator&utm_campaign=banner",
    imagename: "en_mobile_bestfaceswap2.gif",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "desktop",
    zone: "top|middle|bottom",
    targetUrl:
      "https://www.createporn.com?ref=8a5816867207e9e547064c96ccb73fa5",
    imagename: "en_desktop_creatorporn1.webp",
  },
  {
    weight: 1,
    lang: "en|fr",
    device: "mobile",
    zone: "top|middle|bottom",
    targetUrl:
      "https://www.createporn.com?ref=8a5816867207e9e547064c96ccb73fa5",
    imagename: "en_mobile_creatorporn1.webp",
  },
];

function getRandomUrl(urls) {
  let randomIndex = Math.floor(Math.random() * urls.length);
  return urls[randomIndex];
}
function getRandomUrlGroup(groups, groupWeights) {
  const totalWeight = Object.values(groupWeights).reduce(
    (total, weight) => total + weight,
    0
  );
  let randomNum = Math.random() * totalWeight;
  for (const group in groupWeights) {
    randomNum -= groupWeights[group];
    if (randomNum <= 0) {
      return groups[group];
    }
  }
}
window.addEventListener("DOMContentLoaded", function () {
  if (document.cookie.indexOf("disclaimer-shown=true") === -1) {
    document.getElementById("disclaimer-popup").style.display = "block";
    var script = document.createElement("script");
    script.setAttribute("data-cfasync", "false");
    script.setAttribute("type", "text/javascript");
    script.setAttribute("src", "/assets/js/bypass.js");
    document.head.appendChild(script);
    var script = document.createElement("script");
    script.setAttribute("onerror", "vbelsrjq()");
    script.setAttribute("data-cfasync", "false");
    script.setAttribute("type", "text/javascript");
    script.setAttribute(
      "src",
      "//blurbreimbursetrombone.com/aas/r45d/vki/2035380/de2159a9.js"
    );
    document.head.appendChild(script);
    var date = new Date();
    date.setTime(date.getTime() + 1 * 24 * 60 * 60 * 1000);
    var expires = "; expires=" + date.toGMTString();
    document.cookie = "disclaimer-shown=true" + expires + "; path=/";
  }
  document
    .getElementById("disclaimer-agree-button")
    .addEventListener("click", function () {
      var newTab = window.open(window.location.href, "_blank");
      newTab.focus();
      const userLanguage = navigator.language || navigator.userLanguage;
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
      var urlsCandySelect = [
        "https://candy.ai/?oid=2&affid=53&source_id=thepornator&sub1=popunder&sub2=base",
        "https://landing.candynetwork.ai/elara?var_1=cmai_realistic_01.jpg&var_2=cmai_anime_01.jpg&gender=female&uid=6&oid=2&affid=53&source_id=thepornator&sub1=popunder&sub2=funnel",
      ];
      if (!targetLanguages.includes(userLanguage)) {
        urlsCandySelect = ["https://candy.ai?via=maxime85"];
      }
      const urlGroups = {
        urlsBeeg: [
          "https://beeg.link/-0333723745538036",
          "https://beeg.link/-0932594053864920",
          "https://beeg.link/-0974584459268661",
          "https://beeg.link/-0374363204235977",
          "https://beeg.link/-0672928029051124",
          "https://beeg.link/-0696030337427871?t=790-965",
          "https://beeg.link/-0125379762004643?t=1534-1774",
          "https://beeg.link/-0112552416516133?t=655-925",
          "https://beeg.link/-0903810159927361?t=286-959",
          "https://beeg.link/-0386364884397428?t=626-1049",
          "https://beeg.link/-0260729752001010?t=2210-2654",
          "https://beeg.link/-0210899175270318?t=133-558",
          "https://beeg.link/-0119154677548835?t=351-599",
          "https://beeg.link/-0445317237094517",
          "https://beeg.link/-0417986712258649",
          "https://beeg.link/-0975273186178295",
          "https://beeg.link/-0292619678667922",
          "https://beeg.link/-0570412399202511",
          "https://beeg.link/-0315858969310949",
          "https://beeg.link/-0857512346428734",
          "https://beeg.link/-0241802508204847",
          "https://beeg.link/-0868056170326847",
          "https://beeg.link/-0762776719739620",
          "https://beeg.link/-0547863108945549",
          "https://beeg.link/-0183932926446266",
          "https://beeg.link/-0699550742062494",
          "https://beeg.link/-0246166175420267",
          "https://beeg.link/-0476889418139911",
          "https://beeg.link/-0963177313336462",
          "https://beeg.link/-0861370890925474",
          "https://beeg.link/-0912805444492406",
          "https://beeg.link/-0473984587205923",
          "https://beeg.link/-0380327972670026",
          "https://beeg.link/-0905232886772328",
          "https://beeg.link/-0649924676216170",
          "https://beeg.link/-0548856771185741",
          "https://beeg.link/-0647416647981184?t=744-1041",
          "https://beeg.link/-0244664726172804?t=1018-1442",
          "https://beeg.link/-0524739609227720?t=1687-1924",
          "https://beeg.link/-0422106531218939?t=670-900",
          "https://beeg.link/-0320231154813177?t=1305-1666",
          "https://beeg.link/-0676822257377438?t=688-966",
          "https://beeg.link/-0572640772668440?t=2843-3039",
          "https://beeg.link/-0260608444167019?t=385-633",
          "https://beeg.link/-0319209003344810?t=689-1043",
          "https://beeg.link/-0146576450464294",
          "https://beeg.link/-0457264087484005",
          "https://beeg.link/-0119299614975812",
          "https://beeg.link/-0422581119384649",
          "https://beeg.link/-0931443394199862",
          "https://beeg.link/-0791551264241681",
          "https://beeg.link/-0676560220961817",
          "https://beeg.link/-0542224687542182",
          "https://beeg.link/-0571146913091077",
          "https://beeg.link/-0949020437453251?t=267-846",
          "https://beeg.link/-0932511282894685?t=890-1070",
          "https://beeg.link/-0509007879657268?t=456-694",
          "https://beeg.link/-0302100015784586?t=1261-1538",
          "https://beeg.link/-0472848299996387?t=412-674",
          "https://beeg.link/-0480656613255482?t=1267-1663",
          "https://beeg.link/-0685244802506405?t=1114-1370",
          "https://beeg.link/-0906164192604186?t=831-1207",
          "https://beeg.link/-0907689234300591?t=923-1607",
          "https://beeg.link/-0277889170641496?t=1060-1271",
          "https://beeg.link/-0277889170641496?t=747-1060",
          "https://beeg.link/-0300262780952739",
          "https://beeg.link/-0728440356751473",
          "https://beeg.link/-0229243716671896",
          "https://beeg.link/-0268491327563886",
          "https://beeg.link/-0779040103500590",
          "https://beeg.link/-0750640484042767",
          "https://beeg.link/-0913119861015448",
          "https://beeg.link/-0739665553494959",
          "https://beeg.link/-0524426187005020",
          "https://beeg.link/-0643726602208421",
          "https://beeg.link/-0797992219521508",
          "https://beeg.link/-0799088645731631",
          "https://beeg.link/-0690264053791637",
          "https://beeg.link/-0748029477729704",
          "https://beeg.link/-0974623812003316",
          "https://beeg.link/-0384687029971363",
          "https://beeg.link/-0638530897809561",
          "https://beeg.link/-0439366008249711",
          "https://beeg.link/-0915938138377068",
          "https://beeg.link/-0822180690912364",
          "https://beeg.link/-0182042791751398",
          "https://beeg.link/-0766369177113388",
          "https://beeg.link/-0365685528491998",
          "https://beeg.link/-0112764915346344",
          "https://beeg.link/-0649284995602195",
          "https://beeg.link/-0339814266598941",
          "https://beeg.link/-0672226514361616",
          "https://beeg.link/-0497028137617747",
          "https://beeg.link/-0192996495613810",
          "https://beeg.link/-0489189417360519",
          "https://beeg.link/-0300358854352776",
          "https://beeg.link/-0964686700782533",
          "https://beeg.link/-0225616962681459",
          "https://beeg.link/-0951922898795270",
          "https://beeg.link/-0265196467925764",
          "https://beeg.link/-0459765527754067",
          "https://beeg.link/-0775311349412902?t=1608-1819",
          "https://beeg.link/-0636771112815845?t=522-922",
          "https://beeg.link/-0942875288145461?t=1180-1443",
          "https://beeg.link/-0311141544824662?t=292-532",
          "https://beeg.link/-0632707835931836",
          "https://beeg.link/-0123068593683681",
          "https://beeg.link/-0510133559558072",
          "https://beeg.link/-0176271944133529",
          "https://beeg.link/-0631530260232931",
          "https://beeg.link/-0549865308494832",
          "https://beeg.link/-0533151643827369?t=821-1094",
          "https://beeg.link/-0816736124662747",
          "https://beeg.link/-0328501352805359",
          "https://beeg.link/-0106970559518828",
          "https://beeg.link/-0204874853183821",
          "https://beeg.link/-0487869527882146",
          "https://beeg.link/-0365804673167253",
          "https://beeg.link/-0123298363843590",
          "https://beeg.link/-0617896257676239",
          "https://beeg.link/-0911654314858327",
          "https://beeg.link/-0781019584863120",
          "https://beeg.link/-0816478134815566",
          "https://beeg.link/-0343781985818379",
          "https://beeg.link/-0688010174406769",
          "https://beeg.link/-0325793773655518",
          "https://beeg.link/-0173822715332879",
          "https://beeg.link/-0117878800829212",
          "https://beeg.link/-0471939342478057",
          "https://beeg.link/-0181348955278235",
          "https://beeg.link/-0130509571198686",
          "https://beeg.link/-0605415541992573",
          "https://beeg.link/-0306236311345861",
          "https://beeg.link/-0781178536506968",
          "https://beeg.link/-0305343172657465",
          "https://beeg.link/-0673210713729728",
          "https://beeg.link/-0262383787298729",
          "https://beeg.link/-0463582181144514",
          "https://beeg.link/-0254663351597878",
          "https://beeg.link/-0740814873225604",
          "https://beeg.link/-0172504881783240",
          "https://beeg.link/-0223280371061707",
          "https://beeg.link/-0320307750051219",
          "https://beeg.link/-0894397574695709",
          "https://beeg.link/-0946936539995278",
          "https://beeg.link/-0872508578046749",
          "https://beeg.link/-0723717573510976",
          "https://beeg.link/-0833055573304225",
          "https://beeg.link/-0858741915231079",
          "https://beeg.link/-0407661284480908?t=1678-1995",
          "https://beeg.link/-0266767996103419?t=1731-2315",
          "https://beeg.link/-0563129477425624?t=1-863",
          "https://beeg.link/-0563129477425624?t=1248-1670",
          "https://beeg.link/-0578644883378372?t=1166-1448",
          "https://beeg.link/-0903640699414556?t=1251-1809",
          "https://beeg.link/-0903640699414556?t=1143-1396",
          "https://beeg.link/-0903640699414556?t=2254-2974",
          "https://beeg.link/-0106614021705639?t=1123-1413",
          "https://beeg.link/-0397444441676944?t=822-1710",
          "https://beeg.link/-0608380444794106?t=2035-2485",
          "https://beeg.link/-0273554880322947?t=881-1190",
          "https://beeg.link/-0161240331703039?t=1865-2207",
          "https://beeg.link/-0943029792052417?t=271-533",
          "https://beeg.link/-0324491484544177",
          "https://beeg.link/-0329832524068246",
          "https://beeg.link/-0501520891065352",
          "https://beeg.link/-0395281946731778",
          "https://beeg.link/-0886616784120005",
          "https://beeg.link/-0689954428179375",
          "https://beeg.link/-0300130108010439",
          "https://beeg.link/-0643693045989021",
          "https://beeg.link/-0994727841530156",
          "https://beeg.link/-0577798135020345",
          "https://beeg.link/-0402200258506834",
          "https://beeg.link/-0458615406367315",
          "https://beeg.link/-0243623059318321",
          "https://beeg.link/-0118673548610728?t=870-1249",
          "https://beeg.link/-0651453994460975?t=138-657",
          "https://beeg.link/-0364740577804888?t=1940-2301",
          "https://beeg.link/-0721493211509919?t=1837-2101",
          "https://beeg.link/-0721493211509919?t=234-868",
          "https://beeg.link/-0660117431587441?t=401-932",
          "https://beeg.link/-0580075046105056?t=2286-2817",
          "https://beeg.link/-0147781740404592?t=2271-2637",
          "https://beeg.link/-0147781740404592?t=536-1202",
          "https://beeg.link/-0114372282755230?t=1750-2231",
          "https://beeg.link/-0114372282755230?t=1312-1745",
          "https://beeg.link/-0336449455871300?t=1040-1276",
          "https://beeg.link/-0208747451086737",
          "https://beeg.link/-0326548973057136",
          "https://beeg.link/-0177487216925557",
          "https://beeg.link/-0683529128023627",
          "https://beeg.link/-0318782080198819",
          "https://beeg.link/-0775585094671034",
          "https://beeg.link/-0804368698055460?t=9-396",
          "https://beeg.link/-0804368698055460?t=1877-2160",
          "https://beeg.link/-0369727948950597?t=996-1267",
          "https://beeg.link/-0539114911030155?t=31-427",
          "https://beeg.link/-0539114911030155?t=536-772",
          "https://beeg.link/-0420172425904647?t=1370-1649",
          "https://beeg.link/-0420172425904647?t=47-621",
          "https://beeg.link/-0505373802365111?t=1989-2342",
          "https://beeg.link/-0505373802365111?t=212-976",
          "https://beeg.link/-0807151309598433?t=15-765",
          "https://beeg.link/-0807151309598433?t=582-1048",
          "https://beeg.link/-0807151309598433?t=1209-1464",
          "https://beeg.link/-0116064237570014?t=557-965",
          "https://beeg.link/-0116064237570014?t=321-937",
          "https://beeg.link/-0116064237570014?t=967-1382",
          "https://beeg.link/-0888498923356656?t=207-773",
          "https://beeg.link/-0888498923356656?t=417-777",
          "https://beeg.link/-0770041954812649?t=1580-2134",
          "https://beeg.link/-0233822033855041?t=1127-1352",
          "https://beeg.link/-0229394711432325?t=2268-2482",
          "https://beeg.link/-0585319937930430?t=2671-3037",
          "https://beeg.link/-0616809367554480",
          "https://beeg.link/-0543849542866467",
          "https://beeg.link/-0188586505376805",
          "https://beeg.link/-0709638054765230",
          "https://beeg.link/-0951738567717129",
          "https://beeg.link/-0794691903367915",
          "https://beeg.link/-0559556258167396",
          "https://beeg.link/-0424948896065178",
          "https://beeg.link/-0593185193992697",
          "https://beeg.link/-0238176335962132",
          "https://beeg.link/-0534037194512743",
          "https://beeg.link/-0290705963306121",
          "https://beeg.link/-0827734273717897?t=898-1261",
          "https://beeg.link/-0253493369958857?t=2295-2687",
          "https://beeg.link/-0183659356718683?t=926-1562",
          "https://beeg.link/-0456007796433810?t=44-537",
          "https://beeg.link/-0856937025910052?t=537-973",
          "https://beeg.link/-0856937025910052?t=1181-1540",
          "https://beeg.link/-0303977137310856?t=1479-1893",
          "https://beeg.link/-0303977137310856?t=1900-2170",
          "https://beeg.link/-0764071434355608?t=678-1235",
          "https://beeg.link/-0764071434355608?t=677-1234",
          "https://beeg.link/-0196961330058039?t=2660-2872",
          "https://beeg.link/-0727567244521884?t=2629-3318",
          "https://beeg.link/-0935639682160513?t=994-1504",
          "https://beeg.link/-0725352220558638?t=1632-1919",
          "https://beeg.link/-0155879948681305?t=336-689",
          "https://beeg.link/-0478824477540073",
          "https://beeg.link/-0713329195576184",
          "https://beeg.link/-0921183742904297",
          "https://beeg.link/-0409046464157504",
          "https://beeg.link/-0801690309166574",
          "https://beeg.link/-0907617989616821",
          "https://beeg.link/-0324003030981392",
          "https://beeg.link/-0464324335249648",
          "https://beeg.link/-0793475566378382",
          "https://beeg.link/-0853210429165315",
          "https://beeg.link/-0172128999413076",
          "https://beeg.link/-0236107745033436",
          "https://beeg.link/-0656054022338930",
          "https://beeg.link/-0391021209980027",
          "https://beeg.link/-0344936185549117",
          "https://beeg.link/-0278126504186367",
          "https://beeg.link/-0532021099481162?t=615-987",
          "https://beeg.link/-0532021099481162?t=1754-2120",
          "https://beeg.link/-0275263476894544?t=1734-1967",
          "https://beeg.link/-0742342853361421?t=242-597",
          "https://beeg.link/-0742342853361421?t=982-1229",
          "https://beeg.link/-0626845085536282?t=1129-1534",
          "https://beeg.link/-0626845085536282?t=2089-2359",
          "https://beeg.link/-0642824791832982?t=578-965",
          "https://beeg.link/-0642824791832982?t=24-575",
          "https://beeg.link/-0202240657783597?t=254-509",
          "https://beeg.link/-0202240657783597?t=737-1422",
          "https://beeg.link/-0156352591441513?t=2117-2298",
          "https://beeg.link/-0237940062459427?t=303-652",
          "https://beeg.link/-0923630637862414?t=1107-1371",
          "https://beeg.link/-0956991039903562?t=14-438",
          "https://beeg.link/-0143006279297361?t=728-1275",
          "https://beeg.link/-0827121263716098?t=1173-1380",
          "https://beeg.link/-0757302266324222?t=528-904",
          "https://beeg.link/-0541125152710724?t=304-494",
          "https://beeg.link/-0843260396178294?t=266-510",
          "https://beeg.link/-0733376954552646?t=1329-1571",
          "https://beeg.link/-0871040496283159",
          "https://beeg.link/-0390114858618206",
          "https://beeg.link/-0353787876908038",
          "https://beeg.link/-0850064580418614",
          "https://beeg.link/-0713296110034109",
          "https://beeg.link/-0167748057668678",
          "https://beeg.link/-0555942979070808",
          "https://beeg.link/-0730247275325009",
          "https://beeg.link/-0720578907804578",
          "https://beeg.link/-0886082759709413",
          "https://beeg.link/-0323835958036717",
          "https://beeg.link/-0153321733481093?t=167-883",
          "https://beeg.link/-0153321733481093?t=719-1065",
          "https://beeg.link/-0567115715394856?t=507-1109",
          "https://beeg.link/-0567115715394856?t=14-431",
          "https://beeg.link/-0169266434986589?t=1291-2049",
          "https://beeg.link/-0169266434986589?t=381-1141",
          "https://beeg.link/-0169266434986589?t=1294-1612",
          "https://beeg.link/-0639246920465579?t=65-460",
          "https://beeg.link/-0171396874451074?t=1228-1498",
          "https://beeg.link/-0818958476910755?t=241-849",
          "https://beeg.link/-0818958476910755?t=179-847",
          "https://beeg.link/-0899230861751415?t=2001-2203",
          "https://beeg.link/-0324603017579025?t=1046-1750",
          "https://beeg.link/-0400232060393805?t=996-1276",
          "https://beeg.link/-0112335328923449?t=1220-1723",
          "https://beeg.link/-0295577057992511?t=1618-1972",
          "https://beeg.link/-0654702713006993?t=544-1339",
          "https://beeg.link/-0654702713006993?t=1341-1818",
          "https://beeg.link/-0304710284569590?t=651-922",
          "https://beeg.link/-0197337094330579",
          "https://beeg.link/-0230674461403729",
          "https://beeg.link/-0541323101320767",
          "https://beeg.link/-0185973649945041",
          "https://beeg.link/-0918879140894382",
          "https://beeg.link/-0184023991118182",
          "https://beeg.link/-0144478034384157",
          "https://beeg.link/-0829706589663650",
          "https://beeg.link/-0141283717536796",
          "https://beeg.link/-0788562546756061",
          "https://beeg.link/-0524869059047747",
          "https://beeg.link/-0740372594018898",
          "https://beeg.link/-0762697615178579",
          "https://beeg.link/-0546416768699660",
          "https://beeg.link/-0680339045907065",
          "https://beeg.link/-0366474404865155",
          "https://beeg.link/-0610692636599941",
          "https://beeg.link/-0522622159159419",
          "https://beeg.link/-0308683313945329",
          "https://beeg.link/-0875064536418652",
          "https://beeg.link/-0309168001388523",
          "https://beeg.link/-0306658622610118",
          "https://beeg.link/-0798513195768938",
          "https://beeg.link/-0674370674654086",
          "https://beeg.link/-0638884261072960",
          "https://beeg.link/-0653976404247956",
          "https://beeg.link/-0629022552813330",
          "https://beeg.link/-0814235628620783",
          "https://beeg.link/-0489388144620103",
          "https://beeg.link/-0445227448200422",
          "https://beeg.link/-0126730587301971",
          "https://beeg.link/-0999496093172317",
          "https://beeg.link/-0918100919421697",
          "https://beeg.link/-0105119944367396",
          "https://beeg.link/-0622269221882255",
          "https://beeg.link/-0745042765889834",
          "https://beeg.link/-0446032405953742",
          "https://beeg.link/-0465511872302316",
          "https://beeg.link/-0900958520920608",
          "https://beeg.link/-0640190896721817",
          "https://beeg.link/-0410070760242327",
          "https://beeg.link/-0748543765567148",
          "https://beeg.link/-0497155804854120",
          "https://beeg.link/-0897121920740408",
          "https://beeg.link/-0836189527984725",
          "https://beeg.link/-0948701418851351",
          "https://beeg.link/-0357434881788310",
          "https://beeg.link/-0717267779550128",
          "https://beeg.link/-0247969085215343",
          "https://beeg.link/-01032789099?t=1397-1997",
          "https://beeg.link/-01032789099?t=1631-2231",
          "https://beeg.link/-01032789099?t=1223-1870",
          "https://beeg.link/-01032789099?t=2117-2717",
          "https://beeg.link/-01032789099?t=893-1493",
          "https://beeg.link/-01032789099?t=439-1039",
          "https://beeg.link/-01032789099?t=31-631",
          "https://beeg.link/-01650381383?t=1247-1600",
          "https://beeg.link/-01444696610?t=146-746",
          "https://beeg.link/-01444696610?t=46-646",
          "https://beeg.link/-01444696610?t=499-1099",
          "https://beeg.link/-01444696610?t=399-620",
          "https://beeg.link/-01444696610?t=268-868",
          "https://beeg.link/-01444696610?t=219-819",
          "https://beeg.link/-01877723999?t=740-928",
          "https://beeg.link/-01877723999?t=15-615",
          "https://beeg.link/-01877723999?t=745-1345",
          "https://beeg.link/-01218962775?t=445-1045",
          "https://beeg.link/-01218962775?t=725-1105",
          "https://beeg.link/-01218962775?t=753-1353",
          "https://beeg.link/-01218962775?t=1199-1799",
          "https://beeg.link/-01218962775?t=151-751",
          "https://beeg.link/-0924299552043270?t=832-1103",
          "https://beeg.link/-0924299552043270?t=218-960",
          "https://beeg.link/-0483439640593362",
          "https://beeg.link/-0835950507629594",
          "https://beeg.link/-0495475485342378",
          "https://beeg.link/-0384900426593349",
          "https://beeg.link/-0232044171129128",
          "https://beeg.link/-0996022109872784",
          "https://beeg.link/-0381451786445950",
          "https://beeg.link/-0909673528201236",
          "https://beeg.link/-0136990541576633?t=932-1757",
          "https://beeg.link/-0390908776212619?t=917-1180",
          "https://beeg.link/-0866017208720187?t=820-1167",
          "https://beeg.link/-0553198581708392?t=831-1042",
          "https://beeg.link/-0588295910875418?t=306-1374",
          "https://beeg.link/-0588295910875418?t=493-1192",
          "https://beeg.link/-0512305457772212?t=6-814",
          "https://beeg.link/-0512305457772212?t=374-570",
          "https://beeg.link/-0126474351587834?t=582-831",
          "https://beeg.link/-0323934051736912?t=2077-2410",
          "https://beeg.link/-0323934051736912?t=1359-1957",
          "https://beeg.link/-0145184687028113?t=35-637",
          "https://beeg.link/-0145184687028113?t=474-815",
          "https://beeg.link/-0529696925398859?t=1372-2038",
          "https://beeg.link/-0650940375518263?t=1455-1697",
          "https://beeg.link/-0379486928489790?t=74-435",
          "https://beeg.link/-0261035821231570?t=1033-1333",
          "https://beeg.link/-0983763667910281?t=1613-1872",
          "https://beeg.link/-0693029882333164?t=64-301",
          "https://beeg.link/-0575760950917577?t=2332-2705",
          "https://beeg.link/-0575760950917577?t=447-1329",
          "https://beeg.link/-0535696302164968?t=391-648",
          "https://beeg.link/-0222099636424778?t=2747-2942",
          "https://beeg.link/-0726058358798048",
          "https://beeg.link/-0460064069792492",
          "https://beeg.link/-0192831417413257",
          "https://beeg.link/-0499273465602187",
          "https://beeg.link/-0831573955644008",
          "https://beeg.link/-0681707281468110",
          "https://beeg.link/-0822221232696183",
          "https://beeg.link/-0619751228792853",
          "https://beeg.link/-0719544999530561",
          "https://beeg.link/-0750173303848573?t=1040-1636",
          "https://beeg.link/-0972845981544937?t=2322-2619",
          "https://beeg.link/-0967083777847534?t=2166-2502",
          "https://beeg.link/-0349177069880320?t=204-454",
          "https://beeg.link/-0659785556918731?t=273-1231",
          "https://beeg.link/-0659785556918731?t=964-1228",
          "https://beeg.link/-0362218272972623?t=870-1329",
          "https://beeg.link/-0108978263822354?t=735-976",
          "https://beeg.link/-0669297250282632?t=842-1105",
          "https://beeg.link/-0646286090191654?t=318-1091",
          "https://beeg.link/-0847880964286070?t=661-1044",
          "https://beeg.link/-0140866615936644",
          "https://beeg.link/-0239151282425985",
          "https://beeg.link/-0367760385175266",
          "https://beeg.link/-0872910820545090",
          "https://beeg.link/-0226585839663967",
          "https://beeg.link/-0586450106017071?t=619-1170",
          "https://beeg.link/-0976113802117345?t=1198-1776",
          "https://beeg.link/-0808403323817635?t=160-834",
          "https://beeg.link/-0808403323817635?t=672-1104",
          "https://beeg.link/-0127323630509045?t=823-1302",
          "https://beeg.link/-0249150959508232?t=1758-2161",
          "https://beeg.link/-0105432367551420?t=1689-2394",
          "https://beeg.link/-0527535314313370?t=176-474",
          "https://beeg.link/-0534175115874039?t=533-1052",
          "https://beeg.link/-0420571032426981?t=603-1001",
          "https://beeg.link/-0768849826020097?t=31-742",
          "https://beeg.link/-0378871752125359?t=171-768",
          "https://beeg.link/-0415273424104497?t=1998-2457",
          "https://beeg.link/-0415273424104497?t=7-674",
          "https://beeg.link/-0659370894238020",
          "https://beeg.link/-0425937363917697",
          "https://beeg.link/-0405572103004709",
          "https://beeg.link/-0643250202230403",
          "https://beeg.link/-0807761790310987",
          "https://beeg.link/-0909063795403475",
          "https://beeg.link/-0520638441725981",
          "https://beeg.link/-0506574577281555",
          "https://beeg.link/-0135929798451619",
          "https://beeg.link/-0765207578488985",
          "https://beeg.link/-0319610913516052",
          "https://beeg.link/-0966212446601134?t=1019-1704",
          "https://beeg.link/-0642206535330254?t=57-538",
          "https://beeg.link/-0262377900185384?t=108-791",
          "https://beeg.link/-0262377900185384?t=16-790",
          "https://beeg.link/-0590665369739008?t=447-1023",
          "https://beeg.link/-0590665369739008?t=645-1059",
          "https://beeg.link/-0396423491256387?t=1884-2294",
          "https://beeg.link/-0931672725607273?t=698-948",
          "https://beeg.link/-0695691189586143?t=803-1040",
          "https://beeg.link/-0640160283185254?t=734-983",
          "https://beeg.link/-0824382660639632?t=961-1217",
          "https://beeg.link/-0493546362465862",
          "https://beeg.link/-0607801159890800",
          "https://beeg.link/-0188877558357064",
          "https://beeg.link/-0472930314809753",
          "https://beeg.link/-0510298416887581",
          "https://beeg.link/-0100853665323468",
          "https://beeg.link/-0979359564182056",
          "https://beeg.link/-0388488564930512",
          "https://beeg.link/-0564689000664521?t=582-837",
          "https://beeg.link/-0195137029092250?t=1793-2027",
          "https://beeg.link/-0861535275802233?t=516-1148",
          "https://beeg.link/-0701082408264060?t=355-604",
          "https://beeg.link/-0277200682227104?t=821-1524",
          "https://beeg.link/-0175364889131715?t=670-905",
          "https://beeg.link/-0301254558381323?t=100-431",
          "https://beeg.link/-0800492567467253?t=1900-2151",
          "https://beeg.link/-0642034212289220?t=602-1429",
          "https://beeg.link/-0301877732257787?t=465-715",
          "https://beeg.link/-0821820104987681",
          "https://beeg.link/-0562037440964088",
          "https://beeg.link/-0866718545544793",
          "https://beeg.link/-0652798738740021",
          "https://beeg.link/-0104843155124637",
          "https://beeg.link/-0100033306808305",
          "https://beeg.link/-0208157748759280",
          "https://beeg.link/-0942704301519416?t=708-1126",
          "https://beeg.link/-0942704301519416?t=331-865",
          "https://beeg.link/-0796405276123946?t=13-661",
          "https://beeg.link/-0796405276123946?t=664-1192",
          "https://beeg.link/-0796405276123946?t=662-1194",
          "https://beeg.link/-0796405276123946?t=1228-1757",
          "https://beeg.link/-01844303841?t=979-1579",
          "https://beeg.link/-01844303841?t=231-831",
          "https://beeg.link/-01844303841?t=995-1245",
          "https://beeg.link/-01844303841?t=1507-2107",
          "https://beeg.link/-01962298399?t=335-739",
          "https://beeg.link/-01962298399?t=6-334",
          "https://beeg.link/-01962298399?t=336-738",
          "https://beeg.link/-01756273396?t=1387-1927",
          "https://beeg.link/-01756273396?t=1131-1671",
          "https://beeg.link/-01756273396?t=1927-2149",
          "https://beeg.link/-01756273396?t=2199-2739",
          "https://beeg.link/-01756273396?t=2806-3346",
          "https://beeg.link/-01756273396?t=1689-2229",
          "https://beeg.link/-01144450717?t=2091-2811",
          "https://beeg.link/-01144450717?t=1595-1881",
          "https://beeg.link/-01144450717?t=1273-1993",
          "https://beeg.link/-01144450717?t=637-1357",
          "https://beeg.link/-0354392769047282",
          "https://beeg.link/-0718890025881848",
          "https://beeg.link/-0908773224580861",
          "https://beeg.link/-0901566258493690",
          "https://beeg.link/-0434959309877203",
          "https://beeg.link/-0772189698253308",
          "https://beeg.link/-0743186759274310",
          "https://beeg.link/-0961771647470509",
          "https://beeg.link/-0588778892784945",
          "https://beeg.link/-0653337284381787",
          "https://beeg.link/-0105110799121938",
          "https://beeg.link/-0892479982424835",
          "https://beeg.link/-0296221131089820",
          "https://beeg.link/-0374183646279900",
          "https://beeg.link/-0862931536355389",
          "https://beeg.link/-0588852196725091",
          "https://beeg.link/-0419569752866938?t=828-1478",
          "https://beeg.link/-0364969211096445?t=91-656",
          "https://beeg.link/-0364969211096445?t=1013-1279",
          "https://beeg.link/-0364969211096445?t=684-1280",
          "https://beeg.link/-02130127000?t=1740-2301",
          "https://beeg.link/-02130127000?t=2973-3275",
          "https://beeg.link/-02130127000?t=202-866",
          "https://beeg.link/-0107728660045566?t=1010-1536",
          "https://beeg.link/-0107728660045566?t=1306-1539",
          "https://beeg.link/-0107728660045566?t=23-617",
          "https://beeg.link/-0107728660045566?t=485-816",
          "https://beeg.link/-0920024036142586?t=1264-1597",
          "https://beeg.link/-0916444280977394?t=930-1201",
          "https://beeg.link/-0487446687445664",
          "https://beeg.link/-0134399943261659",
          "https://beeg.link/-0872930195796107",
          "https://beeg.link/-0407125283155583",
          "https://beeg.link/-0365872510831523",
          "https://beeg.link/-0380004841214174",
          "https://beeg.link/-0397089717808306",
          "https://beeg.link/-0903766854058615",
          "https://beeg.link/-0623436906543807",
          "https://beeg.link/-0251291714888778",
          "https://beeg.link/-0318370318550521",
          "https://beeg.link/-0568800580390367",
          "https://beeg.link/-0388946560051662",
          "https://beeg.link/-0714418537589244",
          "https://beeg.link/-0383748110149341",
          "https://beeg.link/-0980233533307688",
          "https://beeg.link/-0806127820610050",
          "https://beeg.link/-0460763040479458",
          "https://beeg.link/-0849385296197565",
          "https://beeg.link/-0658536431488737",
          "https://beeg.link/-0956593530731358",
          "https://beeg.link/-0854593901029052",
          "https://beeg.link/-0968408409064485",
          "https://beeg.link/-0392760908571368",
          "https://beeg.link/-0494734426975507",
          "https://beeg.link/-0554657641512622",
          "https://beeg.link/-0229387491425013",
          "https://beeg.link/-0168214433819442",
          "https://beeg.link/-0532197116782703",
          "https://beeg.link/-0732958785461409",
          "https://beeg.link/-0245311741714445",
          "https://beeg.link/-0216106476030624",
          "https://beeg.link/-0151673379235396",
          "https://beeg.link/-0345007828841306",
          "https://beeg.link/-0391554912449754",
          "https://beeg.link/-0330385218536618",
          "https://beeg.link/-0193723293103824",
          "https://beeg.link/-0194825057235482",
          "https://beeg.link/-0686452786533427",
          "https://beeg.link/-0624630236502044",
          "https://beeg.link/-0485811322090287",
          "https://beeg.link/-0444974550806893",
          "https://beeg.link/-0634164687223371",
          "https://beeg.link/-0186679816378636",
          "https://beeg.link/-0775636742026095",
          "https://beeg.link/-0131187303418137",
          "https://beeg.link/-0297345647699104",
          "https://beeg.link/-0177923896182744",
          "https://beeg.link/-0472594843055333",
          "https://beeg.link/-0501091673346454",
          "https://beeg.link/-0830975886040182",
          "https://beeg.link/-0477210025631510",
          "https://beeg.link/-0250893743392304",
          "https://beeg.link/-0355351452164090",
          "https://beeg.link/-0133473834617179",
          "https://beeg.link/-0517187580902768",
          "https://beeg.link/-0390461915988607",
          "https://beeg.link/-0799659701285582",
          "https://beeg.link/-0987554188577468",
          "https://beeg.link/-0487388918883983",
          "https://beeg.link/-0320566452779106",
          "https://beeg.link/-0468663685598224",
          "https://beeg.link/-0229740922353973",
          "https://beeg.link/-0655958862078976",
          "https://beeg.link/-0393595099808147",
          "https://beeg.link/-0866096407642316",
          "https://beeg.link/-0349477335397230",
          "https://beeg.link/-0682700289000981",
          "https://beeg.link/-0988057356497519",
          "https://beeg.link/-0697797340851101",
          "https://beeg.link/-0883322386507697",
          "https://beeg.link/-0660932854324358",
          "https://beeg.link/-0612847350863741",
          "https://beeg.link/-0640753867911649",
          "https://beeg.link/-0538195730518342",
          "https://beeg.link/-0156137358071030",
          "https://beeg.link/-0518133727737462",
          "https://beeg.link/-0146529236529286",
          "https://beeg.link/-0196428659016390",
          "https://beeg.link/-0541687780527408",
          "https://beeg.link/-0795094210469555",
          "https://beeg.link/-0714112667253823",
          "https://beeg.link/-0363320727996119",
          "https://beeg.link/-0668598227883819",
          "https://beeg.link/-0595518413756578",
          "https://beeg.link/-0560913185790756",
          "https://beeg.link/-0958300693689799",
          "https://beeg.link/-0384470543364613",
          "https://beeg.link/-0502486698730477",
          "https://beeg.link/-0155487868076001",
          "https://beeg.link/-0276666107280540",
          "https://beeg.link/-0544330707628439",
          "https://beeg.link/-0410038276138525",
          "https://beeg.link/-0381727609141504",
          "https://beeg.link/-0195028090450090",
          "https://beeg.link/-0482658581722602",
          "https://beeg.link/-0398872409677029",
          "https://beeg.link/-0496510965020376",
          "https://beeg.link/-0372198533608411",
          "https://beeg.link/-0743716358823470",
          "https://beeg.link/-0404383975934325",
          "https://beeg.link/-0132530369561915",
          "https://beeg.link/-0904023599798438",
          "https://beeg.link/-0518395881794694",
          "https://beeg.link/-0160520535119964",
          "https://beeg.link/-0639799632239353",
          "https://beeg.link/-0902395031327742",
          "https://beeg.link/-0307105726974894",
          "https://beeg.link/-0134559749951166",
          "https://beeg.link/-0506151497260585",
          "https://beeg.link/-0511566009921346",
          "https://beeg.link/-0283686146339056",
          "https://beeg.link/-0322803434780981",
          "https://beeg.link/-0563378830500948",
          "https://beeg.link/-0772204663855586",
          "https://beeg.link/-0152387961415749",
          "https://beeg.link/-0853058512282781",
          "https://beeg.link/-0753001912655880",
          "https://beeg.link/-0627162500827081",
          "https://beeg.link/-0485112634106185",
          "https://beeg.link/-0652961553333747",
          "https://beeg.link/-0588264869379769",
          "https://beeg.link/-0258760172969360",
          "https://beeg.link/-0286986629923239",
          "https://beeg.link/-0155405169922620",
          "https://beeg.link/-0660281884200999",
          "https://beeg.link/-0540499334437637",
          "https://beeg.link/-0940327419970866",
          "https://beeg.link/-0769802335255428",
          "https://beeg.link/-0381292982470487",
          "https://beeg.link/-0872998418590382",
          "https://beeg.link/-0694375510017846",
          "https://beeg.link/-0273252921277060",
          "https://beeg.link/-0771373245319461",
          "https://beeg.link/-0390899623758640",
          "https://beeg.link/-0608968068576540",
          "https://beeg.link/-0195460381560813",
          "https://beeg.link/-0421974484849185",
          "https://beeg.link/-0733190474035647",
          "https://beeg.link/-0188669579558459",
          "https://beeg.link/-0574892379470305",
          "https://beeg.link/-0678937867036864",
          "https://beeg.link/-0428890263684335",
          "https://beeg.link/-0346331393639541",
          "https://beeg.link/-0764280633444461",
          "https://beeg.link/-0469994200730934",
          "https://beeg.link/-0677132974712123",
          "https://beeg.link/-0941125709947219",
          "https://beeg.link/-0566266736173677",
          "https://beeg.link/-0287153119330696",
          "https://beeg.link/-0408648473462883",
          "https://beeg.link/-0823385867850293",
          "https://beeg.link/-0351769396115253",
          "https://beeg.link/-0610387849958078",
          "https://beeg.link/-0771465572371697",
          "https://beeg.link/-0840472308798930",
          "https://beeg.link/-0736420383770238",
          "https://beeg.link/-0294685849799441",
          "https://beeg.link/-0816864983659103",
          "https://beeg.link/-0848526647004008",
          "https://beeg.link/-0975915268307683",
          "https://beeg.link/-0739969981375160",
          "https://beeg.link/-0964533896863070",
          "https://beeg.link/-0257323509880226",
          "https://beeg.link/-0227993411854976",
          "https://beeg.link/-0436775717309655",
          "https://beeg.link/-0893849571113412",
          "https://beeg.link/-0611953802559254",
          "https://beeg.link/-0989781562729789",
          "https://beeg.link/-0941177434278037",
          "https://beeg.link/-0212641268624862",
          "https://beeg.link/-0197011550079088",
          "https://beeg.link/-0792928918939095",
          "https://beeg.link/-0943757655662089",
          "https://beeg.link/-0112142418233786",
          "https://beeg.link/-0289534060838196",
          "https://beeg.link/-0566869559863251",
          "https://beeg.link/-0826659886901631",
          "https://beeg.link/-0433106651324528",
          "https://beeg.link/-0886965074973641",
          "https://beeg.link/-0616815807713211",
          "https://beeg.link/-0177295349343727",
          "https://beeg.link/-0137899009607102",
          "https://beeg.link/-0228200305972667",
          "https://beeg.link/-0513040115459764",
          "https://beeg.link/-0100184444126401",
          "https://beeg.link/-0539139444696712",
          "https://beeg.link/-0194157893563460",
          "https://beeg.link/-0523518215400849",
          "https://beeg.link/-0741611157032114",
          "https://beeg.link/-0727871960089497",
          "https://beeg.link/-0142839584831084",
          "https://beeg.link/-0966419780004202",
          "https://beeg.link/-0453401360419831",
          "https://beeg.link/-0467379540120287",
          "https://beeg.link/-0281846561470816",
          "https://beeg.link/-0781254850094210",
          "https://beeg.link/-0882339914226817",
          "https://beeg.link/-0931130238421138",
          "https://beeg.link/-0921277330733811",
          "https://beeg.link/-0850049335525931",
          "https://beeg.link/-0469498747252072",
          "https://beeg.link/-0879742355949465",
          "https://beeg.link/-0230970362470698",
          "https://beeg.link/-0950655512031109",
          "https://beeg.link/-0831895152397494",
          "https://beeg.link/-0227896517486964",
          "https://beeg.link/-0423138247395399",
          "https://beeg.link/-0703025279655986",
          "https://beeg.link/-0777035772374125",
          "https://beeg.link/-0652699202138908",
          "https://beeg.link/-0554812887793188",
          "https://beeg.link/-0593876080832355",
          "https://beeg.link/-0339358177157452",
          "https://beeg.link/-0454120249306056",
          "https://beeg.link/-0815533142675010",
          "https://beeg.link/-0566150688257737",
          "https://beeg.link/-0366647926346466",
          "https://beeg.link/-0146753110810493",
          "https://beeg.link/-0948272754871618",
          "https://beeg.link/-0219055303786521",
          "https://beeg.link/-0131423636816884",
          "https://beeg.link/-0851817773153331",
          "https://beeg.link/-0230751927869958",
          "https://beeg.link/-0861719452682568",
          "https://beeg.link/-0141364225313431",
          "https://beeg.link/-0733905681009831",
          "https://beeg.link/-0678950641403552",
          "https://beeg.link/-0746549827503570",
          "https://beeg.link/-0640968562633273",
          "https://beeg.link/-0936394210690589",
          "https://beeg.link/-0362800752459982",
          "https://beeg.link/-0191210915334184",
          "https://beeg.link/-0786693704648002",
          "https://beeg.link/-0487915555528998",
          "https://beeg.link/-0938226288095004",
          "https://beeg.link/-0789050988906407",
          "https://beeg.link/-0733492206452202",
          "https://beeg.link/-0246373790565300",
          "https://beeg.link/-0646105818050406",
          "https://beeg.link/-0816330372216823",
          "https://beeg.link/-0121501863240189",
          "https://beeg.link/-0989548857139003",
          "https://beeg.link/-0780441067028609",
          "https://beeg.link/-0508892955364204",
          "https://beeg.link/-0101366557023570",
          "https://beeg.link/-0217519218185525",
          "https://beeg.link/-0259873242420701",
          "https://beeg.link/-0713573048047426",
          "https://beeg.link/-0348810100231765",
          "https://beeg.link/-0174023802586417",
          "https://beeg.link/-0960043474615026",
          "https://beeg.link/-0352948393261767",
          "https://beeg.link/-0658811397130673",
          "https://beeg.link/-0287716148069861",
          "https://beeg.link/-0357667907538034",
          "https://beeg.link/-0551772395548968",
          "https://beeg.link/-0494142140140659",
          "https://beeg.link/-0820465577472964",
          "https://beeg.link/-0559465333291530",
          "https://beeg.link/-0469036379651714",
          "https://beeg.link/-0465354385931701",
          "https://beeg.link/-0305386364300488",
          "https://beeg.link/-0774487544731161",
          "https://beeg.link/-0294785752803619",
          "https://beeg.link/-0698562031111136",
          "https://beeg.link/-0378568111721550",
          "https://beeg.link/-0246587200136546",
          "https://beeg.link/-0918206182002186",
          "https://beeg.link/-0118009274462017",
          "https://beeg.link/-0584249242801196",
          "https://beeg.link/-0957314240656326",
          "https://beeg.link/-0613018947892225",
          "https://beeg.link/-0917101785667737",
          "https://beeg.link/-0910929380159126",
          "https://beeg.link/-0712216070076680",
          "https://beeg.link/-0373753745084987",
          "https://beeg.link/-0923679508747107",
          "https://beeg.link/-0730314967484209",
          "https://beeg.link/-0468984485553231",
          "https://beeg.link/-0534534448090511",
          "https://beeg.link/-0740639460949783",
          "https://beeg.link/-0292556660267828",
          "https://beeg.link/-0321806016347144",
          "https://beeg.link/-0106743933587207",
          "https://beeg.link/-0900635144755441",
          "https://beeg.link/-0602554208205114",
          "https://beeg.link/-0811240836799339",
          "https://beeg.link/-0167567514950977",
          "https://beeg.link/-0291794645858793",
          "https://beeg.link/-0569031030905137",
          "https://beeg.link/-0813202209051626",
          "https://beeg.link/-0739019129895341",
          "https://beeg.link/-0242023032663132",
          "https://beeg.link/-0287635553375603",
          "https://beeg.link/-0882740318668672",
          "https://beeg.link/-0791275266352593",
          "https://beeg.link/-0655223754414356",
          "https://beeg.link/-0158223042002551",
          "https://beeg.link/-0579132720154448",
          "https://beeg.link/-0798664734222979",
          "https://beeg.link/-0512127642517640",
          "https://beeg.link/-0752141970598890",
          "https://beeg.link/-0330076495530622",
          "https://beeg.link/-0997974909455706",
          "https://beeg.link/-0545940979617133",
          "https://beeg.link/-0186691533376390",
          "https://beeg.link/-0504243701339833",
          "https://beeg.link/-0781735959295318",
          "https://beeg.link/-0170153462795919",
          "https://beeg.link/-0537610829716079",
          "https://beeg.link/-0425289559807613",
          "https://beeg.link/-0307498972323365",
          "https://beeg.link/-0484775576779301",
          "https://beeg.link/-0539817148434785",
          "https://beeg.link/-0962395657118688",
          "https://beeg.link/-0450739729774316",
          "https://beeg.link/-0657636700730977",
          "https://beeg.link/-0993590148718955",
          "https://beeg.link/-0761921538710329",
          "https://beeg.link/-0376167583275918",
          "https://beeg.link/-0551041518137581",
          "https://beeg.link/-0137594589929090",
          "https://beeg.link/-0712873981160861",
          "https://beeg.link/-0124467265390736",
          "https://beeg.link/-0830112181422692",
          "https://beeg.link/-0971848663438385",
          "https://beeg.link/-0833857752469793",
          "https://beeg.link/-0775042415197313",
          "https://beeg.link/-0486299083441908",
          "https://beeg.link/-0958945644265716",
          "https://beeg.link/-0553955197430688",
          "https://beeg.link/-0410107102525802",
          "https://beeg.link/-0404659577629218",
          "https://beeg.link/-0137346735257055",
          "https://beeg.link/-0391591728932355",
          "https://beeg.link/-0311305768461670",
          "https://beeg.link/-0442408222885270",
          "https://beeg.link/-0794729732121328",
          "https://beeg.link/-0807317374529940",
          "https://beeg.link/-0219697592754374",
          "https://beeg.link/-0579530393707837",
          "https://beeg.link/-0820714221949463",
          "https://beeg.link/-0629458727527340",
          "https://beeg.link/-0760480528316546",
          "https://beeg.link/-0363878848114803",
          "https://beeg.link/-0632216238936210",
          "https://beeg.link/-0740547626046241",
          "https://beeg.link/-0287648195510132",
          "https://beeg.link/-0278958906935643",
          "https://beeg.link/-0961895224831801",
          "https://beeg.link/-0700805070351745",
          "https://beeg.link/-0379185993476318",
          "https://beeg.link/-0878000594216261",
          "https://beeg.link/-0716161329183428",
          "https://beeg.link/-0823568495532156",
          "https://beeg.link/-0306243049584357",
          "https://beeg.link/-0181159769662850",
          "https://beeg.link/-0612807910808184",
          "https://beeg.link/-0114223340638533",
          "https://beeg.link/-0805514273497178",
          "https://beeg.link/-0756421100679231",
          "https://beeg.link/-0688284484924177",
          "https://beeg.link/-0538796820004512",
          "https://beeg.link/-0935310228949476",
          "https://beeg.link/-0957200329138774",
          "https://beeg.link/-0901990522337570",
          "https://beeg.link/-0336984450688037",
          "https://beeg.link/-0761340899619289",
          "https://beeg.link/-0834299785174566",
          "https://beeg.link/-0763321179709374",
          "https://beeg.link/-0230998848538658",
          "https://beeg.link/-0775073536590002",
          "https://beeg.link/-0551069543029146",
          "https://beeg.link/-0952464354218044",
          "https://beeg.link/-0164305978377791",
          "https://beeg.link/-0119656228095703",
          "https://beeg.link/-0435277395212364",
          "https://beeg.link/-0739049605808956",
          "https://beeg.link/-0544646063932952?t=915-1208",
          "https://beeg.link/-0544646063932952?t=139-779",
          "https://beeg.link/-0544646063932952?t=771-1451",
          "https://beeg.link/-01134902096?t=1393-1775",
          "https://beeg.link/-01134902096?t=941-1541",
          "https://beeg.link/-01134902096?t=443-1043",
          "https://beeg.link/-01134902096?t=157-757",
          "https://beeg.link/-0354271864783957",
          "https://beeg.link/-0756438292449114",
          "https://beeg.link/-0232217865679384",
          "https://beeg.link/-0582582354960120",
          "https://beeg.link/-0803461653443466",
          "https://beeg.link/-0602636954412228",
          "https://beeg.link/-0130197180961689",
          "https://beeg.link/-0533323424612618",
          "https://beeg.link/-0925267878045066",
          "https://beeg.link/-0723706695901196",
          "https://beeg.link/-0841822114003348",
          "https://beeg.link/-0588663384871232",
          "https://beeg.link/-0124940428248882",
          "https://beeg.link/-0749513046669555",
          "https://beeg.link/-0204824179114357",
          "https://beeg.link/-0954172231561034",
          "https://beeg.link/-0702158628799810",
          "https://beeg.link/-0785183269162427",
          "https://beeg.link/-0181979986524320",
          "https://beeg.link/-0481063881801806",
          "https://beeg.link/-0895364884159251",
          "https://beeg.link/-0943788239165246",
          "https://beeg.link/-0608095505252620",
          "https://beeg.link/-0923385468321127",
          "https://beeg.link/-0775764116557243",
          "https://beeg.link/-0616266738663805",
          "https://beeg.link/-0620636097504137",
          "https://beeg.link/-0827182187074961",
          "https://beeg.link/-0544121872641951",
          "https://beeg.link/-0257123039931950",
          "https://beeg.link/-0167458971603706",
          "https://beeg.link/-0568723697847460",
          "https://beeg.link/-0174378499901123",
          "https://beeg.link/-0164424861162430",
          "https://beeg.link/-0225478519405014",
          "https://beeg.link/-0211074879083026",
          "https://beeg.link/-0413002086391985",
          "https://beeg.link/-0513211103809726",
          "https://beeg.link/-0921991173673609",
          "https://beeg.link/-0892472850755789",
          "https://beeg.link/-0212321255779413",
          "https://beeg.link/-0433451042488257",
          "https://beeg.link/-0252901019991077",
          "https://beeg.link/-0426479816298282",
          "https://beeg.link/-0178568030705920",
          "https://beeg.link/-0896013275335365",
          "https://beeg.link/-0438123476885759",
          "https://beeg.link/-0170129361181951",
          "https://beeg.link/-0934443937074632",
          "https://beeg.link/-0351029114896778",
          "https://beeg.link/-0940641131608237",
          "https://beeg.link/-0755329798653781",
          "https://beeg.link/-0860881304649635",
          "https://beeg.link/-0604600547676594",
          "https://beeg.link/-0390640753479434",
          "https://beeg.link/-0476240666727305",
          "https://beeg.link/-0240319664200185",
          "https://beeg.link/-0922097639470667",
          "https://beeg.link/-0696492321521728",
          "https://beeg.link/-0592052259630156",
          "https://beeg.link/-0952171641676104",
          "https://beeg.link/-0538710971123913",
          "https://beeg.link/-0938831867096998",
          "https://beeg.link/-0967409802386243",
          "https://beeg.link/-0636815859118779",
          "https://beeg.link/-0284070677975347",
          "https://beeg.link/-0740466104588311",
          "https://beeg.link/-0911103606975527",
          "https://beeg.link/-0513248955021826",
          "https://beeg.link/-0612366197410549",
          "https://beeg.link/-0635949829836892",
          "https://beeg.link/-0147738157111498",
          "https://beeg.link/-0942086569428101",
          "https://beeg.link/-0365235326471176",
          "https://beeg.link/-0488682463338585",
          "https://beeg.link/-0175133864976608",
          "https://beeg.link/-0912766792807934",
          "https://beeg.link/-0895606999095424",
          "https://beeg.link/-0575095219951721",
          "https://beeg.link/-0469297326343927",
          "https://beeg.link/-0651959164342789",
          "https://beeg.link/-0856869460366310",
          "https://beeg.link/-0500736949947919",
          "https://beeg.link/-0848464015525163",
          "https://beeg.link/-0175748143272530",
          "https://beeg.link/-0490897103370007",
          "https://beeg.link/-0140112841653657",
          "https://beeg.link/-0272953894455809",
          "https://beeg.link/-0326957638526967",
          "https://beeg.link/-0414848340494820",
          "https://beeg.link/-0396219386306492",
          "https://beeg.link/-0633685388856536",
          "https://beeg.link/-0575043831060489",
          "https://beeg.link/-0438890360450889",
          "https://beeg.link/-0770670890669935",
          "https://beeg.link/-0789129432350899",
          "https://beeg.link/-0599348771668383",
          "https://beeg.link/-01984536258?t=939-1539",
          "https://beeg.link/-01984536258?t=815-1163",
          "https://beeg.link/-01984536258?t=11-611",
          "https://beeg.link/-01984536258?t=1070-1670",
          "https://beeg.link/-01984536258?t=533-1133",
          "https://beeg.link/-01083288577?t=671-1211",
          "https://beeg.link/-01083288577?t=79-619",
          "https://beeg.link/-01083288577?t=640-891",
          "https://beeg.link/-01083288577?t=919-1459",
          "https://beeg.link/-0183366375812613?t=16-844",
          "https://beeg.link/-0183366375812613?t=1257-1567",
          "https://beeg.link/-0513363095957203",
          "https://beeg.link/-0707285076603306",
          "https://beeg.link/-0366556527665686",
          "https://beeg.link/-0587415759524537",
          "https://beeg.link/-0661134470928560",
          "https://beeg.link/-0537217475562596",
          "https://beeg.link/-0804407999942025",
          "https://beeg.link/-0792269440696299",
          "https://beeg.link/-0288623018037583",
          "https://beeg.link/-0286560194555485",
          "https://beeg.link/-0992576234942669",
          "https://beeg.link/-0549363958128410",
          "https://beeg.link/-0799713083453188",
          "https://beeg.link/-0342050853043141",
          "https://beeg.link/-01825470897?t=897-1437",
          "https://beeg.link/-01825470897?t=1893-2433",
          "https://beeg.link/-01825470897?t=2355-2895",
          "https://beeg.link/-01825470897?t=1538-1813",
          "https://beeg.link/-01825470897?t=1449-1989",
          "https://beeg.link/-01280600334?t=995-1535",
          "https://beeg.link/-01280600334?t=63-603",
          "https://beeg.link/-01280600334?t=577-846",
          "https://beeg.link/-01280600334?t=591-1131",
          "https://beeg.link/-01660186516?t=846-1193",
          "https://beeg.link/-01660186516?t=659-1259",
          "https://beeg.link/-01660186516?t=857-1457",
          "https://beeg.link/-01660186516?t=1593-2193",
          "https://beeg.link/-01660186516?t=2203-2803",
          "https://beeg.link/-01564114596?t=4-612",
          "https://beeg.link/-01564114596?t=11-347",
          "https://beeg.link/-01626055144?t=1662-2250",
          "https://beeg.link/-01626055144?t=591-936",
          "https://beeg.link/-01626055144?t=1197-1647",
          "https://beeg.link/-01447926397?t=1928-2468",
          "https://beeg.link/-01447926397?t=249-789",
          "https://beeg.link/-01447926397?t=711-1251",
          "https://beeg.link/-01447926397?t=1383-1923",
          "https://beeg.link/-01447926397?t=1770-2081",
          "https://beeg.link/-01673086061?t=746-1007",
          "https://beeg.link/-01673086061?t=24-632",
          "https://beeg.link/-01616974509?t=189-789",
          "https://beeg.link/-01616974509?t=1146-1745",
          "https://beeg.link/-01616974509?t=475-1075",
          "https://beeg.link/-01616974509?t=746-1089",
          "https://beeg.link/-01390572634?t=1461-2061",
          "https://beeg.link/-01390572634?t=2083-2363",
          "https://beeg.link/-01390572634?t=1091-1691",
          "https://beeg.link/-01390572634?t=2159-2759",
          "https://beeg.link/-01733789672?t=1695-2415",
          "https://beeg.link/-01733789672?t=1145-1865",
          "https://beeg.link/-01733789672?t=2727-3447",
          "https://beeg.link/-01733789672?t=2337-3057",
          "https://beeg.link/-01045510563?t=148-425",
          "https://beeg.link/-01045510563?t=503-1103",
          "https://beeg.link/-01045510563?t=985-1585",
          "https://beeg.link/-01045510563?t=53-653",
          "https://beeg.link/-01045510563?t=1148-1748",
          "https://beeg.link/-0157455383177607?t=556-901",
          "https://beeg.link/-0157455383177607?t=71-701",
          "https://beeg.link/-0157455383177607?t=711-1051",
          "https://beeg.link/-01137023198?t=2957-3557",
          "https://beeg.link/-01137023198?t=149-749",
          "https://beeg.link/-01137023198?t=675-1275",
          "https://beeg.link/-01137023198?t=1357-1957",
          "https://beeg.link/-01137023198?t=2171-2415",
          "https://beeg.link/-01137023198?t=2353-2953",
          "https://beeg.link/-0797891951619182?t=322-1070",
          "https://beeg.link/-0797891951619182?t=92-318",
          "https://beeg.link/-0698142791886389?t=842-1326",
          "https://beeg.link/-0698142791886389?t=144-826",
          "https://beeg.link/-0985831682718917",
          "https://beeg.link/-0244457550869512",
          "https://beeg.link/-0991470574998624",
          "https://beeg.link/-0762925113393461",
          "https://beeg.link/-0383191395793370",
          "https://beeg.link/-0671981681390369",
          "https://beeg.link/-0306644450531561",
          "https://beeg.link/-0891956120233657",
          "https://beeg.link/-0770741125867156",
          "https://beeg.link/-0118239629854534",
          "https://beeg.link/-0581618098338298",
          "https://beeg.link/-0399754849469810",
          "https://beeg.link/-0440126168951070",
          "https://beeg.link/-0835171966290469",
          "https://beeg.link/-0765160211045433",
          "https://beeg.link/-0939779742539807",
          "https://beeg.link/-0626723911411880",
          "https://beeg.link/-0728544414423039",
          "https://beeg.link/-0780251010433184",
          "https://beeg.link/-0809855519879184",
          "https://beeg.link/-0668292627069046",
          "https://beeg.link/-0920934263665168",
          "https://beeg.link/-0261797466767062",
          "https://beeg.link/-0795095358119349",
          "https://beeg.link/-0998263780822902",
          "https://beeg.link/-0962926354295438",
          "https://beeg.link/-0609065343531204",
          "https://beeg.link/-0673378964998380",
          "https://beeg.link/-0544723219908380",
          "https://beeg.link/-0863655342946917",
          "https://beeg.link/-0684149877968959",
          "https://beeg.link/-0819428667199577",
          "https://beeg.link/-0359244349182289",
          "https://beeg.link/-0622306063177098",
          "https://beeg.link/-0128986667059078",
          "https://beeg.link/-0743855474017782",
          "https://beeg.link/-0875315256101742",
          "https://beeg.link/-0442046242776705",
          "https://beeg.link/-0915955819600876",
          "https://beeg.link/-0859256859949107",
          "https://beeg.link/-0522707769648479",
          "https://beeg.link/-0176698331005474",
          "https://beeg.link/-0338108451515447",
          "https://beeg.link/-0342618210570078",
          "https://beeg.link/-0342653924297494",
          "https://beeg.link/-0859388788164640",
          "https://beeg.link/-0537028202757049",
          "https://beeg.link/-0833862155931139",
          "https://beeg.link/-0747603958717439",
          "https://beeg.link/-0516400419904470",
          "https://beeg.link/-0779498968034802",
          "https://beeg.link/-0236962250792629",
          "https://beeg.link/-0555798454362701",
          "https://beeg.link/-0686720669058128",
          "https://beeg.link/-0179973933266551",
          "https://beeg.link/-0902803589973690",
          "https://beeg.link/-0381492097454746",
          "https://beeg.link/-0419431524084322",
          "https://beeg.link/-0953881525135630",
          "https://beeg.link/-0763475042786262",
          "https://beeg.link/-0422241064620644",
          "https://beeg.link/-0539041908365786",
          "https://beeg.link/-0511761623023217",
          "https://beeg.link/-0235414302474420",
          "https://beeg.link/-0828464559748417",
          "https://beeg.link/-0122747637487363",
          "https://beeg.link/-0599960851574302",
          "https://beeg.link/-0908944714191039",
          "https://beeg.link/-0681794734364175",
          "https://beeg.link/-0805573749523600",
          "https://beeg.link/-0260010584108046",
          "https://beeg.link/-0623988543970685",
          "https://beeg.link/-0162322964005494",
          "https://beeg.link/-0776784006717172",
          "https://beeg.link/-0718481518511217",
          "https://beeg.link/-0835998028165954",
          "https://beeg.link/-0294384123651694",
          "https://beeg.link/-0473442318525191",
          "https://beeg.link/-0224799596156138",
          "https://beeg.link/-0596782752560239",
          "https://beeg.link/-0365580508283088",
          "https://beeg.link/-0158135253220871",
          "https://beeg.link/-0379488735837381",
          "https://beeg.link/-0948323702824483",
          "https://beeg.link/-0595563212375349",
          "https://beeg.link/-0633989324050558",
          "https://beeg.link/-0458903773643331",
          "https://beeg.link/-0181152523189173",
          "https://beeg.link/-0443593695618716",
          "https://beeg.link/-0777423026443095",
          "https://beeg.link/-0529652612225938",
          "https://beeg.link/-0469187657475975",
          "https://beeg.link/-0326712244602007",
          "https://beeg.link/-0222403759966132",
          "https://beeg.link/-0787234064100437",
          "https://beeg.link/-0591027917130084",
          "https://beeg.link/-0678730437730691",
          "https://beeg.link/-0812785781845959",
          "https://beeg.link/-0682140836249349",
          "https://beeg.link/-0307725363376995",
          "https://beeg.link/-0782213821024485",
          "https://beeg.link/-0606930394985781",
          "https://beeg.link/-0791036589282055",
          "https://beeg.link/-0899066154809828",
          "https://beeg.link/-0489905920641466",
          "https://beeg.link/-0592030066020267",
          "https://beeg.link/-0350438874439301",
          "https://beeg.link/-0171639343899047",
          "https://beeg.link/-0459207197400092",
          "https://beeg.link/-0590869573494418",
          "https://beeg.link/-0607878114854271",
          "https://beeg.link/-0213104940008447",
          "https://beeg.link/-0300824162386342",
          "https://beeg.link/-0400322624732106",
          "https://beeg.link/-0415630733668232",
          "https://beeg.link/-0919873806554487",
          "https://beeg.link/-0471919634660293",
          "https://beeg.link/-0178162526655316",
          "https://beeg.link/-0572795818692554",
          "https://beeg.link/-0930952031353210",
          "https://beeg.link/-0494990459683333",
          "https://beeg.link/-0216048042945372",
          "https://beeg.link/-0644098193730959",
          "https://beeg.link/-0539506184605439",
          "https://beeg.link/-0793346534409521",
          "https://beeg.link/-0728649063045664",
          "https://beeg.link/-0296310771916071",
          "https://beeg.link/-0234464823019411",
          "https://beeg.link/-0476800631566592",
          "https://beeg.link/-0626774832615412",
          "https://beeg.link/-0197450504556914",
          "https://beeg.link/-0546286633378115",
          "https://beeg.link/-0132973346241217",
          "https://beeg.link/-0333841218463924",
          "https://beeg.link/-0801577755766766",
          "https://beeg.link/-0771185246909343",
          "https://beeg.link/-0720525823657577",
          "https://beeg.link/-0603000671920113",
          "https://beeg.link/-0623416527076991",
          "https://beeg.link/-0132648760108969",
          "https://beeg.link/-0649332657921756",
          "https://beeg.link/-0720358423224743",
          "https://beeg.link/-0441583566944352",
          "https://beeg.link/-0996908396971235",
          "https://beeg.link/-0177334078476344",
          "https://beeg.link/-0748063895917880",
          "https://beeg.link/-0340207310137189",
          "https://beeg.link/-0528932906000127",
          "https://beeg.link/-0352805367882094",
          "https://beeg.link/-0363766415959589",
          "https://beeg.link/-0607520507073536",
          "https://beeg.link/-0305991280159680",
          "https://beeg.link/-0615730570261009",
          "https://beeg.link/-0835018666181680",
          "https://beeg.link/-0987563781986329",
          "https://beeg.link/-0837614286647493",
          "https://beeg.link/-0980675693047056",
          "https://beeg.link/-0872832846380302",
          "https://beeg.link/-0248283362603742",
          "https://beeg.link/-0921003421009963",
          "https://beeg.link/-0412325689449956",
          "https://beeg.link/-0410286055947279",
          "https://beeg.link/-0172984903782195",
          "https://beeg.link/-0506392543573813",
          "https://beeg.link/-0578463886691895",
          "https://beeg.link/-0854274113527232",
          "https://beeg.link/-0859564935139370",
          "https://beeg.link/-0478553834747874",
          "https://beeg.link/-0824040047345115",
          "https://beeg.link/-0650002633705902",
          "https://beeg.link/-0943109883419477",
          "https://beeg.link/-0696386215699265",
          "https://beeg.link/-0287872958475398",
          "https://beeg.link/-0250573294803247",
          "https://beeg.link/-0351200298386095",
          "https://beeg.link/-0254857249338224",
          "https://beeg.link/-0498100968610622",
          "https://beeg.link/-0135188111366805",
          "https://beeg.link/-0916299881379449",
          "https://beeg.link/-0705251339036874",
          "https://beeg.link/-0533389300407738",
          "https://beeg.link/-0644106604907399",
          "https://beeg.link/-0551999409353467",
          "https://beeg.link/-0833873703421789",
          "https://beeg.link/-0956962264671739",
          "https://beeg.link/-0714073853605420",
          "https://beeg.link/-0759144347847029",
          "https://beeg.link/-0416004725510432",
          "https://beeg.link/-0771058788972045",
          "https://beeg.link/-0128286197296413",
          "https://beeg.link/-0672558530927993",
          "https://beeg.link/-0882831762713281",
          "https://beeg.link/-0172963545648294",
          "https://beeg.link/-0406686823772661",
          "https://beeg.link/-0230529709027823",
          "https://beeg.link/-0999658667502076",
          "https://beeg.link/-0350099183861048",
          "https://beeg.link/-0723133418105579",
          "https://beeg.link/-0555252256144188",
          "https://beeg.link/-0358029362441162",
          "https://beeg.link/-0326708174632849",
          "https://beeg.link/-0639726598545169",
          "https://beeg.link/-0682303981367579",
          "https://beeg.link/-0239009839037916",
          "https://beeg.link/-0677712913850459",
          "https://beeg.link/-0971324732456238",
          "https://beeg.link/-0701187312156353",
          "https://beeg.link/-0208399995398497",
          "https://beeg.link/-0503961233674112",
          "https://beeg.link/-0208554050537213",
          "https://beeg.link/-0995240829276820",
          "https://beeg.link/-0691380052199234",
          "https://beeg.link/-0988853128280063",
          "https://beeg.link/-0618843438825973",
          "https://beeg.link/-0684546656284234",
          "https://beeg.link/-0119711889922518",
          "https://beeg.link/-0895936326210430",
          "https://beeg.link/-0395364919023310",
          "https://beeg.link/-0731586275101937",
          "https://beeg.link/-0250522671906649",
          "https://beeg.link/-0750768704876759",
          "https://beeg.link/-0788592375627605",
          "https://beeg.link/-0344005898687921",
          "https://beeg.link/-0614532378853076",
          "https://beeg.link/-0268336396300099",
          "https://beeg.link/-0694702285539417",
          "https://beeg.link/-0794794117240826",
          "https://beeg.link/-0469721528178885",
          "https://beeg.link/-0585894590481473",
          "https://beeg.link/-0770547802959445",
          "https://beeg.link/-0527236570456421",
          "https://beeg.link/-0127960471495524",
          "https://beeg.link/-0491412172000244",
          "https://beeg.link/-0520576732718186",
          "https://beeg.link/-0622630955392750",
          "https://beeg.link/-0472158673145832",
          "https://beeg.link/-0600333400906052",
          "https://beeg.link/-0609055811427073",
          "https://beeg.link/-0235507717955435",
          "https://beeg.link/-0612364135207845",
          "https://beeg.link/-0907150861007096",
          "https://beeg.link/-0726805279478154",
          "https://beeg.link/-0563766674148025",
          "https://beeg.link/-0161808941957141",
          "https://beeg.link/-0167008536469337",
          "https://beeg.link/-0990046136686568",
          "https://beeg.link/-0514289753060732",
          "https://beeg.link/-0434304540904949",
          "https://beeg.link/-0198823594549656",
          "https://beeg.link/-0424106511959437",
          "https://beeg.link/-0629657505169257",
          "https://beeg.link/-0295339126875300",
          "https://beeg.link/-0358565485906881",
          "https://beeg.link/-0469017572393155",
          "https://beeg.link/-0343381488359957",
          "https://beeg.link/-0533129286758739",
          "https://beeg.link/-0647173548407372",
          "https://beeg.link/-0523802900519205",
          "https://beeg.link/-0310238770756550",
          "https://beeg.link/-0284797175121130",
          "https://beeg.link/-0178497185348986",
          "https://beeg.link/-0586692811981374",
          "https://beeg.link/-0807164285614100",
          "https://beeg.link/-0934091111149587",
          "https://beeg.link/-0489138918639357",
          "https://beeg.link/-0919065332760576",
          "https://beeg.link/-0993986053093988",
          "https://beeg.link/-0448945088511264",
          "https://beeg.link/-0778646909696696",
          "https://beeg.link/-0848105010768134",
          "https://beeg.link/-0322805332540632",
          "https://beeg.link/-0530747487497774",
          "https://beeg.link/-0951102191424191",
          "https://beeg.link/-0711101118296049",
          "https://beeg.link/-0187561187129675",
          "https://beeg.link/-0140591886406494",
          "https://beeg.link/-0454068453325089",
          "https://beeg.link/-0715131094009054",
          "https://beeg.link/-0826577099052711",
          "https://beeg.link/-0672233676309570",
          "https://beeg.link/-0110986730306282",
          "https://beeg.link/-0972988614266173",
          "https://beeg.link/-0865271014376822",
          "https://beeg.link/-0895601356021992",
          "https://beeg.link/-0591093666225023",
          "https://beeg.link/-0677155615503880",
          "https://beeg.link/-0653586926591426",
          "https://beeg.link/-0191649080068003",
          "https://beeg.link/-0943300290554594",
          "https://beeg.link/-0194007180746650",
          "https://beeg.link/-0581439775026922",
          "https://beeg.link/-0737420342996319",
          "https://beeg.link/-0549838865893320",
          "https://beeg.link/-0412619967328117",
          "https://beeg.link/-0614012057317185",
          "https://beeg.link/-0842323348255871",
          "https://beeg.link/-0616079505246380",
          "https://beeg.link/-0249004704320275",
          "https://beeg.link/-0629658843156512",
          "https://beeg.link/-0648519462461547",
          "https://beeg.link/-0423507567689465",
          "https://beeg.link/-0526831159301012",
          "https://beeg.link/-0198910953687816",
          "https://beeg.link/-0492398734311028",
          "https://beeg.link/-0839625679458798",
          "https://beeg.link/-0121108886028273",
          "https://beeg.link/-0689913467715532",
          "https://beeg.link/-0372018546709396",
          "https://beeg.link/-0662470663402669",
          "https://beeg.link/-0990493857415184",
          "https://beeg.link/-0227351433735844",
          "https://beeg.link/-0628726760363086",
          "https://beeg.link/-0485132860698000",
          "https://beeg.link/-0957679930595242",
          "https://beeg.link/-0497920084213444",
          "https://beeg.link/-0685634926607242",
          "https://beeg.link/-0472146324410487",
          "https://beeg.link/-0271069567033523",
          "https://beeg.link/-0827091278359714",
          "https://beeg.link/-0577466746141238",
          "https://beeg.link/-0939452465791617",
          "https://beeg.link/-0681163590137119",
          "https://beeg.link/-0219019777206360",
          "https://beeg.link/-0806031676067805",
          "https://beeg.link/-0538724499963078",
          "https://beeg.link/-0482892624813642",
          "https://beeg.link/-0921636919598532",
          "https://beeg.link/-0768858268761902",
          "https://beeg.link/-0339421862220235",
          "https://beeg.link/-0281985059328877",
          "https://beeg.link/-0723344447974071",
          "https://beeg.link/-0138449091507630",
          "https://beeg.link/-0921887152007122",
          "https://beeg.link/-0820099847319293",
          "https://beeg.link/-0198217644116881",
          "https://beeg.link/-0656936231619823",
          "https://beeg.link/-0593912901924743",
          "https://beeg.link/-0162325201695506",
          "https://beeg.link/-0206847831194397",
          "https://beeg.link/-0590577593119102",
          "https://beeg.link/-0129697007233095",
          "https://beeg.link/-0359785769585214",
          "https://beeg.link/-0451404265795701",
          "https://beeg.link/-0454066234521395",
          "https://beeg.link/-0952805138904638",
          "https://beeg.link/-0918509864366648",
          "https://beeg.link/-0429405366960119",
          "https://beeg.link/-0394143133657107",
          "https://beeg.link/-0974793057968277",
          "https://beeg.link/-0387252789687611",
          "https://beeg.link/-0862239950291259",
          "https://beeg.link/-0296434277831331",
          "https://beeg.link/-0398431091294665",
          "https://beeg.link/-0629646372305559",
          "https://beeg.link/-0488473148864358",
          "https://beeg.link/-0510644478788611",
          "https://beeg.link/-0432792047955063",
          "https://beeg.link/-0327502447121429",
          "https://beeg.link/-0436251247805880",
          "https://beeg.link/-0629604427892673",
          "https://beeg.link/-0995172129798484",
          "https://beeg.link/-0876657191720588",
          "https://beeg.link/-0571110171297605",
          "https://beeg.link/-0929531378141557",
          "https://beeg.link/-0137936786156508",
          "https://beeg.link/-0235352269907604",
          "https://beeg.link/-0220616241955393",
          "https://beeg.link/-0250738216935217",
          "https://beeg.link/-0329640463932072",
          "https://beeg.link/-0682318356897485",
          "https://beeg.link/-0873863240627788",
          "https://beeg.link/-0491480955928405",
          "https://beeg.link/-0696137226758823",
          "https://beeg.link/-0555708481693313",
          "https://beeg.link/-0907507969403361",
          "https://beeg.link/-0482053251288852",
          "https://beeg.link/-0619146064082280",
          "https://beeg.link/-0235526140709030",
          "https://beeg.link/-0344107960451549",
          "https://beeg.link/-0897417043973949",
          "https://beeg.link/-0286444078546282",
          "https://beeg.link/-0230033782619625",
          "https://beeg.link/-0805328096377920",
          "https://beeg.link/-0919769171411116",
          "https://beeg.link/-0662961124547352",
          "https://beeg.link/-0614883937077304",
          "https://beeg.link/-0841998157644101",
          "https://beeg.link/-0865154832938737",
          "https://beeg.link/-0481190285814572",
          "https://beeg.link/-0742946459962183",
          "https://beeg.link/-0989425645486615",
          "https://beeg.link/-0407076473247897",
          "https://beeg.link/-0863871371970851",
          "https://beeg.link/-0685257261466389",
          "https://beeg.link/-0309582996508067",
          "https://beeg.link/-0999608827478662",
          "https://beeg.link/-0406262427662087",
          "https://beeg.link/-0569004460826073",
          "https://beeg.link/-0583815472637061",
          "https://beeg.link/-0879477821612358",
          "https://beeg.link/-0309489894415968",
          "https://beeg.link/-0380277869637698",
          "https://beeg.link/-0966651558500568",
          "https://beeg.link/-0967740487019661",
          "https://beeg.link/-0757074830155368",
          "https://beeg.link/-0172704944552567",
          "https://beeg.link/-0270627732593647",
          "https://beeg.link/-0278635032863966",
          "https://beeg.link/-0617766784820171",
          "https://beeg.link/-0129525328332521",
          "https://beeg.link/-0309862145157932",
          "https://beeg.link/-0445062737592156",
          "https://beeg.link/-0389649897374967",
          "https://beeg.link/-0923892036527698",
          "https://beeg.link/-0606202231321911",
          "https://beeg.link/-0415244475817741",
          "https://beeg.link/-0269732970239131",
          "https://beeg.link/-0677145810849113",
          "https://beeg.link/-0791410792818704",
          "https://beeg.link/-0605294127300095",
          "https://beeg.link/-0805712311909905",
          "https://beeg.link/-0554898584472143",
          "https://beeg.link/-0585774956937593",
          "https://beeg.link/-0184418286095233",
          "https://beeg.link/-0873760375504841",
          "https://beeg.link/-0454917796062705",
          "https://beeg.link/-0170383340868412",
          "https://beeg.link/-0859554575634925",
          "https://beeg.link/-0906754175344310",
          "https://beeg.link/-0486002187573645",
          "https://beeg.link/-0386732823374926",
          "https://beeg.link/-0458049523354775",
          "https://beeg.link/-0204919163135396",
          "https://beeg.link/-0714056445575519",
          "https://beeg.link/-0991953366612213",
          "https://beeg.link/-0387562464915616",
          "https://beeg.link/-0360201438485849",
          "https://beeg.link/-0957270564541695",
          "https://beeg.link/-0496231927576326",
          "https://beeg.link/-0372600316108027",
          "https://beeg.link/-0438227534137699",
          "https://beeg.link/-0340217277560953",
          "https://beeg.link/-0282337286501803",
          "https://beeg.link/-0218691473131763",
          "https://beeg.link/-0361674392279565",
          "https://beeg.link/-0446020741327848",
          "https://beeg.link/-0953110158861692",
          "https://beeg.link/-0863176124439874",
          "https://beeg.link/-0191299182542824",
          "https://beeg.link/-0711200269423879",
          "https://beeg.link/-0298953477982832",
          "https://beeg.link/-0400581238224221",
          "https://beeg.link/-0545890571878964",
          "https://beeg.link/-0707328063526490",
          "https://beeg.link/-0251976493287485",
          "https://beeg.link/-0711179773333010",
          "https://beeg.link/-0312980981867259",
          "https://beeg.link/-0250397160973636",
          "https://beeg.link/-0203905401365522",
          "https://beeg.link/-0881506990806953",
          "https://beeg.link/-0436713552226663",
          "https://beeg.link/-0206901738868861",
          "https://beeg.link/-0619255284240874",
          "https://beeg.link/-0738478590528194",
          "https://beeg.link/-0642541781070360",
          "https://beeg.link/-0625537391880514",
          "https://beeg.link/-0977410396982892",
          "https://beeg.link/-0951039473719152",
          "https://beeg.link/-0286971334393328",
          "https://beeg.link/-0213165548035633",
          "https://beeg.link/-0725988895181996",
          "https://beeg.link/-0574301991182324",
          "https://beeg.link/-0682448569286910",
          "https://beeg.link/-0307323889047550",
          "https://beeg.link/-0490062705163775",
          "https://beeg.link/-0275456838232381",
          "https://beeg.link/-0995613519389901",
          "https://beeg.link/-0704657242392028",
          "https://beeg.link/-0424394078103124",
          "https://beeg.link/-0238390217169948",
          "https://beeg.link/-0841207571169640",
          "https://beeg.link/-0103555058801849",
          "https://beeg.link/-0937763522870566",
          "https://beeg.link/-0613015229890351",
          "https://beeg.link/-0333377960831695",
          "https://beeg.link/-0566143025150438",
          "https://beeg.link/-0329042465976703",
          "https://beeg.link/-0245377971169224",
          "https://beeg.link/-0108922908429077",
          "https://beeg.link/-0586196334714034",
          "https://beeg.link/-0701693616578693",
          "https://beeg.link/-0964699954165316",
          "https://beeg.link/-0180748137859376",
          "https://beeg.link/-0845682025935700",
          "https://beeg.link/-0244888630933306",
          "https://beeg.link/-0571851582356641",
          "https://beeg.link/-0739503726952323",
          "https://beeg.link/-0290830902234790",
          "https://beeg.link/-0537705257022782",
          "https://beeg.link/-0549477228103316",
          "https://beeg.link/-0244856447368711",
          "https://beeg.link/-0494568948655101",
          "https://beeg.link/-0595867738649933",
          "https://beeg.link/-0361015295460887",
          "https://beeg.link/-0648027437798614",
          "https://beeg.link/-0649320889837600",
          "https://beeg.link/-0822263713941427",
          "https://beeg.link/-0573903375692773",
          "https://beeg.link/-0785316025236704",
          "https://beeg.link/-0223062751712076",
          "https://beeg.link/-0303243778798695",
          "https://beeg.link/-0905142231758700",
          "https://beeg.link/-0272263511432435",
          "https://beeg.link/-0302052070719818",
          "https://beeg.link/-0314978656535862",
          "https://beeg.link/-0844106033311604",
          "https://beeg.link/-0350028253975102",
          "https://beeg.link/-0122892425329620",
          "https://beeg.link/-0762393174306621",
          "https://beeg.link/-0390094908670844",
          "https://beeg.link/-0479711751051569",
          "https://beeg.link/-0648041354309928",
          "https://beeg.link/-0404960526211337",
          "https://beeg.link/-0141026092212721",
          "https://beeg.link/-0360783441488315",
          "https://beeg.link/-0332864880355809",
          "https://beeg.link/-0202946291659811",
          "https://beeg.link/-0990470976119153",
          "https://beeg.link/-0887116853748326",
          "https://beeg.link/-0716302278878708",
          "https://beeg.link/-0934374775822432",
          "https://beeg.link/-0226481202961887",
          "https://beeg.link/-0298693581693824",
          "https://beeg.link/-0152058516509139",
          "https://beeg.link/-0435534393857071",
          "https://beeg.link/-0356684003175313",
          "https://beeg.link/-0684756460252626",
          "https://beeg.link/-0286128772459582",
          "https://beeg.link/-0703960524057979",
          "https://beeg.link/-0544747769003078",
          "https://beeg.link/-0534773971509647",
          "https://beeg.link/-0853374666012518",
          "https://beeg.link/-0925268672957070",
          "https://beeg.link/-0584455381551394",
          "https://beeg.link/-0951288650558839",
          "https://beeg.link/-0120858853254713",
          "https://beeg.link/-0686724859227139",
          "https://beeg.link/-0758029397544313",
          "https://beeg.link/-0535621180865779",
          "https://beeg.link/-0790813081396907",
          "https://beeg.link/-0643535974870817",
          "https://beeg.link/-0963915959179672",
          "https://beeg.link/-0745256650180581",
          "https://beeg.link/-0553623851236347",
          "https://beeg.link/-0681657450567156",
          "https://beeg.link/-0318313513700954",
          "https://beeg.link/-0375085576370052",
          "https://beeg.link/-0527931322827788",
          "https://beeg.link/-0581578175071104",
          "https://beeg.link/-0946949053819728",
          "https://beeg.link/-0498533375370908",
          "https://beeg.link/-0855419925001871",
          "https://beeg.link/-0998279908316256",
          "https://beeg.link/-0245654976752879",
          "https://beeg.link/-0814672241967215",
          "https://beeg.link/-0601487035159490",
          "https://beeg.link/-0842704428295964",
          "https://beeg.link/-0704720325675083",
          "https://beeg.link/-0703994499991175",
          "https://beeg.link/-0820862864040526",
          "https://beeg.link/-0904385906650645",
          "https://beeg.link/-0773223073314946",
          "https://beeg.link/-0711194571746886",
          "https://beeg.link/-0839918115952227",
          "https://beeg.link/-0630873936868274",
          "https://beeg.link/-0374063697865466",
          "https://beeg.link/-0690152136833262",
          "https://beeg.link/-0926049440838899",
          "https://beeg.link/-0849052360268599",
          "https://beeg.link/-0175382596577263",
          "https://beeg.link/-0374764215986756",
          "https://beeg.link/-0864136668775206",
          "https://beeg.link/-0987793533065380",
          "https://beeg.link/-0288177726990862",
          "https://beeg.link/-0425788511375607",
          "https://beeg.link/-0865292638157068",
          "https://beeg.link/-0940519163076116",
          "https://beeg.link/-0939789160617692",
          "https://beeg.link/-0608524374991514",
          "https://beeg.link/-0753427445157298",
          "https://beeg.link/-0543254932258569",
          "https://beeg.link/-0763754053409493",
          "https://beeg.link/-0373420316838580",
          "https://beeg.link/-0302762521911490",
          "https://beeg.link/-0578731664933578",
          "https://beeg.link/-0988502235153412",
          "https://beeg.link/-0969390849704708",
          "https://beeg.link/-0882954537466240",
          "https://beeg.link/-0241992911237942",
          "https://beeg.link/-0618039394504123",
          "https://beeg.link/-0925220350294156",
          "https://beeg.link/-0747719606407456",
          "https://beeg.link/-0102496262291715",
          "https://beeg.link/-0283318692280056",
          "https://beeg.link/-0224937567219950",
          "https://beeg.link/-0613469720468499",
          "https://beeg.link/-0346452615085999",
          "https://beeg.link/-0241682689604904",
          "https://beeg.link/-0162686548230547",
          "https://beeg.link/-0583778505769493",
          "https://beeg.link/-0337668542735729",
          "https://beeg.link/-0630685859304636",
          "https://beeg.link/-0930392251621934",
          "https://beeg.link/-0494016377892492",
          "https://beeg.link/-0548641769934794",
          "https://beeg.link/-0281747638103656",
          "https://beeg.link/-0940979603999300",
          "https://beeg.link/-0321274358704193",
          "https://beeg.link/-0931358471911577",
          "https://beeg.link/-0443689398838872",
          "https://beeg.link/-0166530095521434",
          "https://beeg.link/-0561860994522991",
          "https://beeg.link/-0339890288040756",
          "https://beeg.link/-0375613518192462",
          "https://beeg.link/-0299532239682153",
          "https://beeg.link/-0296018839206180",
          "https://beeg.link/-0596985688648719",
          "https://beeg.link/-0425147354550781",
          "https://beeg.link/-0532581240907673",
          "https://beeg.link/-0858182762353590",
          "https://beeg.link/-0372004753323546",
          "https://beeg.link/-0835090778709758",
          "https://beeg.link/-0911721872570109",
          "https://beeg.link/-0357777951877002",
          "https://beeg.link/-0284493676802161",
          "https://beeg.link/-0553336243399504",
          "https://beeg.link/-0657877515407992",
          "https://beeg.link/-0684626005165601",
          "https://beeg.link/-0923753999221584",
          "https://beeg.link/-0551219408753754",
          "https://beeg.link/-0949999498489862",
          "https://beeg.link/-0654123486381034",
          "https://beeg.link/-0423646853707087",
          "https://beeg.link/-0745308076353664",
          "https://beeg.link/-0640509935718801",
          "https://beeg.link/-0316531633075442",
          "https://beeg.link/-0528247440177416",
          "https://beeg.link/-0112380445884532",
          "https://beeg.link/-0580492327286588",
          "https://beeg.link/-0154760521388939",
          "https://beeg.link/-0773145087513101",
          "https://beeg.link/-0993302815610620",
          "https://beeg.link/-0367946329670626",
          "https://beeg.link/-0621982400161458",
          "https://beeg.link/-0178692492940263",
          "https://beeg.link/-0907684553147017",
          "https://beeg.link/-0775357577932201",
          "https://beeg.link/-0837498344822982",
          "https://beeg.link/-0135296026301979",
          "https://beeg.link/-0980988508253808",
          "https://beeg.link/-0163983156389526",
          "https://beeg.link/-0894299716906326",
          "https://beeg.link/-0441099152616263",
          "https://beeg.link/-0375739084517102",
          "https://beeg.link/-0198031727091682",
          "https://beeg.link/-0432026473586248",
          "https://beeg.link/-0901043351570474",
          "https://beeg.link/-0413221298885304",
          "https://beeg.link/-0393883704276831",
          "https://beeg.link/-0679894377648681",
          "https://beeg.link/-0742649161079992",
          "https://beeg.link/-0114115573684675",
          "https://beeg.link/-0901986418094099",
          "https://beeg.link/-0983711512568863",
          "https://beeg.link/-0767985530376160",
          "https://beeg.link/-0324129665481711",
          "https://beeg.link/-0993642703208207",
          "https://beeg.link/-0320223978448395",
          "https://beeg.link/-0495331408074305",
          "https://beeg.link/-0129820219400279",
          "https://beeg.link/-0729570138974824",
          "https://beeg.link/-0969950668934410",
          "https://beeg.link/-0212005428508904",
          "https://beeg.link/-0558494311868478",
          "https://beeg.link/-0364809910275373",
          "https://beeg.link/-0213636100326618",
          "https://beeg.link/-0460023995462668",
          "https://beeg.link/-0938813947819745",
          "https://beeg.link/-0538093759212443",
          "https://beeg.link/-0942291048978892",
          "https://beeg.link/-0413183920456689",
          "https://beeg.link/-0587788456729853",
          "https://beeg.link/-0406552479972513",
          "https://beeg.link/-0952460829263355",
          "https://beeg.link/-0876108771617453",
          "https://beeg.link/-0943447032309969",
          "https://beeg.link/-0995914772072384",
          "https://beeg.link/-0528471829236797",
          "https://beeg.link/-0144097069151776",
          "https://beeg.link/-0907668991261480",
          "https://beeg.link/-0477368231365512",
          "https://beeg.link/-0988052351192902",
          "https://beeg.link/-0518110183551039",
          "https://beeg.link/-0989700229248391",
          "https://beeg.link/-0483964108817717",
          "https://beeg.link/-0662706238115302",
          "https://beeg.link/-0526522518637096",
          "https://beeg.link/-0788120248050216",
          "https://beeg.link/-0305356357483432",
          "https://beeg.link/-0142753105677455",
          "https://beeg.link/-0319692042322365",
          "https://beeg.link/-0392592856615442",
          "https://beeg.link/-0393701501924886",
          "https://beeg.link/-0121031993652770",
          "https://beeg.link/-0311106773474712",
          "https://beeg.link/-0412832679354949",
          "https://beeg.link/-0236665979372803",
          "https://beeg.link/-0161369020844921",
          "https://beeg.link/-0960261401306261",
          "https://beeg.link/-0865368501325234",
          "https://beeg.link/-0257809880764115",
          "https://beeg.link/-0780522178964574",
          "https://beeg.link/-0285925857249616",
          "https://beeg.link/-0638873641832257",
          "https://beeg.link/-0538688725150396",
          "https://beeg.link/-0499296876484133",
          "https://beeg.link/-0197591774881474",
          "https://beeg.link/-0104169882005583",
          "https://beeg.link/-0396396566002175",
          "https://beeg.link/-0412301266831530",
          "https://beeg.link/-0248868572864880",
          "https://beeg.link/-0546441499446316",
          "https://beeg.link/-0323455669045506",
          "https://beeg.link/-0510212975630670",
          "https://beeg.link/-0877199594464297",
          "https://beeg.link/-0873855724928925",
          "https://beeg.link/-0488526495722731",
          "https://beeg.link/-0279897864966723",
          "https://beeg.link/-0261470614007603",
          "https://beeg.link/-0555293202624346",
          "https://beeg.link/-0327300878934350",
          "https://beeg.link/-0799338988439812",
          "https://beeg.link/-0150929806448105",
          "https://beeg.link/-0204420310907969",
          "https://beeg.link/-0286361201137150",
          "https://beeg.link/-0245591562187718",
          "https://beeg.link/-0685924371326281",
          "https://beeg.link/-0723407840344134",
          "https://beeg.link/-0152485815522887",
          "https://beeg.link/-0707293063033251",
          "https://beeg.link/-0243679087418627",
          "https://beeg.link/-0187039020715725",
          "https://beeg.link/-0646200611060639",
          "https://beeg.link/-0765937286942371",
          "https://beeg.link/-0498845031470674",
          "https://beeg.link/-0807311012596350",
          "https://beeg.link/-0648289857847419",
          "https://beeg.link/-0915539111426444",
          "https://beeg.link/-0270641686145308",
          "https://beeg.link/-0563707166679616",
          "https://beeg.link/-0917556357307913",
          "https://beeg.link/-0860436497118415",
          "https://beeg.link/-0446712828454061",
          "https://beeg.link/-0614779117401683",
          "https://beeg.link/-0721581419896008",
          "https://beeg.link/-0929572530023648",
          "https://beeg.link/-0778789968684589",
          "https://beeg.link/-0809538101461423",
          "https://beeg.link/-0684130333118753",
          "https://beeg.link/-0108986781443109",
          "https://beeg.link/-0100783833997168",
          "https://beeg.link/-0345383016576957",
          "https://beeg.link/-0621579475457194",
          "https://beeg.link/-0916541992897877",
          "https://beeg.link/-0696350867922419",
          "https://beeg.link/-0475938750628055",
          "https://beeg.link/-0954394038442315",
          "https://beeg.link/-0818659152381403",
          "https://beeg.link/-0813448284356419",
          "https://beeg.link/-0460993094608111",
          "https://beeg.link/-0585771167453270",
          "https://beeg.link/-0179475892110713",
          "https://beeg.link/-0694328171840825",
          "https://beeg.link/-0953423826063824",
          "https://beeg.link/-0727540806757848",
          "https://beeg.link/-0190057622510290",
          "https://beeg.link/-0912577939484991",
          "https://beeg.link/-0566974964728556",
          "https://beeg.link/-0281147412753469",
          "https://beeg.link/-0998497002103008",
          "https://beeg.link/-0482428148549077",
          "https://beeg.link/-0151113616959566",
          "https://beeg.link/-0407668130857580",
          "https://beeg.link/-0484339941385485",
          "https://beeg.link/-0787888262682744",
          "https://beeg.link/-0659200440409711",
          "https://beeg.link/-0565299830330354",
          "https://beeg.link/-0122669022699982",
          "https://beeg.link/-0782691707866752",
          "https://beeg.link/-0342821294899512",
          "https://beeg.link/-0464589383363012",
          "https://beeg.link/-0895215313659672",
          "https://beeg.link/-0350990960068205",
          "https://beeg.link/-0487602589747655",
          "https://beeg.link/-0857331884091629",
          "https://beeg.link/-0639490305888668",
          "https://beeg.link/-0260076568954136",
          "https://beeg.link/-0845143228200091",
          "https://beeg.link/-0659894776076257",
          "https://beeg.link/-0947271000713045",
          "https://beeg.link/-0139912831057276",
          "https://beeg.link/-0116850346700672",
          "https://beeg.link/-0778233484527146",
          "https://beeg.link/-0863456018160456",
          "https://beeg.link/-0673857907986881",
          "https://beeg.link/-0994043074498335",
          "https://beeg.link/-0941086672284294",
          "https://beeg.link/-0280862382662809",
          "https://beeg.link/-0615904382109700",
          "https://beeg.link/-0860468606635626",
          "https://beeg.link/-0967017176197988",
          "https://beeg.link/-0423827688117902",
          "https://beeg.link/-0462575797323634",
          "https://beeg.link/-0358365758447083",
          "https://beeg.link/-0504004815126977",
          "https://beeg.link/-0837013580989296",
          "https://beeg.link/-0503824551435592",
          "https://beeg.link/-0206900687239949",
          "https://beeg.link/-0711450063276461",
          "https://beeg.link/-0937995847943464",
          "https://beeg.link/-0697546694464041",
          "https://beeg.link/-0361790307693610",
          "https://beeg.link/-0553080002832608",
          "https://beeg.link/-0249560613900100",
          "https://beeg.link/-0325967682331433",
          "https://beeg.link/-0369417366630712",
          "https://beeg.link/-0919718078506349",
          "https://beeg.link/-0769326721718837",
          "https://beeg.link/-0847616677208244",
          "https://beeg.link/-0508742475998897",
          "https://beeg.link/-0928549218632341",
          "https://beeg.link/-0936237503873940",
          "https://beeg.link/-0424006342160508",
          "https://beeg.link/-0263087037851642",
          "https://beeg.link/-0439071304801968",
          "https://beeg.link/-0998191717447968",
          "https://beeg.link/-0798456489890291",
          "https://beeg.link/-0797931906317359",
          "https://beeg.link/-0759290675702989",
          "https://beeg.link/-0535055917652742",
          "https://beeg.link/-0450688000768228",
          "https://beeg.link/-0217639378751408",
          "https://beeg.link/-0387667318373279",
          "https://beeg.link/-0629191983039117",
          "https://beeg.link/-0128093545227961",
          "https://beeg.link/-0372590457418297",
          "https://beeg.link/-0893377274084283",
          "https://beeg.link/-0359383629401467",
          "https://beeg.link/-0929712924343254",
          "https://beeg.link/-0500716988073634",
          "https://beeg.link/-0865089678379005",
          "https://beeg.link/-0586598269518005",
          "https://beeg.link/-0584579964240420",
          "https://beeg.link/-0920738561372233",
          "https://beeg.link/-0266524481337954",
          "https://beeg.link/-0973018292821311",
          "https://beeg.link/-0899770642621090",
          "https://beeg.link/-0369265926891544",
          "https://beeg.link/-0507014820339381",
          "https://beeg.link/-0290985862512548",
          "https://beeg.link/-0939390334908207",
          "https://beeg.link/-0782719264182103",
          "https://beeg.link/-0920150769988925",
          "https://beeg.link/-0287343568437527",
          "https://beeg.link/-0391294060618854",
          "https://beeg.link/-0387557721095815",
          "https://beeg.link/-0562453762119397",
          "https://beeg.link/-0926437074967800",
          "https://beeg.link/-0612485432139298",
          "https://beeg.link/-0987501030820631",
          "https://beeg.link/-0441154667247993",
          "https://beeg.link/-0499941592086974",
          "https://beeg.link/-0886978264508460",
          "https://beeg.link/-0195608547666254",
          "https://beeg.link/-0180115073587327",
          "https://beeg.link/-0397206238270725",
          "https://beeg.link/-0738949660514703",
          "https://beeg.link/-0324104718629489",
          "https://beeg.link/-0121806541969467",
          "https://beeg.link/-0692502756426950",
          "https://beeg.link/-0304819617302280",
          "https://beeg.link/-0722687157337560",
          "https://beeg.link/-0326411768663889",
          "https://beeg.link/-0538272154558276",
          "https://beeg.link/-0876197410228272",
          "https://beeg.link/-0424291608255177",
          "https://beeg.link/-0961467202777029",
          "https://beeg.link/-0307925929341673",
          "https://beeg.link/-0636039612462149",
          "https://beeg.link/-0843266716632831",
          "https://beeg.link/-0590762815871962",
          "https://beeg.link/-0418939521458029",
          "https://beeg.link/-0830706610840868",
          "https://beeg.link/-0492048261707287",
          "https://beeg.link/-0939961757462469",
          "https://beeg.link/-0841722808848714",
          "https://beeg.link/-0890092726222695",
          "https://beeg.link/-0113779219568350",
          "https://beeg.link/-0774346059149755",
          "https://beeg.link/-0243222012930315",
          "https://beeg.link/-0424613668655705",
          "https://beeg.link/-0791856506743848",
          "https://beeg.link/-0782979867491736",
          "https://beeg.link/-0546439440729551",
          "https://beeg.link/-0245839039279449",
          "https://beeg.link/-0140080370628644",
          "https://beeg.link/-0889428226756332",
          "https://beeg.link/-0843948324680646",
          "https://beeg.link/-0194776352852864",
          "https://beeg.link/-0656233061829659",
          "https://beeg.link/-0473535340065362",
          "https://beeg.link/-0846740929016836",
          "https://beeg.link/-0261318179745574",
          "https://beeg.link/-0383012863285725",
          "https://beeg.link/-0189559801687777",
          "https://beeg.link/-0497011942475512",
          "https://beeg.link/-0378405153038195",
          "https://beeg.link/-0759956815621729",
          "https://beeg.link/-0432357548866972",
          "https://beeg.link/-0705303672846854",
          "https://beeg.link/-0201357511486309",
          "https://beeg.link/-0790125949709361",
          "https://beeg.link/-0234067838411414",
          "https://beeg.link/-0858944159851952",
          "https://beeg.link/-0646547463601063",
          "https://beeg.link/-0711231734988458",
          "https://beeg.link/-0947267777696277",
          "https://beeg.link/-0881338514433214",
          "https://beeg.link/-0482288835092719",
          "https://beeg.link/-0166994931361611",
          "https://beeg.link/-0366060765145139",
          "https://beeg.link/-0895033133061522",
          "https://beeg.link/-0877868265806699",
          "https://beeg.link/-0246954985921136",
          "https://beeg.link/-0270850756498511",
          "https://beeg.link/-0381949152506992",
          "https://beeg.link/-0283532883446888",
          "https://beeg.link/-0501847369980313",
          "https://beeg.link/-0233272531262244",
          "https://beeg.link/-0185872550958318",
          "https://beeg.link/-0799728020408275",
          "https://beeg.link/-0309438588784468",
          "https://beeg.link/-0149262500795284",
          "https://beeg.link/-0335439685317158",
          "https://beeg.link/-0869760285350994",
          "https://beeg.link/-0638960594051915",
          "https://beeg.link/-0720303115450580",
          "https://beeg.link/-0690138083385269",
          "https://beeg.link/-0731154185573374",
          "https://beeg.link/-0916848849474646",
          "https://beeg.link/-0747677567682379",
          "https://beeg.link/-0762564783077091",
          "https://beeg.link/-0483924946749744",
          "https://beeg.link/-0579393019273795",
          "https://beeg.link/-0893991991736430",
          "https://beeg.link/-0796145485031366",
          "https://beeg.link/-0203492562805458",
          "https://beeg.link/-0102272769322217",
          "https://beeg.link/-0648307165168519",
          "https://beeg.link/-0197045084514907",
          "https://beeg.link/-0112204466670182",
          "https://beeg.link/-0208853781807071",
          "https://beeg.link/-0436082004258140",
          "https://beeg.link/-0644155919089986",
          "https://beeg.link/-0967861690201686",
          "https://beeg.link/-0285750943232176",
          "https://beeg.link/-0191072802734264",
          "https://beeg.link/-0812296419572851",
          "https://beeg.link/-0414710528936389",
          "https://beeg.link/-0343253449390124",
          "https://beeg.link/-0102390418425045",
          "https://beeg.link/-0746081987983668",
          "https://beeg.link/-0563265107561189",
          "https://beeg.link/-0592556600440282",
          "https://beeg.link/-0859910281016871",
          "https://beeg.link/-0269316827394375",
          "https://beeg.link/-0741746120100427",
          "https://beeg.link/-0797896085510836",
          "https://beeg.link/-0615125173537964",
          "https://beeg.link/-0351526894462093",
          "https://beeg.link/-0870301955604775",
          "https://beeg.link/-0263264200916139",
          "https://beeg.link/-0863574133032745",
          "https://beeg.link/-0889904444356140",
          "https://beeg.link/-0563075811412794",
          "https://beeg.link/-0867794428773835",
          "https://beeg.link/-0114127878802336",
          "https://beeg.link/-0851881811605120",
          "https://beeg.link/-0141406270368579",
          "https://beeg.link/-0464883886310190",
          "https://beeg.link/-0290782460920176",
          "https://beeg.link/-0785277740402211",
          "https://beeg.link/-0925871190777279",
          "https://beeg.link/-0272836018220860",
          "https://beeg.link/-0189303769429378",
          "https://beeg.link/-0989185623364923",
          "https://beeg.link/-0238427409361806",
          "https://beeg.link/-0235261583666157",
          "https://beeg.link/-0390867882622949",
          "https://beeg.link/-0880651285018067",
          "https://beeg.link/-0432004960244737",
          "https://beeg.link/-0200120380285681",
          "https://beeg.link/-0263755376711139",
          "https://beeg.link/-0619677586541778",
          "https://beeg.link/-0909738462434144",
          "https://beeg.link/-0455174315594136",
          "https://beeg.link/-0752259977054472",
          "https://beeg.link/-0995094178576658",
          "https://beeg.link/-0288244095022054",
          "https://beeg.link/-0236667569917286",
          "https://beeg.link/-0766743905194962",
          "https://beeg.link/-0958725260641881",
        ],
        urlsJMTV: [
          "https://www.jacquieetmicheltv.net/?dscl=1&ab=0&utm_medium=traffic&utm_source=thepornator&utm_campaign=JMTV_Home_Popunder&affiliate=0f5d50f7-8900-4952-b9ad-815f31f86ef7",
        ],
        urlsUnClothy: [
          "https://unclothy.com/?utm_source=thepornator&utm_medium=referral&utm_campaign=june",
        ],
        urlsDeepMode: ["https://deepmode.com?fpr=thepornator"],
        urlsPornxAi: [
          "https://pornx.ai/search?feed=trending&ref=nmzkmjl&tap_s=4004563-883473&tm_campaign=popunder",
        ],
        urlsCandy: urlsCandySelect,
      };
      var weights = {
        urlsBeeg: 40,
        urlsJMTV: 0,
        urlsUnClothy: 0,
        urlsPornxAi: 10,
        urlsCandy: 40,
        urlsDeepMode: 10,
      };
      if (window.location.href.indexOf("/fr/") > -1) {
        weights = {
          urlsBeeg: 40,
          urlsJMTV: 0,
          urlsUnClothy: 0,
          urlsPornxAi: 25,
          urlsCandy: 30,
          urlsDeepMode: 10,
        };
      }
      const selectedGroup = getRandomUrlGroup(urlGroups, weights);
      const randomUrl = getRandomUrl(selectedGroup);
      var popunderurl = randomUrl;
      window.location.href = popunderurl;
      document.getElementById("disclaimer-popup").style.display = "none";
      var date = new Date();
      date.setTime(date.getTime() + 1 * 24 * 60 * 60 * 1000);
      var expires = "; expires=" + date.toGMTString();
      document.cookie = "disclaimer-shown=true" + expires + "; path=/";
    });
  var linksout = document.querySelectorAll('a[href^="/out/"]');
  for (var i = 0; i < linksout.length; i++) {
    linksout[i].addEventListener("click", function (event) {
      var href = this.getAttribute("href");
      var type = "";
      if (href.includes("video_")) {
        type = "video";
      } else if (href.includes("model_")) {
        type = "model";
      } else {
        type = "site";
      }
    });
  }
});
async function loadBannersJson(jsonPath) {
  try {
    const response = await fetch(jsonPath);
    if (!response.ok) {
      throw new Error("Network response was not ok " + response.statusText);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    return [];
  }
}
async function initializeBanners() {
  // const arrayBanners = await loadBannersJson('/assets/json/banners.json?t=' + Math.floor(Date.now() / 1000));
  insertAdsBannerByZoneId(arrayBanners, "topbanner", "top");
  insertAdsBannerByZoneId(arrayBanners, "middleads6", "middle");
  insertAdsBannerByZoneId(arrayBanners, "middleads8", "middle");
  insertAdsBannerByZoneId(arrayBanners, "middleads12", "middle");
  insertAdsBannerByZoneId(arrayBanners, "middleads16", "middle");
  insertAdsBannerByZoneId(arrayBanners, "middleads24", "middle");
  insertAdsBannerByZoneId(arrayBanners, "middleads32", "middle");
  insertAdsBannerByZoneId(arrayBanners, "middleads40", "middle");
  insertAdsBannerByZoneId(arrayBanners, "middleads48", "middle");
  insertAdsBannerByZoneId(arrayBanners, "middleads56", "middle");
  insertAdsBannerByZoneId(arrayBanners, "middleads64", "middle");
  insertAdsBannerByZoneId(arrayBanners, "middleads72", "middle");
  insertAdsBannerByZoneId(arrayBanners, "middleads80", "middle");
  insertAdsBannerByZoneId(arrayBanners, "bottombanner", "bottom");
}
(function () {
  "use strict";
  const select = (el, all = false) => {
    el = el.trim();
    if (all) {
      return [...document.querySelectorAll(el)];
    } else {
      if (el != "") return document.querySelector(el);
    }
  };
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all);
    if (selectEl) {
      if (all) {
        selectEl.forEach((e) => e.addEventListener(type, listener));
      } else {
        selectEl.addEventListener(type, listener);
      }
    }
  };
  const onscroll = (el, listener) => {
    el.addEventListener("scroll", listener);
  };
  let navbarlinks = select("#navbar .scrollto", true);
  const navbarlinksActive = () => {
    let position = window.scrollY + 200;
    navbarlinks.forEach((navbarlink) => {
      if (!navbarlink.hash) return;
      let section = select(navbarlink.hash);
      if (!section) return;
      if (
        position >= section.offsetTop &&
        position <= section.offsetTop + section.offsetHeight
      ) {
        navbarlink.classList.add("active");
      } else {
        navbarlink.classList.remove("active");
      }
    });
  };
  window.addEventListener("load", navbarlinksActive);
  onscroll(document, navbarlinksActive);
  const scrollto = (el) => {
    let header = select("#header");
    let offset = header.offsetHeight;
    let elementPos = select(el).offsetTop;
    window.scrollTo({
      top: elementPos - offset,
      behavior: "smooth",
    });
  };
  let selectHeader = select("#header");
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add("header-scrolled");
      } else {
        selectHeader.classList.remove("header-scrolled");
      }
    };
    window.addEventListener("load", headerScrolled);
    onscroll(document, headerScrolled);
  }
  let backtotop = select(".back-to-top");
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add("active");
      } else {
        backtotop.classList.remove("active");
      }
    };
    window.addEventListener("load", toggleBacktotop);
    onscroll(document, toggleBacktotop);
  }
  on("click", ".mobile-nav-toggle", function (e) {
    select("#navbar").classList.toggle("navbar-mobile");
    this.classList.toggle("bx-x-circle");
  });
  on(
    "click",
    ".navbar .dropdown > a",
    function (e) {
      if (select("#navbar").classList.contains("navbar-mobile")) {
        e.preventDefault();
        this.nextElementSibling.classList.toggle("dropdown-active");
      }
    },
    true
  );
  on(
    "click",
    ".scrollto",
    function (e) {
      if (select(this.hash)) {
        e.preventDefault();
        let navbar = select("#navbar");
        if (navbar.classList.contains("navbar-mobile")) {
          navbar.classList.remove("navbar-mobile");
          let navbarToggle = select(".mobile-nav-toggle");
          navbarToggle.classList.toggle("bi-list");
          navbarToggle.classList.toggle("bi-x");
        }
        scrollto(this.hash);
      }
    },
    true
  );
  window.addEventListener("load", () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash);
      }
    }
    initializeBanners();
  });
})();
function insertAdsBannerByZoneId(arrayBanners, zoneid, zone) {
  var adsDiv = document.getElementById(zoneid);
  if (adsDiv) {
    adsDiv.appendChild(getRandomBanner(arrayBanners, zone));
  }
}
function getBannerByCriteria(arrayBanners, lang, device, zone) {
  var eligibleBanners = "";
  if (lang !== null && device !== null && zone !== null) {
    eligibleBanners = arrayBanners.filter((banner) => {
      const bannerLangs = banner.lang.split("|");
      const bannerZones = banner.zone.split("|");
      return (
        bannerLangs.includes(lang) &&
        bannerZones.includes(zone) &&
        banner.device === device
      );
    });
  } else {
    if (device !== null)
      eligibleBanners = arrayBanners.filter(
        (banner) => banner.device === device
      );
  }
  if (eligibleBanners.length === 0) {
    return null;
  }
  const totalWeight = eligibleBanners.reduce(
    (sum, banner) => sum + banner.weight,
    0
  );
  const randomWeightedNumber = Math.random() * totalWeight;
  let cumulativeWeight = 0;
  for (const banner of eligibleBanners) {
    cumulativeWeight += banner.weight;
    if (randomWeightedNumber <= cumulativeWeight) {
      return {
        targetUrl: banner.targetUrl,
        imagename: banner.imagename,
      };
    }
  }
  return null;
}
function getRandomBanner(arrayBanners, zone) {
  var div = document.createElement("div");
  div.style.justifyContent = "center";
  div.style.display = "flex";
  var targeturl = "";
  var imagename = "";
  var img = document.createElement("img");
  var lang = "en";
  if (window.location.href.indexOf("/fr/") > -1) lang = "fr";
  if (window.innerWidth > 600) {
    let randomDesktopBanner = getBannerByCriteria(
      arrayBanners,
      lang,
      "desktop",
      zone
    );
    img.src = "/assets/img/banners/" + randomDesktopBanner.imagename;
    targeturl = randomDesktopBanner.targetUrl;
    imagename = randomDesktopBanner.imagename;
    img.style.maxHeight = "150px";
    img.alt = randomDesktopBanner.imagename;
  } else {
    let randomMobileBanner = getBannerByCriteria(
      arrayBanners,
      lang,
      "mobile",
      zone
    );
    img.src = "/assets/img/banners/" + randomMobileBanner.imagename;
    img.alt = randomMobileBanner.imagename;
    targeturl = randomMobileBanner.targetUrl;
    imagename = randomMobileBanner.imagename;
  }
  img.style.cursor = "pointer";
  img.onclick = function () {
    window.open(targeturl, "_blank");
  };
  div.appendChild(img);
  return div;
}
function addSondageAsync(answer) {
  var xhr = null;
  if (window.XMLHttpRequest) {
    xhr = new XMLHttpRequest();
  } else if (window.ActiveXObject) {
    xhr = new ActiveXObject("Microsoft.XMLHTTP");
  }
  document.getElementById("was-this-helpful").innerHTML =
    '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>&nbsp;&nbsp;Envoi de votre réponse';
  xhr.open(
    "GET",
    "/php/controller.php?action=addSondageVote&answer=" + answer,
    true
  );
  xhr.send(null);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4) {
      document.getElementById("was-this-helpful").innerHTML =
        "Merci pour votre participation !";
    }
  };
}
function getParameterByName(name, url = window.location.href) {
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
    results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return "";
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}
function loadMoreResults(page, start, lang, category, site) {
  var xhr = null;
  if (window.XMLHttpRequest) {
    xhr = new XMLHttpRequest();
  } else if (window.ActiveXObject) {
    xhr = new ActiveXObject("Microsoft.XMLHTTP");
  }
  document.querySelector("#btnmore_" + start).innerHTML =
    '<img src="/assets/img/loading.gif" style="width: 100px;margin-bottom: 20px;" />';
  xhr.open(
    "GET",
    "/php/controller.php?action=loadmoremodels&page=" +
      page +
      "&category=" +
      category +
      "&site=" +
      site +
      "&start=" +
      start +
      "&lang=" +
      lang,
    true
  );
  xhr.send(null);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4) {
      document.getElementById("divmore_" + start).innerHTML = this.responseText;
      document.getElementById("btnmore_" + start).remove();
    }
  };
}
/*!lazysizes - v5.3.2*/
!(function (e) {
  var t = (function (u, D, f) {
    "use strict";
    var k, H;
    if (
      ((function () {
        var e;
        var t = {
          lazyClass: "lazyload",
          loadedClass: "lazyloaded",
          loadingClass: "lazyloading",
          preloadClass: "lazypreload",
          errorClass: "lazyerror",
          autosizesClass: "lazyautosizes",
          fastLoadedClass: "ls-is-cached",
          iframeLoadMode: 0,
          srcAttr: "data-src",
          srcsetAttr: "data-srcset",
          sizesAttr: "data-sizes",
          minSize: 40,
          customMedia: {},
          init: true,
          expFactor: 1.5,
          hFac: 0.8,
          loadMode: 2,
          loadHidden: true,
          ricTimeout: 0,
          throttleDelay: 125,
        };
        H = u.lazySizesConfig || u.lazysizesConfig || {};
        for (e in t) {
          if (!(e in H)) {
            H[e] = t[e];
          }
        }
      })(),
      !D || !D.getElementsByClassName)
    ) {
      return {
        init: function () {},
        cfg: H,
        noSupport: true,
      };
    }
    var O = D.documentElement,
      i = u.HTMLPictureElement,
      P = "addEventListener",
      $ = "getAttribute",
      q = u[P].bind(u),
      I = u.setTimeout,
      U = u.requestAnimationFrame || I,
      o = u.requestIdleCallback,
      j = /^picture$/i,
      r = ["load", "error", "lazyincluded", "_lazyloaded"],
      a = {},
      G = Array.prototype.forEach,
      J = function (e, t) {
        if (!a[t]) {
          a[t] = new RegExp("(\\s|^)" + t + "(\\s|$)");
        }
        return a[t].test(e[$]("class") || "") && a[t];
      },
      K = function (e, t) {
        if (!J(e, t)) {
          e.setAttribute("class", (e[$]("class") || "").trim() + " " + t);
        }
      },
      Q = function (e, t) {
        var a;
        if ((a = J(e, t))) {
          e.setAttribute("class", (e[$]("class") || "").replace(a, " "));
        }
      },
      V = function (t, a, e) {
        var i = e ? P : "removeEventListener";
        if (e) {
          V(t, a);
        }
        r.forEach(function (e) {
          t[i](e, a);
        });
      },
      X = function (e, t, a, i, r) {
        var n = D.createEvent("Event");
        if (!a) {
          a = {};
        }
        a.instance = k;
        n.initEvent(t, !i, !r);
        n.detail = a;
        e.dispatchEvent(n);
        return n;
      },
      Y = function (e, t) {
        var a;
        if (!i && (a = u.picturefill || H.pf)) {
          if (t && t.src && !e[$]("srcset")) {
            e.setAttribute("srcset", t.src);
          }
          a({
            reevaluate: true,
            elements: [e],
          });
        } else if (t && t.src) {
          e.src = t.src;
        }
      },
      Z = function (e, t) {
        return (getComputedStyle(e, null) || {})[t];
      },
      s = function (e, t, a) {
        a = a || e.offsetWidth;
        while (a < H.minSize && t && !e._lazysizesWidth) {
          a = t.offsetWidth;
          t = t.parentNode;
        }
        return a;
      },
      ee = (function () {
        var a, i;
        var t = [];
        var r = [];
        var n = t;
        var s = function () {
          var e = n;
          n = t.length ? r : t;
          a = true;
          i = false;
          while (e.length) {
            e.shift()();
          }
          a = false;
        };
        var e = function (e, t) {
          if (a && !t) {
            e.apply(this, arguments);
          } else {
            n.push(e);
            if (!i) {
              i = true;
              (D.hidden ? I : U)(s);
            }
          }
        };
        e._lsFlush = s;
        return e;
      })(),
      te = function (a, e) {
        return e
          ? function () {
              ee(a);
            }
          : function () {
              var e = this;
              var t = arguments;
              ee(function () {
                a.apply(e, t);
              });
            };
      },
      ae = function (e) {
        var a;
        var i = 0;
        var r = H.throttleDelay;
        var n = H.ricTimeout;
        var t = function () {
          a = false;
          i = f.now();
          e();
        };
        var s =
          o && n > 49
            ? function () {
                o(t, {
                  timeout: n,
                });
                if (n !== H.ricTimeout) {
                  n = H.ricTimeout;
                }
              }
            : te(function () {
                I(t);
              }, true);
        return function (e) {
          var t;
          if ((e = e === true)) {
            n = 33;
          }
          if (a) {
            return;
          }
          a = true;
          t = r - (f.now() - i);
          if (t < 0) {
            t = 0;
          }
          if (e || t < 9) {
            s();
          } else {
            I(s, t);
          }
        };
      },
      ie = function (e) {
        var t, a;
        var i = 99;
        var r = function () {
          t = null;
          e();
        };
        var n = function () {
          var e = f.now() - a;
          if (e < i) {
            I(n, i - e);
          } else {
            (o || r)(r);
          }
        };
        return function () {
          a = f.now();
          if (!t) {
            t = I(n, i);
          }
        };
      },
      e = (function () {
        var v, m, c, h, e;
        var y, z, g, p, C, b, A;
        var n = /^img$/i;
        var d = /^iframe$/i;
        var E = "onscroll" in u && !/(gle|ing)bot/.test(navigator.userAgent);
        var _ = 0;
        var w = 0;
        var M = 0;
        var N = -1;
        var L = function (e) {
          M--;
          if (!e || M < 0 || !e.target) {
            M = 0;
          }
        };
        var x = function (e) {
          if (A == null) {
            A = Z(D.body, "visibility") == "hidden";
          }
          return (
            A ||
            !(
              Z(e.parentNode, "visibility") == "hidden" &&
              Z(e, "visibility") == "hidden"
            )
          );
        };
        var W = function (e, t) {
          var a;
          var i = e;
          var r = x(e);
          g -= t;
          b += t;
          p -= t;
          C += t;
          while (r && (i = i.offsetParent) && i != D.body && i != O) {
            r = (Z(i, "opacity") || 1) > 0;
            if (r && Z(i, "overflow") != "visible") {
              a = i.getBoundingClientRect();
              r =
                C > a.left && p < a.right && b > a.top - 1 && g < a.bottom + 1;
            }
          }
          return r;
        };
        var t = function () {
          var e, t, a, i, r, n, s, o, l, u, f, c;
          var d = k.elements;
          if ((h = H.loadMode) && M < 8 && (e = d.length)) {
            t = 0;
            N++;
            for (; t < e; t++) {
              if (!d[t] || d[t]._lazyRace) {
                continue;
              }
              if (!E || (k.prematureUnveil && k.prematureUnveil(d[t]))) {
                R(d[t]);
                continue;
              }
              if (!(o = d[t][$]("data-expand")) || !(n = o * 1)) {
                n = w;
              }
              if (!u) {
                u =
                  !H.expand || H.expand < 1
                    ? O.clientHeight > 500 && O.clientWidth > 500
                      ? 500
                      : 370
                    : H.expand;
                k._defEx = u;
                f = u * H.expFactor;
                c = H.hFac;
                A = null;
                if (w < f && M < 1 && N > 2 && h > 2 && !D.hidden) {
                  w = f;
                  N = 0;
                } else if (h > 1 && N > 1 && M < 6) {
                  w = u;
                } else {
                  w = _;
                }
              }
              if (l !== n) {
                y = innerWidth + n * c;
                z = innerHeight + n;
                s = n * -1;
                l = n;
              }
              a = d[t].getBoundingClientRect();
              if (
                (b = a.bottom) >= s &&
                (g = a.top) <= z &&
                (C = a.right) >= s * c &&
                (p = a.left) <= y &&
                (b || C || p || g) &&
                (H.loadHidden || x(d[t])) &&
                ((m && M < 3 && !o && (h < 3 || N < 4)) || W(d[t], n))
              ) {
                R(d[t]);
                r = true;
                if (M > 9) {
                  break;
                }
              } else if (
                !r &&
                m &&
                !i &&
                M < 4 &&
                N < 4 &&
                h > 2 &&
                (v[0] || H.preloadAfterLoad) &&
                (v[0] ||
                  (!o && (b || C || p || g || d[t][$](H.sizesAttr) != "auto")))
              ) {
                i = v[0] || d[t];
              }
            }
            if (i && !r) {
              R(i);
            }
          }
        };
        var a = ae(t);
        var S = function (e) {
          var t = e.target;
          if (t._lazyCache) {
            delete t._lazyCache;
            return;
          }
          L(e);
          K(t, H.loadedClass);
          Q(t, H.loadingClass);
          V(t, B);
          X(t, "lazyloaded");
        };
        var i = te(S);
        var B = function (e) {
          i({
            target: e.target,
          });
        };
        var T = function (e, t) {
          var a = e.getAttribute("data-load-mode") || H.iframeLoadMode;
          if (a == 0) {
            e.contentWindow.location.replace(t);
          } else if (a == 1) {
            e.src = t;
          }
        };
        var F = function (e) {
          var t;
          var a = e[$](H.srcsetAttr);
          if ((t = H.customMedia[e[$]("data-media") || e[$]("media")])) {
            e.setAttribute("media", t);
          }
          if (a) {
            e.setAttribute("srcset", a);
          }
        };
        var s = te(function (t, e, a, i, r) {
          var n, s, o, l, u, f;
          if (!(u = X(t, "lazybeforeunveil", e)).defaultPrevented) {
            if (i) {
              if (a) {
                K(t, H.autosizesClass);
              } else {
                t.setAttribute("sizes", i);
              }
            }
            s = t[$](H.srcsetAttr);
            n = t[$](H.srcAttr);
            if (r) {
              o = t.parentNode;
              l = o && j.test(o.nodeName || "");
            }
            f = e.firesLoad || ("src" in t && (s || n || l));
            u = {
              target: t,
            };
            K(t, H.loadingClass);
            if (f) {
              clearTimeout(c);
              c = I(L, 2500);
              V(t, B, true);
            }
            if (l) {
              G.call(o.getElementsByTagName("source"), F);
            }
            if (s) {
              t.setAttribute("srcset", s);
            } else if (n && !l) {
              if (d.test(t.nodeName)) {
                T(t, n);
              } else {
                t.src = n;
              }
            }
            if (r && (s || l)) {
              Y(t, {
                src: n,
              });
            }
          }
          if (t._lazyRace) {
            delete t._lazyRace;
          }
          Q(t, H.lazyClass);
          ee(function () {
            var e = t.complete && t.naturalWidth > 1;
            if (!f || e) {
              if (e) {
                K(t, H.fastLoadedClass);
              }
              S(u);
              t._lazyCache = true;
              I(function () {
                if ("_lazyCache" in t) {
                  delete t._lazyCache;
                }
              }, 9);
            }
            if (t.loading == "lazy") {
              M--;
            }
          }, true);
        });
        var R = function (e) {
          if (e._lazyRace) {
            return;
          }
          var t;
          var a = n.test(e.nodeName);
          var i = a && (e[$](H.sizesAttr) || e[$]("sizes"));
          var r = i == "auto";
          if (
            (r || !m) &&
            a &&
            (e[$]("src") || e.srcset) &&
            !e.complete &&
            !J(e, H.errorClass) &&
            J(e, H.lazyClass)
          ) {
            return;
          }
          t = X(e, "lazyunveilread").detail;
          if (r) {
            re.updateElem(e, true, e.offsetWidth);
          }
          e._lazyRace = true;
          M++;
          s(e, t, r, i, a);
        };
        var r = ie(function () {
          H.loadMode = 3;
          a();
        });
        var o = function () {
          if (H.loadMode == 3) {
            H.loadMode = 2;
          }
          r();
        };
        var l = function () {
          if (m) {
            return;
          }
          if (f.now() - e < 999) {
            I(l, 999);
            return;
          }
          m = true;
          H.loadMode = 3;
          a();
          q("scroll", o, true);
        };
        return {
          _: function () {
            e = f.now();
            k.elements = D.getElementsByClassName(H.lazyClass);
            v = D.getElementsByClassName(H.lazyClass + " " + H.preloadClass);
            q("scroll", a, true);
            q("resize", a, true);
            q("pageshow", function (e) {
              if (e.persisted) {
                var t = D.querySelectorAll("." + H.loadingClass);
                if (t.length && t.forEach) {
                  U(function () {
                    t.forEach(function (e) {
                      if (e.complete) {
                        R(e);
                      }
                    });
                  });
                }
              }
            });
            if (u.MutationObserver) {
              new MutationObserver(a).observe(O, {
                childList: true,
                subtree: true,
                attributes: true,
              });
            } else {
              O[P]("DOMNodeInserted", a, true);
              O[P]("DOMAttrModified", a, true);
              setInterval(a, 999);
            }
            q("hashchange", a, true);
            [
              "focus",
              "mouseover",
              "click",
              "load",
              "transitionend",
              "animationend",
            ].forEach(function (e) {
              D[P](e, a, true);
            });
            if (/d$|^c/.test(D.readyState)) {
              l();
            } else {
              q("load", l);
              D[P]("DOMContentLoaded", a);
              I(l, 2e4);
            }
            if (k.elements.length) {
              t();
              ee._lsFlush();
            } else {
              a();
            }
          },
          checkElems: a,
          unveil: R,
          _aLSL: o,
        };
      })(),
      re = (function () {
        var a;
        var n = te(function (e, t, a, i) {
          var r, n, s;
          e._lazysizesWidth = i;
          i += "px";
          e.setAttribute("sizes", i);
          if (j.test(t.nodeName || "")) {
            r = t.getElementsByTagName("source");
            for (n = 0, s = r.length; n < s; n++) {
              r[n].setAttribute("sizes", i);
            }
          }
          if (!a.detail.dataAttr) {
            Y(e, a.detail);
          }
        });
        var i = function (e, t, a) {
          var i;
          var r = e.parentNode;
          if (r) {
            a = s(e, r, a);
            i = X(e, "lazybeforesizes", {
              width: a,
              dataAttr: !!t,
            });
            if (!i.defaultPrevented) {
              a = i.detail.width;
              if (a && a !== e._lazysizesWidth) {
                n(e, r, i, a);
              }
            }
          }
        };
        var e = function () {
          var e;
          var t = a.length;
          if (t) {
            e = 0;
            for (; e < t; e++) {
              i(a[e]);
            }
          }
        };
        var t = ie(e);
        return {
          _: function () {
            a = D.getElementsByClassName(H.autosizesClass);
            q("resize", t);
          },
          checkElems: t,
          updateElem: i,
        };
      })(),
      t = function () {
        if (!t.i && D.getElementsByClassName) {
          t.i = true;
          re._();
          e._();
        }
      };
    return (
      I(function () {
        H.init && t();
      }),
      (k = {
        cfg: H,
        autoSizer: re,
        loader: e,
        init: t,
        uP: Y,
        aC: K,
        rC: Q,
        hC: J,
        fire: X,
        gW: s,
        rAF: ee,
      })
    );
  })(e, e.document, Date);
  (e.lazySizes = t),
    "object" == typeof module && module.exports && (module.exports = t);
})("undefined" != typeof window ? window : {});
function displayVideoRatingButtons(id) {
  var divElement = document.getElementById(id);
  divElement.classList.add("rating-active");
}
function hideVideoRatingButtons(id) {
  var divElement = document.getElementById(id);
  divElement.classList.remove("rating-active");
}
function updateVideoDetailUpDownAsync(score, slug, lang) {
  var xhr = null;
  if (window.XMLHttpRequest) {
    xhr = new XMLHttpRequest();
  } else if (window.ActiveXObject) {
    xhr = new ActiveXObject("Microsoft.XMLHTTP");
  }
  var allDivRating = document.getElementById(slug);
  var videoslug = slug.replace("video_", "");
  var divRatingUp = document.getElementById("ratingup_" + videoslug);
  var divRatingDown = document.getElementById("ratingdown_" + videoslug);
  var divRatingNone = document.getElementById("ratingnone_" + videoslug);
  var thanksmsg = "Thanks for your vote!";
  if (lang == "fr") thanksmsg = "Merci pour votre vote !";
  xhr.open(
    "GET",
    "/php/controller.php?action=updateVideoDetailUpDown&score=" +
      score +
      "&slug=" +
      videoslug,
    true
  );
  xhr.send(null);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4) {
      if (score == 1) {
        divRatingDown.style.display = "none";
        divRatingNone.style.display = "none";
        divRatingUp.onclick = null;
        divRatingUp.innerHTML +=
          '<span style="font-size:0.8rem;line-height: 1;">' +
          thanksmsg +
          "</span>";
      } else if (score == -1) {
        divRatingUp.style.display = "none";
        divRatingNone.style.display = "none";
        divRatingDown.onclick = null;
        divRatingDown.innerHTML +=
          '<span style="font-size:0.8rem;line-height: 1;">' +
          thanksmsg +
          "</span>";
      } else {
        allDivRating.classList.remove("rating-active");
      }
      setTimeout(function () {
        allDivRating.classList.remove("rating-active");
      }, 3000);
    }
  };
}
function showMoreLetter(letter, action, seeless, seemore) {
  if (action == 1) {
    document.getElementById("showmore_" + letter).innerHTML = seeless;
    document.getElementById("showmore_" + letter).href =
      "javascript:showMoreLetter('" +
      letter +
      "', 0, '" +
      seeless +
      "', '" +
      seemore +
      "');";
    var elements = document.getElementsByClassName("hidden_" + letter);
    for (let i = 0; i < elements.length; i++) {
      elements[i].classList.remove("hidden");
    }
  } else {
    document.getElementById("showmore_" + letter).innerHTML = seemore;
    document.getElementById("showmore_" + letter).href =
      "javascript:showMoreLetter('" +
      letter +
      "', 1, '" +
      seeless +
      "', '" +
      seemore +
      "');";
    var elements = document.getElementsByClassName("hidden_" + letter);
    for (let i = 0; i < elements.length; i++) {
      elements[i].classList.add("hidden");
    }
  }
}
function validateAdminAiContentForm() {
  var checkboxes = document.getElementsByName("tags[]");
  var checked = false;
  for (var i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked) {
      checked = true;
      break;
    }
  }
  if (!checked) {
    alert("Please select at least one tag.");
    return false;
  }
  return true;
}
export function displayModelsList(modelsprofile, link) {
  let res = "";
  if (modelsprofile) {
    res += `
                <div class="d-block d-md-flex listing col-lg-12" style="padding: 10px;">
                    <div class="img-avatar col-lg-3 col-md-3">
                        <div class="img-avatar-container" style="position: relative;">
                            <a rel="nofollow" href="${link}" target="_blank" rel="noopener" referrerpolicy="origin">
                                <img src="${
                                  modelsprofile.photo
                                }" style="width:200px;height:200px;" alt="${
      modelsprofile.pseudo
    }">
                            </a>
                            <a href="#" style="position: absolute;bottom: 0;left: 50%;transform: translateX(-50%);">
                                <img src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" data-src="/assets/img/logomodelsites/onlyfans.webp" class="lazyload" style="width: 50px;height: auto;" alt="onlyfans">
                            </a>
                        </div>
                    </div>
                    <div class="result-container col-lg-9 col-md-9">
                        <a rel="nofollow" href="${link}" target="_blank" rel="noopener" referrerpolicy="origin">
                            <svg style="width:1em;" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M10.75 5.5C10.75 3.42893 12.4289 1.75 14.5 1.75C16.5711 1.75 18.25 3.42893 18.25 5.5C18.25 7.57107 16.5711 9.25 14.5 9.25C13.7339 9.25 13.0214 9.02026 12.4278 8.62592L11.3519 9.7018C12.229 10.36 13.319 10.75 14.5 10.75C17.3995 10.75 19.75 8.3995 19.75 5.5C19.75 2.60051 17.3995 0.25 14.5 0.25C11.6005 0.25 9.25 2.60051 9.25 5.5C9.25 6.67746 9.63763 7.76439 10.2922 8.64014L11.3685 7.56385C10.9776 6.97187 10.75 6.26251 10.75 5.5Z" fill="black"></path>
                                <path d="M14.5574 4.375L15.618 5.43566L5.4357 15.618L4.37504 14.5573L14.5574 4.375Z" fill="black"></path>
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M8.64014 10.2922C7.76439 9.63763 6.67746 9.25 5.5 9.25C2.60051 9.25 0.25 11.6005 0.25 14.5C0.25 17.3995 2.60051 19.75 5.5 19.75C8.3995 19.75 10.75 17.3995 10.75 14.5C10.75 13.319 10.36 12.229 9.7018 11.3519L8.62592 12.4278C9.02026 13.0214 9.25 13.7339 9.25 14.5C9.25 16.5711 7.57107 18.25 5.5 18.25C3.42893 18.25 1.75 16.5711 1.75 14.5C1.75 12.4289 3.42893 10.75 5.5 10.75C6.26251 10.75 6.97187 10.9776 7.56385 11.3685L8.64014 10.2922Z" fill="black"></path>
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M14.5574 2.96078L17.0322 5.43566L5.43569 17.0322L2.96082 14.5573L14.5574 2.96078ZM14.5574 4.375L4.37504 14.5573L5.4357 15.618L15.618 5.43566L14.5574 4.375Z" fill="white"></path>
                            </svg>
                            <span style="vertical-align: middle;">${limiterString(
                              "https://onlyfans.com/out/" + modelsprofile.slug,
                              45
                            )}</span>
                            <br>
                            <h3 style="font-weight: bold;">${
                              modelsprofile.pseudo
                            }</h3>
                        </a>
                        <div class="pb-3 text-muted about" style="max-height:150px;overflow-y: auto;margin-bottom: 15px;">${
                          modelsprofile.description
                        }</div>
                        <div class="profile-info">`;
    if (modelsprofile.nblikes && modelsprofile.nblikes > 0) {
      res += `
                            <span class="mr-3">
                                <i class="bx bxs-heart"></i>
                                &nbsp; <strong>${modelsprofile.nblikes}</strong>
                            </span>`;
    }
    if (modelsprofile.nbphotos && modelsprofile.nbphotos > 0) {
      res += `
                            <span class="mr-3">
                                <i class="bx bxs-camera"></i>
                                &nbsp;<strong>${modelsprofile.nbphotos}</strong>
                            </span>`;
    }
    if (modelsprofile.nbvideos && modelsprofile.nbvideos > 0) {
      res += `
                            <span class="mr-3">
                                <i class="bx bxs-video"></i>
                                &nbsp;<strong>${modelsprofile.nbvideos}</strong>
                            </span>`;
    }
    if (modelsprofile.nbposts && modelsprofile.nbposts > 0) {
      res += `
                            <span class="mr-3">
                                <i class="bx bxs-note"></i>
                                &nbsp;<strong>${modelsprofile.nbposts}</strong>
                            </span>`;
    }
    if (modelsprofile.price) {
      res += `
                            <span class="mr-3">
                                <i class="bx bxs-dollar-circle"></i>&nbsp;<strong>${modelsprofile.price}</strong>
                            </span>`;
    }
    res += `
                        </div>
                    </div>
                </div>`;
  }
  return res;
}
function limiterString(str, maxLength) {
  if (str.length > maxLength) {
    return str.substring(0, maxLength) + "...";
  }
  return str;
}
function insertModelHTML(modelsProfiles) {
  const targetDivs = document.querySelectorAll(
    ".d-block.d-md-flex.listing.col-lg-12"
  );
  if (targetDivs.length < 2) {
    console.error("Il n'y a pas assez de divs pour insérer le contenu.");
    return;
  }
  targetDivs.forEach((div, index) => {
    if (index < targetDivs.length - 1) {
      const nextDiv = targetDivs[index + 1];
      const modelsProfile = modelsProfiles[index];
      if (modelsProfile) {
        const link = modelsProfile.link;
        const modelHTML = displayModelsList(modelsProfile, link);
        nextDiv.insertAdjacentHTML("beforebegin", modelHTML);
      }
    }
  });
}
function fetchAndInsertModels() {
  fetch(
    "https://ctads.rtbsuperhub.com/creative4/?count=15&tpcampid=27d4ab04-cae6-4213-a7da-07805256ef4d"
  )
    .then((response) => response.json())
    .then((data) => {
      const modelsProfiles = data.map((item) => {
        const modelData = JSON.parse(item.adm.native.assets[1].data.value);
        const link = item.adm.native.link;
        return {
          id: modelData.id,
          pseudo: modelData.name,
          photo: modelData.imgUrl,
          description: modelData.description,
          nblikes: modelData.likeCount,
          nbphotos: modelData.photosCount,
          nbvideos: modelData.videosCount,
          nbposts: modelData.postsCount,
          price: modelData.price,
          background: "",
          modelssite: "",
          modelscategories: "",
          slug: modelData.profile_name,
          link: link,
        };
      });
      insertModelHTML(modelsProfiles);
    })
    .catch((error) => console.error("Error fetching data:", error));
}
await initPages();
