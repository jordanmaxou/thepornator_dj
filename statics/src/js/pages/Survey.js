import translations from "../libs/translations/index.js";

const Answer = Object.freeze({
  STRONGLY_DISAGREE: 1,
  DISAGREE: 2,
  NEUTRAL: 3,
  AGREE: 4,
  STRONGLY_AGREE: 5,
});

export class Survey {
  #startTime;
  #questions;
  #currentQuestionPosition;
  #actionUrl;
  #messageBlockId = "fake";

  constructor() {
    this.#questions = this.getQuestions();
    this.#currentQuestionPosition = 0;
    this.#startTime = null;
    this.#actionUrl = document.getElementById("buttons")?.dataset?.actionUrl;
  }

  start() {
    if (this.#questions.length > 0) {
      this.initButtons();
      this.displayNextQuestion();
      this.#startTime = new Date();
    }
  }

  initButtons() {
    this.initAnswerButton("strong-agree", Answer.STRONGLY_AGREE);
    this.initAnswerButton("agree", Answer.AGREE);
    this.initAnswerButton("neutral", Answer.NEUTRAL);
    this.initAnswerButton("disagree", Answer.DISAGREE);
    this.initAnswerButton("strong-disagree", Answer.STRONGLY_DISAGREE);
    document.getElementById("back-button").addEventListener("click", () => {
      this.prevQuestion();
    });
  }

  initAnswerButton(className, answer) {
    Array.from(document.getElementsByClassName(className)).forEach(
      (element) => {
        element.addEventListener("click", async () => {
          await this.nextQuestion(answer);
        });
      }
    );
  }

  displayNextQuestion() {
    const question = this.#questions[this.#currentQuestionPosition];
    this.updateQuestionAndProgressDisplay(
      question.question,
      this.#currentQuestionPosition,
      this.#questions.length
    );
    this.updateButtonsDisplay(
      this.#currentQuestionPosition,
      this.#questions.length
    );
  }

  updateQuestionAndProgressDisplay(question, position, totalQuestions) {
    const percent = Math.round((position / totalQuestions) * 100);

    document.getElementById("question-text").innerHTML = question;
    document.getElementById("question-number").innerHTML = `Question ${
      position + 1
    } / ${totalQuestions}`;
    this.updateProgressDisplay(percent);
  }

  updateProgressDisplay(percent) {
    document.getElementById("progress").innerHTML = `
      <div class="progress-bar" role="progressbar" style="width:${percent}%;" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100">
        ${percent}%
      </div>
    `;
  }

  updateButtonsDisplay(position, totalQuestions) {
    if (position === 0) {
      this.toggleElementVisibility("back-button", false);
      this.toggleElementVisibility("back-button-home", true);
      this.toggleElementVisibility("buttons", true);
    } else {
      this.toggleElementVisibility("back-button", true);
      this.toggleElementVisibility("back-button-home", false);

      if (position > totalQuestions) {
        this.toggleElementVisibility("buttons", false);
      } else {
        this.toggleElementVisibility("buttons", true);
      }
    }
  }

  toggleElementVisibility(elementId, isVisible) {
    document.getElementById(elementId).style.display = isVisible
      ? "block"
      : "none";
  }

  getQuestions() {
    const surveyQuestionsScriptElement =
      document.getElementById("survey-questions");
    if (surveyQuestionsScriptElement) {
      const rawQuestions = surveyQuestionsScriptElement.textContent;
      if (rawQuestions) {
        try {
          return JSON.parse(rawQuestions);
        } catch (e) {
          throw Error(`A problem occurs during questions retrieval ${e}`);
        }
      }
    }
    throw Error("A problem occurs during questions retrieval");
  }

  async nextQuestion(answer) {
    // register current answer
    this.#questions[this.#currentQuestionPosition].answer = answer;

    // next question
    this.#currentQuestionPosition++;

    if (this.#currentQuestionPosition < this.#questions.length) {
      this.displayNextQuestion();
    } else {
      this.updateProgressDisplay(100);
      await this.showResults();
    }
  }

  prevQuestion() {
    if (this.#currentQuestionPosition > 0) {
      this.#currentQuestionPosition--;
      this.displayNextQuestion();
    }
  }

  getSurveyDuration() {
    const endTime = new Date();
    const timeDiff = (endTime - this.#startTime) / 1000;
    return Math.round(timeDiff);
  }

  fakeTreatment() {
    const messages = [
      "",
      translations("collectresponses"),
      translations("collectdatasites"),
      translations("calculsimil"),
      translations("idrecommend"),
      translations("finalresult"),
    ];

    let percent = 0;
    let i = 0;

    const interval = setInterval(() => {
      document.getElementById("fake").innerHTML = `
        <div class="progress">
          <div class="progress-bar progress-bar-striped bg-success" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <br>
        <button class="btn btn-outline-success btn-lg" style="border:0px;" type="button" disabled>
          <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
          ${messages[i]}
        </button>
      `;
      percent += 20;
      i++;

      if (percent > 100) {
        clearInterval(interval);
      }
    }, 1500);
  }

  async saveResultsAsync(values, duration) {
    try {
      const csrftoken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
      const response = await fetch(this.#actionUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        mode: "same-origin",
        body: JSON.stringify({
          notes: values,
          duration: duration,
        }),
      });

      if (response.ok) {
        return { data: await response.json() };
      }
      return { status: response.status };
    } catch (error) {
      console.error("An error occurred while saving results:", error);
    }
  }

  async showResults() {
    const duration = this.getSurveyDuration();
    const result = await this.saveResultsAsync(
      this.#questions.map((value) => {
        return { id: value.id, answer: value.answer };
      }),
      duration
    );
    if (result?.data && result?.data?.redirect_url) {
      this.fakeTreatment();
      location.href = result.data.redirect_url;
    } else {
      if (result?.status === 406) {
        this.displayRobotSuspicionMessage();
      } else {
        this.displayErrorMessage();
      }
    }
  }

  displayRobotSuspicionMessage() {
    document.getElementById(
      this.#messageBlockId
    ).innerHTML = `<div class="error-message alert alert-danger">${translations(
      "robotSuspicion"
    )}</div>`;
  }

  displayErrorMessage() {
    document.getElementById(
      this.#messageBlockId
    ).innerHTML = `<div class="error-message alert alert-danger">${translations(
      "errorMessage"
    )}</div>`;
  }
}
