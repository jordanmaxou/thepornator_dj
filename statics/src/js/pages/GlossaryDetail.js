export class GlossaryDetail {
  #ratingContainerId = "rating";
  #ratingContainer;
  #voteUrl;
  #voteButtons;
  #nbUpId = "nbup";
  #nbUp;
  #nbDownId = "nbdown";
  #nbDown;

  constructor() {
    this.#ratingContainer = document.getElementById(this.#ratingContainerId);
    this.#voteUrl = this.#ratingContainer.dataset.url;
    this.#voteButtons = this.#ratingContainer.querySelectorAll("button");
    this.#nbUp = document.getElementById(this.#nbUpId);
    this.#nbDown = document.getElementById(this.#nbDownId);
  }

  start() {
    Array.from(this.#voteButtons).forEach((button) => {
      button.addEventListener("click", async () => {
        const counts = await this.sendVote(button.dataset.value);
        this.#nbUp.innerText = counts.up;
        this.#nbDown.innerText = counts.down;
        this.disableVoteButtons();
      });
    });
  }

  async sendVote(type_vote) {
    try {
      const csrftoken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
      const response = await fetch(this.#voteUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        mode: "same-origin",
        body: JSON.stringify({
          type: type_vote,
        }),
      });

      if (response.ok) {
        return await response.json();
      }
    } catch (error) {
      console.error("An error occurred during result update", error);
    }
  }

  disableVoteButtons() {
    Array.from(this.#voteButtons).forEach((button) => {
      button.disabled = true;
    });
  }
}
