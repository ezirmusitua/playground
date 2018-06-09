import React from 'react'

export default class PostsPage extends React.Component {
  constructor() {
    super()
  }

  render() {
    const {props: {data: {allMarkdownRemark: {totalCount, edges: posts}}}} = this
    return (
      <div>
        <h1 style={{display: 'inline-block', borderBottom: '1px solid'}}>
          Amazing Pandas Eating Things
        </h1>
        <h4>{totalCount} Posts</h4>
        {posts.map(({node}) => (
          <div key={node.id}>
            <h3>
              {node.frontmatter.title}{" "}
              <span color="#BBB">— {node.frontmatter.date}</span>
            </h3>
            <p>{node.excerpt}</p>
          </div>
        ))}
      </div>)
  }
}

export const query = graphql`
    query BlogPostsQuery {
        allMarkdownRemark(sort: {fields: [frontmatter___date], order: DESC}) {
            totalCount
            edges {
                node {
                    id
                    frontmatter {
                        title
                        date(formatString: "DD MMMM, YYYY")
                    }
                    excerpt
                }
            }
        }
    }
`