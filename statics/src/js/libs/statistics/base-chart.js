export class BaseChart {
  dataId;
  data;
  canvasId;
  canvas;

  init() {
    const dataContainer = document.getElementById(this.dataId);
    if (dataContainer) {
      this.data = JSON.parse(
        document.getElementById(this.dataId)?.textContent ?? {}
      );
      this.canvas = document.getElementById(this.canvasId);
      if (this.canvas) {
        return true;
      }
      console.error(`Can't find container with id '${this.canvasId}'`);
    } else {
      console.error(`Can't find container with id '${this.dataId}'`);
    }
    return false;
  }
}
