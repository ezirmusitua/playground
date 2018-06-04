export const AppComponent = {
  bindings: {},
  template: `
  <div> Hello World </div>
  `,
  controller: class AppCtrl {
    constructor() {
      // Object.assign(this)
      console.log('Hello World')
    }
  }
}