import React from 'react'
import Link from 'gatsby-link'

export default class IndexPage extends React.Component {
  constructor() {
    super()
  }

  render() {
    const {props: {data: {allMarkdownRemark: {totalCount, edges: posts}}}} = this
    return (<div>
      <h1 style={{display: "inline-block", borderBottom: "1px solid"}}>
        Amazing Pandas Eating Things
      </h1>
      <h4>{totalCount} Posts</h4>
      {posts.map(({node}) =>
        <div key={node.id}>
          <Link to={node.fields.slug} style={{textDecoration: `none`, color: `inherit`}}>
            <h3>
              {node.frontmatter.title}{" "}
              <span style={{color: "#BBB"}}>— {node.frontmatter.date}</span>
            </h3>
            <p>
              {node.excerpt}
            </p>
          </Link>
        </div>
      )}
    </div>)
  }
}

export const query = graphql`
    query IndexQuery {
        allMarkdownRemark(sort: { fields: [frontmatter___date], order: DESC }) {
            totalCount
            edges {
                node {
                    id
                    frontmatter {
                        title
                        date(formatString: "DD MMMM, YYYY")
                    }
                    fields {
                        slug
                    }
                    excerpt
                }
            }
        }
    }
`