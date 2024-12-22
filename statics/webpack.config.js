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
    bootstrap: "./src/js/bootstrap.bundle.js",
    bypass: "./src/js/bypass.js",
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
        {
          from: path.resolve(__dirname, "src/admin"),
          to: path.resolve(__dirname, "dist/admin"),
        },
        {
          from: path.resolve(__dirname, "src/debug_toolbar"),
          to: path.resolve(__dirname, "dist/debug_toolbar"),
        },
        {
          from: path.resolve(__dirname, "src/tinymce"),
          to: path.resolve(__dirname, "dist/tinymce"),
        },
        {
          from: path.resolve(__dirname, "src/django_tinymce"),
          to: path.resolve(__dirname, "dist/django_tinymce"),
        },
        {
          from: path.resolve(__dirname, "src/favicon.ico"),
          to: path.resolve(__dirname, "dist/favicon.ico"),
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
