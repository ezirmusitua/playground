# Webpack[4].Tutorial

[Webpack 4 Tutorial: from 0 Conf to Production Mode (Updated)](https://www.valentinog.com/blog/webpack-4-tutorial/)

---

## Zero Configuration

default entry: `src/index.js` ，overriding with: webpack `entry` 

default output: `dist/main.js` ，overriding with: webpack —output `output`

development mode: optimized for speed and does nothing more than providing an un-minified bundle

production mode: enables all sorts of optimizations out of the box. Including minification, scope hoisting, tree-shaking and more

## Babel Loader

    # install babel necessary  
    npm i babel-core babel-loader babel-preset-env --save-dev  
    # add babelrc  
    ## vim .babelrc
    { "presets": ["env"] }
    ## :wq  
    # add webpack config  
    ## vim webpack.config.js  
    module.exports = {
      module: {
        rules: [
          {
            test: /\.js$/,
            exclude: /node_modules/,
            use: { loader: "babel-loader" }
      }
    }
    ## :wq
    

## HTML Plugin

    # install html plugin and loader
    npm i html-webpack-plugin html-loader --save-dev
    # update webpack config  
    ## vim webpack.config.js  
    const HtmlWebpackPlugin = require('html-webpack-plugin');
    module.exports = { 
      module: {
    		// ...
    		rules: [
    			// ...
    			{
    				test: /\.html$/,
    				use: [
    					{
    						loader: "html-loader",
    						options: { minimize: true }
    					}
    				]
    			}
    			// ...
    		]
    		// ...
    	}
    	// ...
    	plugins: [
    		new HtmlWebPackPlugin({
    			template: "./src/index.html",
    			filename: "./index.html",
    		})
    	]
    };
    ## :wq

There's no need to include your JavaScript inside the HTML file: the bundle will be automatically injected.

## Extract CSS To A File

`**extract-text-webpack-plugin` is currently not working with webpack4 2018/06/04**

[mini-css-extract-plugin](https://github.com/webpack-contrib/mini-css-extract-plugin)

    # install css plugin and loader 
    npm i mini-css-extract-plugin css-loader --save-dev
    # update webpack config  
    ## vim webpack.config.js
    // ...
    const MiniCssExtractPlugin = require('mini-css-extract-plugin');
    // ...
    module.exports = {
    	module: {
    		// ...
    		rules: [
    			// ...
    			{
    				test: /\.css$/,
    				use: [
    					MiniCssExtractPlugin.loader, 'css-loader'
    				]
    			}
    		]
    		// ...
    	},
    	// ...
    	plugins: [
    		// ...
    		new MiniCssExtractPlugin({
    			filename: '[name].css',
    			chunkFilename: '[id].css',
    		})
    		// ...
    	]
    	// ...
    };
    ## :wq
    # import css in entry point  
    ## vim src/index.js
    // ...
    import from './main.css'
    // ...
    ## :wq

## Dev Server

    # install dev server
    npm i webpack-dev-server --save-dev  
    # update package.json 
    // ...
    "script": {
    
    	"start": "webpack-dev-server --mode development --open --config webpack.config.js"
    }
    // ...