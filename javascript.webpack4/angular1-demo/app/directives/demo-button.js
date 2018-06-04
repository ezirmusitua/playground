export function demoButton() {
  return {
    restrict: 'E',
    scope: {name: '@'},
    template: '<md-button class="md-primary md-raised" aria-label="debug" ng-click="sayHi()">Click Me ~</md-button>',
    link(scope) {
      scope.sayHi = () => {
        alert(`Hi ${scope.name}`)
      }
    }
  }
}