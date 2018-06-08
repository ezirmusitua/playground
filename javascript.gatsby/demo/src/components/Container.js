import React from "react"

export default class Container extends React.Component {
  constructor() {
    super()
  }

  render() {
    return (
      <div style={{margin: "3rem auto", maxWidth: 600}}>{this.props.children}</div>
    )
  }
};