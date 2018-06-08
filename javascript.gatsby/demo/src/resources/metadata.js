export class MetaDataQuery {
  static get siteTitle() {
    return graphql`
        query siteTitleQuery {
            site {
                siteMetadata {
                    title
                }
            }
        }`
  }
}