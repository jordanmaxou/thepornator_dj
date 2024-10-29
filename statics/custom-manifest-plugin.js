const fs = require('fs');
const path = require('path');
const micromatch = require('micromatch');

class CustomManifestPlugin {
  constructor(options) {
    this.options = options || {};
    this.manifestFileName = this.options.filename || 'manifest.json';
    this.include = this.options.include || [];
  }

  apply(compiler) {
    compiler.hooks.emit.tapAsync('CustomManifestPlugin', (compilation, callback) => {
      const manifest = {};

      for (const filename in compilation.assets) {
        if(this.include.length === 0 || micromatch.isMatch(filename, this.include)){
          const originalName = filename.replace(/\.[a-f0-9]+\./, '.');
          manifest[originalName] = filename;
        }
      }

      const manifestJson = JSON.stringify(manifest, null, 2);

      compilation.assets[this.manifestFileName] = {
        source: () => manifestJson,
        size: () => manifestJson.length,
      };

      callback();
    });
  }
}

module.exports = CustomManifestPlugin;
