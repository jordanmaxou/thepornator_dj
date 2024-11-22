import path from "path";
import { fileURLToPath } from "url";
import MiniCssExtractPlugin from "mini-css-extract-plugin";
import CopyWebpackPlugin from "copy-webpack-plugin";
import { CustomManifestPlugin } from "./custom-manifest-plugin.js";
import { CleanWebpackPlugin } from "clean-webpack-plugin";
const __dirname = path.dirname(fileURLToPath(import.meta.url));

export default {
  entry: {
    main: "./src/js/main.js",
    chart: "./src/js/chart.js",
  },
  stats: {
    warnings: false,
  },
  output: {
    library: "lib",
    filename: "[name].[contenthash:5].js",
    path: path.resolve(__dirname, "dist"),
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "main.[contenthash:5].css",
    }),
    new CopyWebpackPlugin({
      patterns: [
        {
          from: path.resolve(__dirname, "src/img"),
          to: path.resolve(__dirname, "dist/img"),
          globOptions: {
            ignore: ["**/*.js", "**/*.css"],
          },
        },
      ],
    }),
    new CustomManifestPlugin({
      include: ["**/*.js", "**/*.css"],
    }),
    new CleanWebpackPlugin(),
  ],
  module: {
    rules: [
      {
        test: /\.(scss)$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
          },
          {
            loader: "css-loader",
          },
          {
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                plugins: () => [require("autoprefixer")],
              },
            },
          },
          {
            loader: "sass-loader",
          },
        ],
      },
    ],
  },
};
