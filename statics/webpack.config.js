const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const CopyWebpackPlugin = require('copy-webpack-plugin');
const CustomManifestPlugin = require('./custom-manifest-plugin');


module.exports = {
  entry: './src/js/main.js',
  stats: {
    warnings: false
  },
  output: {
    filename: 'main.[contenthash:5].js',
    path: path.resolve(__dirname, 'dist'),
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'main.[contenthash:5].css'
    }),
    new CopyWebpackPlugin({
      patterns: [
        {
          from: path.resolve(__dirname, 'src/img'),
          to: path.resolve(__dirname, 'dist/img'),
          globOptions: {
            ignore: ['**/*.js', '**/*.css'],
          },
        },
      ],
    }),
    new CustomManifestPlugin({
      include: ['**/*.js', '**/*.css']
    })
  ],
  module: {
    rules: [
      {
        test: /\.(scss)$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: () => [
                  require('autoprefixer')
                ]
              }
            }
          },
          {
            loader: 'sass-loader'
          },
        ]
      }
    ]
  }
};
