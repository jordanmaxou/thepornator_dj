import { shuffleArray } from "../libs/utils/index.js";

export class AiGame {
  #countDownInSeconds = 20;
  #introId = "intro";
  #intro;
  #resultId = "result";
  #result;
  #dataId = "data-pictures";
  #data;
  #frameId = "frame";
  #frame;
  #startButtonId = "start-button";
  #startButton;
  #playButtonsId = "play-buttons";
  #playButtons;
  #progressContainerId = "progress";
  #progressContainer;
  #progressBar;
  #mainGameContainerId = "main-game";
  #mainGameContainer;
  #addScoreUrl;
  #scoreId = "score";
  #scoreSpan;
  #fakeButtonId = "fake";
  #fakeButton;
  #realButtonId = "real";
  #realButton;

  constructor() {
    this.#data = shuffleArray(
      JSON.parse(document.getElementById(this.#dataId)?.textContent ?? "{}")
    );
    this.#frame = document.getElementById(this.#frameId);
    this.#startButton = document.getElementById(this.#startButtonId);
    this.#intro = document.getElementById(this.#introId);
    this.#result = document.getElementById(this.#resultId);
    this.#playButtons = document.getElementById(this.#playButtonsId);
    this.#progressContainer = document.getElementById(
      this.#progressContainerId
    );
    if (this.#progressContainer) {
      this.#progressBar =
        this.#progressContainer.querySelector(".progress-bar");
    }
    this.#mainGameContainer = document.getElementById(
      this.#mainGameContainerId
    );
    this.#addScoreUrl = this.#mainGameContainer?.dataset?.url;

    this.startX = 0;
    this.startY = 0;
    this.moveX = 0;
    this.moveY = 0;
    this.results = this.#data.reduce((acc, value) => {
      acc[value.id] = 0;
      return acc;
    }, {});
    this.#scoreSpan = document.getElementById(this.#scoreId);
    this.#realButton = document.getElementById(this.#realButtonId);
    this.#fakeButton = document.getElementById(this.#fakeButtonId);
    this.count = this.#countDownInSeconds;
    this.twitterLink = document.querySelector(".btn-twitter");
    this.facebookLink = document.querySelector(".btn-facebook");
    this.redditLink = document.querySelector(".btn-reddit");
  }

  start() {
    this.injectCards();
    this.currentCard = this.#frame.querySelector(".card:last-child");
    this.initCard(this.currentCard);
    this.initButtons();
    this.#startButton.addEventListener("click", () => {
      this.play();
    });
  }

  initButtons() {
    this.#fakeButton.addEventListener("click", () => {
      this.moveX = -1;
      this.moveY = 0;
      this.complete();
    });
    this.#realButton.addEventListener("click", () => {
      this.moveX = 1;
      this.moveY = 0;
      this.complete();
    });
  }

  scroll() {
    if (window.innerWidth <= 768) position = 250;
    else position = 100;
    window.scrollTo({ top: position, behavior: "smooth" });
  }

  play() {
    scroll();
    this.#intro.style.display = "none";
    this.#frame.style.display = "block";
    this.#result.style.display = "none";
    this.#startButton.style.display = "none";
    this.#playButtons.style.display = "block";
    this.#progressContainer.style.display = "flex";
    this.#progressBar.style.width = "100%";
    this.timer = setInterval(() => this.countDown(), 1000);
  }

  async countDown() {
    this.count--;
    this.#progressBar.style.width =
      ((this.count + 1) / this.#countDownInSeconds) * 100 + "%";
    if (this.count < 0) {
      await this.endGame();
    }
  }

  injectCards() {
    this.#data.forEach((picture) => {
      this.#frame.insertAdjacentHTML("beforeend", this.getCard(picture));
    });
  }

  getCard(picture) {
    return `
      <div class="card"
           data-id="${picture.id}"
           style="background-image: url('${picture.file}');">
      </div>`;
  }

  initCard(card) {
    card.addEventListener("pointerdown", this.onPointerDown);
  }

  setTransform(x, y, deg, duration) {
    this.currentCard.style.transform = `translate3d(${x}px, ${y}px, 0) rotate(${deg}deg)`;
    if (duration) this.currentCard.style.transition = `transform ${duration}ms`;
  }

  onPointerDown = ({ clientX, clientY }) => {
    this.startX = clientX;
    this.startY = clientY;
    this.currentCard.addEventListener("pointermove", this.onPointerMove);
    this.currentCard.addEventListener("pointerup", this.onPointerUp);
    this.currentCard.addEventListener("pointerleave", this.onPointerUp);
  };

  onPointerMove = ({ clientX, clientY }) => {
    this.moveX = clientX - this.startX;
    this.moveY = clientY - this.startY;
    this.setTransform(this.moveX, this.moveY, (this.moveX / innerWidth) * 50);
  };

  onPointerUp = async () => {
    this.currentCard.removeEventListener("pointermove", this.onPointerMove);
    this.currentCard.removeEventListener("pointerup", this.onPointerUp);
    this.currentCard.removeEventListener("pointerleave", this.onPointerUp);
    if (Math.abs(this.moveX) > frame.clientWidth / 2) {
      this.currentCard.removeEventListener("pointerdown", this.onPointerDown);
      await this.complete();
    } else {
      this.cancel();
    }
  };

  async complete() {
    const flyX = (Math.abs(this.moveX) / this.moveX) * innerWidth * 1.3;
    const flyY = (this.moveY / this.moveX) * flyX;
    this.setTransform(flyX, flyY, (flyX / innerWidth) * 50, innerWidth);

    const prev = this.currentCard;
    const next = this.currentCard.previousElementSibling;

    var real = -1;
    if (this.moveX > 0) real = 1;
    this.results[prev.dataset.id] = real;

    if (next) {
      this.initCard(next);
      this.currentCard = next;
      const frame = this.#frame;
      setTimeout(() => frame.removeChild(prev), innerWidth);
    } else {
      await this.endGame();
    }
    scroll();
  }

  cancel() {
    this.setTransform(0, 0, 0, 100);
    setTimeout(() => (this.currentCard.style.transition = ""), 100);
  }

  async sendAnswers() {
    try {
      const csrftoken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
      const response = await fetch(this.#addScoreUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        mode: "same-origin",
        body: JSON.stringify(this.results),
      });

      if (response.ok) {
        return await response.json();
      }
    } catch (error) {
      console.error("An error occurred during score sending", error);
    }
  }

  async endGame() {
    if (this.timer) {
      clearInterval(this.timer);
    }
    this.#startButton.style.display = "block";
    this.#playButtons.style.display = "none";
    this.#frame.style.display = "none";
    const response = await this.sendAnswers();
    console.log(response);
    if (response && "score" in response) {
      if (response.score == 20) {
        this.#result.querySelector(".perfect").style.display = "inline";
      } else if (response.score > 15) {
        this.#result.querySelector(".good").style.display = "inline";
      } else if (response.score > 10) {
        this.#result.querySelector(".average").style.display = "inline";
      } else {
        this.#result.querySelector(".bad").style.display = "inline";
      }
      this.#scoreSpan.innerText = response.score;
      this.twitterLink.href = response.social_urls.twitter;
      this.facebookLink.href = response.social_urls.facebook;
      this.redditLink.href = response.social_urls.reddit;
      this.#result.style.display = "block";
      this.#progressContainer.style.display = "none";
      this.#mainGameContainer.style.overflow = "unset";
    }
  }
}
