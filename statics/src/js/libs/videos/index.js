import translate from "../../libs/translations/index.js";

export class VideosVote {
  #csrftoken;

  constructor() {
    this.#csrftoken = document.querySelector(
      "[name=csrfmiddlewaretoken]"
    ).value;
  }

  start() {
    Array.from(document.querySelectorAll("[data-url]")).forEach((content) => {
      const contentUrl = content.dataset.url;
      const itemRating = content.querySelector(".item-rating");
      Array.from(content.querySelectorAll("a")).forEach((a) => {
        a.addEventListener("click", () => {
          itemRating.classList.add("rating-active");
          itemRating
            .querySelector(".item-rating-up")
            .addEventListener("click", async () => {
              await this.voteUp(contentUrl, itemRating);
            });
          itemRating
            .querySelector(".item-rating-down")
            .addEventListener("click", async () => {
              await this.voteDown(contentUrl, itemRating);
            });
          itemRating
            .querySelector(".item-rating-none")
            .addEventListener("click", () => {
              this.removeRatingButtons(itemRating);
            });
        });
      });
    });
  }

  async voteUp(url, itemRatingElement) {
    await this.vote(url, "up", itemRatingElement);
  }

  async voteDown(url, itemRatingElement) {
    await this.vote(url, "down", itemRatingElement);
  }

  async vote(url, type, itemRatingElement) {
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": this.#csrftoken,
        },
        mode: "same-origin",
        body: JSON.stringify({
          type,
        }),
      });

      if (response.ok) {
        this.thanksUser(itemRatingElement, type);
      }
    } catch (error) {
      console.error("An error occurred during video content vote", error);
    }
  }
  removeRatingButtons(itemRating) {
    itemRating.classList.remove("rating-active");
    // fast way to remove all event listeners attached to
    itemRating.replaceWith(itemRating.cloneNode(true));
  }

  thanksUser(itemRating, type) {
    const itemRatingUp = itemRating.querySelector(".item-rating-up");
    const itemRatingDown = itemRating.querySelector(".item-rating-down");
    const itemRatingNone = itemRating.querySelector(".item-rating-none");
    if (type === "up") {
      itemRatingDown.style.display = "none";
      itemRatingNone.style.display = "none";
      itemRatingUp.innerHTML = `<span style="font-size:0.8rem;line-height: 1;">${translate(
        "thanksmsg"
      )}</span>`;
    } else if (type == "down") {
      itemRatingUp.style.display = "none";
      itemRatingNone.style.display = "none";
      itemRatingDown.innerHTML = `<span style="font-size:0.8rem;line-height: 1;">${translate(
        "thanksmsg"
      )}</span>`;
    }
    setTimeout(function () {
      itemRating.classList.remove("rating-active");
    }, 3000);
  }
}
