import React from 'react'

import Helmet from 'react-helmet'
import Navigation from '../components/Navigation'
import './index.scss'

export default class Layout extends React.Component {
  constructor() {
    super()
  }

  render() {
    const {props: {data: {site: {siteMetadata: {title, navs, meta}}}, children}} = this
    return (<div>
      <Helmet title={title} meta={meta}/>
      <Navigation siteTitle={title} links={navs}/>
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
                title,
                meta {
                    name,
                    content
                },
                navs {
                    to,
                    name
                }
            }
        }
    }
`