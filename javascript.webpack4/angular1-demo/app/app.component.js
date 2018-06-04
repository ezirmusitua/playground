export const AppComponent = {
  bindings: {},
  controllerAs: 'vm',
  template: `
  <div id="app">
    <h2>Demo TODO App[{{vm.env}}] Implemented By Angular1.7 And Bundled By Webpack4</h2>
    <div ui-view></div> 
    <demo-button name="jferroal"></demo-button>
  </div>
  `,
  controller: class AppCtrl {
    constructor(Config) {
      // Object.assign(this)
      const vm = this
      console.log('Hello World: ', Config.env)
      vm.env = Config.env
    }
  }
}