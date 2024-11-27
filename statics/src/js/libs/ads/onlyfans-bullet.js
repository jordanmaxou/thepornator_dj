import translate from "../translations/index.js";

export class OnlyfansBullet {
  #modelProfileUrl =
    "https://ctads.rtbsuperhub.com/creative4/?count=1&tpcampid=27d4ab04-cae6-4213-a7da-07805256ef4d";
  #bulletId = "bullet";
  #bulletContainer;
  #openModalButton;
  #modalContainer;
  #closeModalButton;
  #subscribeLink;

  constructor() {
    this.#bulletContainer = document.getElementById(this.#bulletId);
    this.#openModalButton =
      this.#bulletContainer?.querySelector(".modal-open-button");
    this.#closeModalButton = this.#bulletContainer?.querySelector(".close");
    this.#subscribeLink = this.#bulletContainer?.querySelector(".btn-success");
    this.#modalContainer = this.#bulletContainer?.querySelector(".modal");
  }

  async start() {
    await this.initModal();
  }

  async initModal() {
    const profile = await this.getModelProfileData();
    if (profile) {
      this.completeProfileHTML(profile);
      this.initModalEventListeners();
      this.display();
    }
  }

  display() {
    this.#bulletContainer.style.display = "block";
  }

  completeProfileHTML(profile) {
    this.completeBulletButtonImg(profile.photo);
    this.completeProfileInfo(profile);
    this.completeAboutProfile(profile);
    this.completeProfileLink(profile);
    this.completeAvatar(profile);
    this.completeButtonSuccess(profile);
  }

  completeBulletButtonImg(profilePhoto) {
    const img = this.#openModalButton.querySelector("img");
    img.src = profilePhoto;
  }

  completeProfileLink(profile) {
    const profileLinkContainer =
      this.#modalContainer.querySelector(".profile-link");
    profileLinkContainer.innerHTML = this.getProfileLinkHTML(profile);
    profileLinkContainer.href = profile.link;
  }

  getProfileLinkHTML(profile) {
    return `
      <svg style="width:1em"
                  viewBox="0 0 20 20"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M10.75 5.5C10.75 3.42893 12.4289 1.75 14.5 1.75C16.5711 1.75 18.25 3.42893 18.25 5.5C18.25 7.57107 16.5711 9.25 14.5 9.25C13.7339 9.25 13.0214 9.02026 12.4278 8.62592L11.3519 9.7018C12.229 10.36 13.319 10.75 14.5 10.75C17.3995 10.75 19.75 8.3995 19.75 5.5C19.75 2.60051 17.3995 0.25 14.5 0.25C11.6005 0.25 9.25 2.60051 9.25 5.5C9.25 6.67746 9.63763 7.76439 10.2922 8.64014L11.3685 7.56385C10.9776 6.97187 10.75 6.26251 10.75 5.5Z" fill="black">
          </path>
          <path d="M14.5574 4.375L15.618 5.43566L5.4357 15.618L4.37504 14.5573L14.5574 4.375Z" fill="black"></path>
          <path fill-rule="evenodd" clip-rule="evenodd" d="M8.64014 10.2922C7.76439 9.63763 6.67746 9.25 5.5 9.25C2.60051 9.25 0.25 11.6005 0.25 14.5C0.25 17.3995 2.60051 19.75 5.5 19.75C8.3995 19.75 10.75 17.3995 10.75 14.5C10.75 13.319 10.36 12.229 9.7018 11.3519L8.62592 12.4278C9.02026 13.0214 9.25 13.7339 9.25 14.5C9.25 16.5711 7.57107 18.25 5.5 18.25C3.42893 18.25 1.75 16.5711 1.75 14.5C1.75 12.4289 3.42893 10.75 5.5 10.75C6.26251 10.75 6.97187 10.9776 7.56385 11.3685L8.64014 10.2922Z" fill="black">
          </path>
          <path fill-rule="evenodd" clip-rule="evenodd" d="M14.5574 2.96078L17.0322 5.43566L5.43569 17.0322L2.96082 14.5573L14.5574 2.96078ZM14.5574 4.375L4.37504 14.5573L5.4357 15.618L15.618 5.43566L14.5574 4.375Z" fill="white">
          </path>
        </svg>
        <span style="vertical-align: middle;">${this.limiterString(
          "https://onlyfans.com/out/" + profile.slug,
          45
        )}</span>
        <br>
        <h3 style="font-weight: bold;">${profile.pseudo}</h3>
    `;
  }

  completeAvatar(profile) {
    const avatarContainer = this.#modalContainer.querySelector(".img-avatar");
    avatarContainer.innerHTML = this.getAvatarHTML(profile);
  }

  getAvatarHTML(profile) {
    return `                        
      <div class="img-avatar-container" style="position: relative;">
          <a rel="nofollow" href="${profile.link}" target="_blank" rel="noopener" referrerpolicy="origin">
              <img src="${profile.photo}" style="width:200px;height:200px;" alt="${profile.pseudo}">
          </a>
          <a href="#" style="position: absolute;bottom: 0;left: 50%;transform: translateX(-50%);">
              <img src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" data-src="/assets/img/logomodelsites/onlyfans.webp" class="lazyload" style="width: 50px;height: auto;" alt="onlyfans">
          </a>
      </div>
    `;
  }

  completeProfileInfo(profile) {
    const profileInfoContainer =
      this.#bulletContainer.querySelector(".profile-info");
    if (profileInfoContainer) {
      profileInfoContainer.innerHTML = this.getProfileInfoHTML(profile);
    }
  }

  completeAboutProfile(profile) {
    const profileAboutContainer = this.#bulletContainer.querySelector(".about");
    profileAboutContainer.innerHTML = profile.description;
  }

  getProfileInfoHTML(profile) {
    let html = "";
    if (profile.nblikes && profile.nblikes > 0) {
      html += `<span class="mr-3">
                <i class="bx bxs-heart"></i>
                &nbsp; <strong>${profile.nblikes}</strong>
              </span>`;
    }
    if (profile.nbphotos && profile.nbphotos > 0) {
      html += `<span class="mr-3">
                <i class="bx bxs-camera"></i>
                &nbsp;<strong>${profile.nbphotos}</strong>
              </span>
              `;
    }
    if (profile.nbvideos && profile.nbvideos > 0) {
      html += `<span class="mr-3">
                <i class="bx bxs-video"></i>
                &nbsp;<strong>${profile.nbvideos}</strong>
              </span>
              `;
    }
    if (profile.nbposts && profile.nbposts > 0) {
      html += `<span class="mr-3">
                <i class="bx bxs-note"></i>
                &nbsp;<strong>${profile.nbposts}</strong>
              </span>
              `;
    }
    if (profile.price) {
      html += `<span class="mr-3">
                <i class="bx bxs-dollar-circle"></i>
                &nbsp;<strong>${profile.price}</strong>
              </span>
              `;
    }
    return html;
  }

  completeButtonSuccess(profile) {
    this.#subscribeLink.href = profile.link;

    let buttonText = translate("subscribenowfree");
    if (profile.price && profile.price > 0) {
      buttonText = translate("subscribenow", { price: profile.price });
    }
    this.#subscribeLink.innerText = buttonText;
  }

  initModalEventListeners() {
    this.#openModalButton?.addEventListener("click", () => {
      this.#modalContainer.style.display = "block";
    });
    this.#closeModalButton.addEventListener("click", () => {
      this.#modalContainer.style.display = "none";
    });
    window.addEventListener("click", (event) => {
      if (event.target == this.#modalContainer) {
        this.#modalContainer.style.display = "none";
      }
    });
  }

  async getModelProfileData() {
    try {
      const response = await fetch(this.#modelProfileUrl);
      if (response.ok) {
        const data = await response.json();
        const modelData = JSON.parse(data[0].adm.native.assets[1].data.value);
        const link = data[0].adm.native.link;
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
          background: "", // not given
          modelssite: "", // not given
          modelscategories: "", // not given
          slug: modelData.profile_name, // used as slug
          link,
        };
      } else {
        throw Error("A problem occurs during model profile info retrieval");
      }
    } catch (error) {
      console.error("Model profiles retrieval failed: ", error);
    }
  }

  limiterString(str, maxLength) {
    if (str.length > maxLength) {
      return str.substring(0, maxLength) + "...";
    }
    return str;
  }
}
