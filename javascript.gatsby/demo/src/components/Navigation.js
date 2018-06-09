import React from 'react'
import Link from 'gatsby-link'
import Header from './Header'

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
    const {props: {siteTitle, links}} = this
    return (<div style={{margin: `0 auto`, position: `relative`}}>
      <Header title={siteTitle} style={{marginBottom: `1.5rem`}}/>
      <ul style={{listStyle: `none`, position: `absolute`, top: `30px`, right: `30px`}}>
        {links.map((l) => <ListLink to={l.to} key={l.name}>{l.name}</ListLink>)}
      </ul>
    </div>)
  }
}