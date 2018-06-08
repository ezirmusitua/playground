import React from 'react'
import Link from 'gatsby-link'
import Header from './Header'
import {MetaDataQuery} from '../resources/metadata'

class ListLink extends React.Component {
  constructor() {
    super()
  }

  render() {
    const {props} = this
    return (<li style={{display: `inline-block`, marginRight: `1rem`}}>
      <Link to={props.to}>
        {props.children}
      </Link>
    </li>)
  }
}

export default class Navigation extends React.Component {
  constructor() {
    super()
  }

  render() {
    console.log(this.props.data, this.props)
    return (<div style={{margin: `0 auto`, position: `relative`}}>
      <Header siteTitle={'123'} style={{marginBottom: `1.5rem`}}/>
      <ul style={{listStyle: `none`, position: `absolute`, top: `30px`, right: `30px`}}>
        {this.props.links.map((l) => <ListLink to={l.to} key={l.name}>{l.name}</ListLink>)}
      </ul>
    </div>)
  }
}

export const query = graphql`
  query SiteTitleQuery {
    site {
      siteMetadata {
        title
      }
    }
  }
`
