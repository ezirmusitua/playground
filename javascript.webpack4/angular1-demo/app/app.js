import {AppComponent} from './app.component'
import angular from 'angular'
import AngularAria from 'angular-aria'
import AngularAnimate from 'angular-animate'
import AngularMaterial from 'angular-material'

angular.module('angular-webpack4', [
  AngularAria,
  AngularAnimate,
  AngularMaterial
]).
  component('app', AppComponent).
  run(() => {
    console.log('Running')
  })
angular.element(document).ready(() => {
  angular.bootstrap(document, ['angular-webpack4'])
})