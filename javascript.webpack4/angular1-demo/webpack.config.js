// const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin')

const isDev = process.env.NODE_ENV !== 'production'
module.exports = {
  entry: {
    app: './app/app.js'
  },
  module: {
    rules: [
      {
        enforce: 'pre',
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'eslint-loader',
          options: {
            fix: true,
            emitError: true
          }
        },
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {loader: 'babel-loader'}
      },
      {
        test: /assets\/.*\.(jpg|png)$/,
        use: {
          loader: 'file-loader',
          options: {
            name: 'assets/[name].[hash].[ext]',
          },
        },
      },
      {
        test: /\.html$/,
        use: [
          {
            loader: 'html-loader',
            options: {
              minimize: true
            }
          }
        ]
      },
      {
        test: /\.s?[ac]ss$/,
        use: [
          isDev ? 'style-loader' : MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
        ],
      }
    ]
  },
  plugins: [
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      template: 'app/index.html',
      filename: 'index.html'
    }),
    new MiniCssExtractPlugin({
      filename: isDev ? '[name].css' : '[name].[hash].css',
      chunkFilename: isDev ? '[id].css' : '[id].[hash].css',
    })
  ]
}
