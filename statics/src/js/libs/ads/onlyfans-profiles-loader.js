export class OnlyfansProfilesLoader {
  constructor() {}

  start() {
    this.fetchAndInsertModels();
  }

  insertModelHTML(modelsProfiles) {
    const targetDivs = document.querySelectorAll(
      ".d-block.d-md-flex.listing.col-lg-12"
    );
    if (targetDivs.length < 2) {
      console.error("Not enough container to insert content.");
      return;
    }
    targetDivs.forEach((_, index) => {
      if (index < targetDivs.length - 1) {
        const nextDiv = targetDivs[index + 1];
        const modelsProfile = modelsProfiles[index];
        if (modelsProfile) {
          const link = modelsProfile.link;
          const modelHTML = this.displayModelsList(modelsProfile, link);
          nextDiv.insertAdjacentHTML("beforebegin", modelHTML);
        }
      }
    });
  }

  fetchAndInsertModels() {
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
        this.insertModelHTML(modelsProfiles);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }

  displayModelsList(modelsprofile, link) {
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
                            <span style="vertical-align: middle;">${this.limiterString(
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

  limiterString(str, maxLength) {
    if (str.length > maxLength) {
      return str.substring(0, maxLength) + "...";
    }
    return str;
  }
}
