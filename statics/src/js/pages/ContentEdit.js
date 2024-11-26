export class ContentEdit {
  #modalCategoriesFieldsId = "form-content";
  #modalCategoriesFields;
  #modalCountrySelectId = "country";
  #modalCountrySelect;
  #modalNbTagsNumberId = "nb-tags";
  #modalNbTagsNumber;
  #modalValidateButtonId = "btnvalidateedittags";
  #modalValidateButton;
  #modalFormId = "edit-form";
  #modalForm;
  #updateCategoriesCountryUrl;
  #updateVoteUrl;
  #thankYouMessageId = "thank-you-message";
  #thankYouMessageBlock;
  #voteButtonsId = "buttons-container";
  #voteButtonsContainer;
  #voteMessageId = "message-container";
  #voteMessageContainer;
  #updateVoteContentType;

  constructor() {
    this.#modalCategoriesFields = document.getElementById(
      this.#modalCategoriesFieldsId
    );
    this.#modalCountrySelect = document.getElementById(
      this.#modalCountrySelectId
    );
    this.#modalNbTagsNumber = document.getElementById(
      this.#modalNbTagsNumberId
    );
    this.#modalValidateButton = document.getElementById(
      this.#modalValidateButtonId
    );
    this.#modalForm = document.getElementById(this.#modalFormId);
    if (this.#modalForm) {
      this.#updateCategoriesCountryUrl = this.#modalForm?.action;
    }

    this.#thankYouMessageBlock = document.getElementById(
      this.#thankYouMessageId
    );

    this.#voteButtonsContainer = document.getElementById(this.#voteButtonsId);
    this.#updateVoteUrl = this.#voteButtonsContainer?.dataset?.url;
    this.#updateVoteContentType = this.#voteButtonsContainer?.dataset?.type;

    this.#voteMessageContainer = document.getElementById(this.#voteMessageId);
  }

  start() {
    this.initModal();
    this.initVote();
  }

  initModal() {
    if (this.#modalCategoriesFields && this.#modalNbTagsNumber) {
      this.#modalCategoriesFields
        .querySelectorAll(".checkbox")
        .forEach((checkbox) => {
          checkbox.addEventListener("change", () => {
            if (checkbox.checked === true) {
              this.#modalNbTagsNumber.innerText =
                parseInt(this.#modalNbTagsNumber.innerText) + 1;
            } else {
              this.#modalNbTagsNumber.innerText =
                parseInt(this.#modalNbTagsNumber.innerText) - 1;
            }
            const categoriesCounterUpdateEvent = new CustomEvent(
              "categoriesCounterUpdate",
              {
                detail: { counter: this.#modalNbTagsNumber.innerText }, // Tu peux passer d'autres informations ici
              }
            );
            this.#modalNbTagsNumber.dispatchEvent(categoriesCounterUpdateEvent);
          });
        });
      this.#modalNbTagsNumber.addEventListener(
        "categoriesCounterUpdate",
        (event) => {
          if (parseInt(event.detail.counter) > 9) {
            this.disableUncheckedCheckboxes();
          } else {
            this.enableUncheckedCheckboxes();
          }
        }
      );
    }
    if (this.#modalValidateButton) {
      this.#modalValidateButton.addEventListener("click", async (e) => {
        e.preventDefault();
        await this.sendCategoriesAndCountryUpdate();
      });
    }
  }

  disableUncheckedCheckboxes() {
    this.#modalCategoriesFields
      .querySelectorAll(".checkbox")
      .forEach((checkbox) => {
        if (!checkbox.checked) {
          checkbox.disabled = true;
        }
      });
  }

  enableUncheckedCheckboxes() {
    this.#modalCategoriesFields
      .querySelectorAll(".checkbox")
      .forEach((checkbox) => {
        if (!checkbox.checked) {
          checkbox.disabled = false;
        }
      });
  }

  getCategoriesAndCountryUserData() {
    return {
      categories: Array.from(
        this.#modalCategoriesFields.querySelectorAll(
          'input[type="checkbox"]:checked'
        )
      )
        .filter((item) => item.checked)
        .map((item) => item.value),
      country: this.#modalCountrySelect.value ?? null,
    };
  }

  async sendCategoriesAndCountryUpdate() {
    try {
      const csrftoken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
      const response = await fetch(this.#updateCategoriesCountryUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        mode: "same-origin",
        body: JSON.stringify(this.getCategoriesAndCountryUserData()),
      });

      if (response.ok) {
        this.displayThankYouMessageAndRefresh();
      }
    } catch (error) {
      console.error("An error occurred during result update", error);
    }
  }

  displayThankYouMessageAndRefresh() {
    this.#thankYouMessageBlock.style.display = "block";
    this.#modalForm.style.display = "none";
    setTimeout(function () {
      location.reload(true);
    }, 3000);
  }

  initVote() {
    this.#voteButtonsContainer
      .querySelectorAll(".vote-button")
      .forEach((voteButton) => {
        voteButton.addEventListener("click", async () => {
          const typeVote = voteButton?.dataset?.value;
          const typeContent = voteButton?.dataset?.type;
          if (typeVote && this.#updateVoteContentType) {
            await this.updateVote(typeVote, this.#updateVoteContentType);
          } else {
            console.error("Can't find vote value");
          }
        });
      });
  }

  async updateVote(type_vote, type_content) {
    try {
      const csrftoken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
      const response = await fetch(this.#updateVoteUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        mode: "same-origin",
        body: JSON.stringify({ vote: type_vote, type: type_content }),
      });

      if (response.ok) {
        const data = await response.json();
        if (data && data.next_url) {
          this.showMessageAndRedirect(data.next_url);
        } else {
          throw Error("Problem during vote http response processing");
        }
      }
    } catch (error) {
      console.error("An error occurred during vote", error);
    }
  }

  showMessageAndRedirect(url) {
    this.#voteButtonsContainer.style.display = "none";
    this.#voteMessageContainer.style.display = "block";
    let opacity = 0;
    const interval = setInterval(() => {
      opacity += 0.1;
      this.#voteMessageContainer.style.opacity = opacity;
      if (opacity >= 1) {
        clearInterval(interval);
        setTimeout(() => {
          window.location.href = url;
        }, 500);
      }
    }, 50);
  }
}
