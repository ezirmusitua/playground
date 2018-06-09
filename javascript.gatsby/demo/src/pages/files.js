import React from 'react'

export default class FileListPage extends React.Component {
  constructor() {
    super()
  }

  render() {
    const {props: {data: {allFile: {edges}}}} = this
    return (<div>
      <h1>My Site's Files</h1>
      <table>
        <thead>
        <tr>
          <th>relativePath</th>
          <th>prettySize</th>
          <th>extension</th>
          <th>birthTime</th>
        </tr>
        </thead>
        <tbody>
        {edges.map(({node}, index) =>
          <tr key={index}>
            <td>
              {node.relativePath}
            </td>
            <td>
              {node.prettySize}
            </td>
            <td>
              {node.extension}
            </td>
            <td>
              {node.birthTime}
            </td>
          </tr>
        )}
        </tbody>
      </table>
    </div>)
  }
}

export const query = graphql`
    query MyFilesQuery {
        allFile {
            edges {
                node {
                    relativePath
                    prettySize
                    extension
                    birthTime(fromNow: true)
                }
            }
        }
    }
`
