export const AppComponent = {
  bindings: {},
  controllerAs: 'vm',
  template: `
  <div> Hello World {{vm.env}}</div>
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