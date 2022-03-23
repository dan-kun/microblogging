/* eslint-disable no-undef */
const path = require("path");
const BundleTracker = require("webpack-bundle-tracker");
const { VueLoaderPlugin } = require("vue-loader");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin"); // Elimina los archivos antes de generar el bundle

module.exports = {
  mode: "development",
  devtool: "inline-source-map",
  entry: ["./src/main.js"],
  output: {
    publicPath: "/static/dist/",
    filename: "[name]-[hash].js",
    chunkFilename: "[name]-[hash].js",
    path: path.resolve("../static/dist/"),
  },

  plugins: [
    new VueLoaderPlugin(),
    new BundleTracker({ filename: "./webpack-stats.json" }),
    new CleanWebpackPlugin(),
    new MiniCssExtractPlugin({
      filename: "[name]-[hash].css",
    }),
  ],

  module: {
    rules: [
      {
        test: /\.vue$/,
        use: "vue-loader",
      },
      {
        test: /\.postcss$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
          },
          {
            loader: "css-loader",
            options: {
              importLoaders: 1,
            },
          },
          {
            loader: "postcss-loader",
          },
        ],
      },
    ],
  },
}