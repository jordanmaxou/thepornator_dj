export class Banner {
  #getBannersUrl = "/banners/";
  #bannerContainers;
  #availableZones = ["top", "bottom", "middle"];

  constructor() {
    this.#bannerContainers = document.querySelectorAll(".banner");
  }
  async start() {
    const banners = await this.getBanners();
    this.insertAds(banners);
  }

  insertAds(banners) {
    Array.from(this.#bannerContainers).forEach((banner) => {
      const zone = banner?.dataset?.zone;
      const device = this.getDevice();
      if (zone && this.#availableZones.includes(zone)) {
        banner.insertAdjacentHTML(
          "afterbegin",
          this.buildBannerHTML(
            this.getRandomBanner(banners, device, zone),
            device
          )
        );
      } else {
        console.warn(
          "Banner container found but with no valid data zone value"
        );
      }
    });
  }
  async getBanners() {
    const response = await fetch(`${this.#getBannersUrl}?t=${Date.now()}`);
    if (response.ok) {
      const data = await response.json();
      if (data && data.banners) {
        return data.banners;
      }
    }
    throw Error("A problem occurs during banners retrieval");
  }

  getRandomBanner(banners, device, zone) {
    let eligibleBanners = "";
    if (device && zone) {
      eligibleBanners = banners.filter((banner) => {
        return banner.zones.includes(zone) && banner.device === device;
      });
    } else {
      if (device)
        eligibleBanners = banners.filter((banner) => banner.device === device);
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
          targetUrl: banner.target_url,
          imagePath: banner.image_path,
        };
      }
    }
    return null;
  }

  getDevice() {
    if (window.innerWidth > 600) {
      return "desktop";
    } else {
      return "mobile";
    }
  }

  buildBannerHTML(banner, device) {
    return `
      <div style="justify-content: center; display: flex;" >
        <img src="${banner.imagePath}" style="cursor: pointer; ${
      device === "desktop" ? "max-height: 150px" : ""
    }" onclick="window.open('${banner.targetUrl}', '_blank')" />
      </div>
    `;
  }
}
