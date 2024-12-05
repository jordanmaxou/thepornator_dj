import { VideosVote } from "../libs/videos/index.js";

export class Home {
  constructor() {
    this.videosVote = new VideosVote();
  }

  start() {
    this.videosVote.start();
  }
}
