import React from 'react'

import Helmet from 'react-helmet'
import Navigation from '../components/Navigation'
import './index.scss'

export default class Layout extends React.Component {
  constructor() {
    super()
  }
  render() {
    const {props:{ data, children }} = this
    return (<div>
    <Helmet title={data.site.siteMetadata.title}
            meta={[
              {name: 'description', content: 'Sample'},
              {name: 'keywords', content: 'sample, something'},
            ]}/>
    <Navigation siteTitle={data.site.siteMetadata.title} links={[{
      to: '/page-2', name: 'Page 2'
    }, {
      to: '/counter', name: 'Counter'
    }, {
      to: '/typography-demo', name: 'Typography Demo'
    }, {
      to: '/about', name: 'About'
    }]}/>
    <div style={{
      margin: '0 auto',
      maxWidth: 960,
      padding: '0px 1.0875rem 1.45rem',
      paddingTop: 0,
    }}>{children()}</div>
  </div>)
  }
}

export const query = graphql`
  query LayoutSiteTitleQuery {
    site {
      siteMetadata {
        title
      }
    }
  }
`