import React from 'react'

export default class Post extends React.Component {
  constructor() {
    super()
  }

  render() {
    const {props: {data: {markdownRemark: post}}} = this
    return (<div>
      <h1>{post.frontmatter.title}</h1>
      <div dangerouslySetInnerHTML={{__html: post.html}}/>
    </div>)
  }
}
export const query = graphql`
    query BlogPostQuery($slug: String!) {
        markdownRemark(fields: { slug: { eq: $slug } }) {
            html
            frontmatter {
                title
            }
        }
    }
`