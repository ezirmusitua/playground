import {AppComponent} from './app.component'
import angular from 'angular'
import AngularAria from 'angular-aria'
import AngularAnimate from 'angular-animate'
import AngularMaterial from 'angular-material'

import {todoService} from './services'

angular.module('angular-webpack4', [
  AngularAria,
  AngularAnimate,
  AngularMaterial,
  todoService
]).component('app', AppComponent).
  run(() => {
    console.log('App Running')
  })
angular.element(document).ready(() => {
  angular.bootstrap(document, ['angular-webpack4'])
})