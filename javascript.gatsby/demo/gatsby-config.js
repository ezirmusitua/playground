module.exports = {
  siteMetadata: {
    title: 'Gatsby Starter Demo',
    meta: [{
      name: 'description', content: 'Sample'
    }, {
      name: 'keywords', content: 'sample, something'
    }],
    navs: [{
      to: '/', name: 'Blog Post List'
    }, {
      to: '/counter', name: 'Counter'
    }, {
      to: '/typography-demo', name: 'Typography Demo'
    }, {
      to: '/about', name: 'About'
    }, {
      to: '/files', name: 'File List'
    }]
  },
  plugins: [
    {
      resolve: 'gatsby-plugin-react-helmet'
    },
    {
      resolve: `gatsby-plugin-typography`,
      options: {
        pathToConfigModule: `src/utils/typography.js`,
      }
    },
    {
      resolve: 'gatsby-plugin-sass'
    },
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        name: `src`,
        path: `${__dirname}/src/`
      }
    },
    {
      resolve: 'gatsby-transformer-remark'
    }
  ],
}
