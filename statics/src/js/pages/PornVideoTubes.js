import { VideosVote } from "../libs/videos/index.js";

export class PornVideoTubes {
  constructor() {
    this.videoVote = new VideosVote();
  }

  start() {
    this.videoVote.start();
  }
}
