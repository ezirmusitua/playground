import 'animate.css/animate.css'
import 'angular-material/angular-material.scss'
import './app.scss'

import {AppComponent} from './app.component'
import angular from 'angular'
import AngularAria from 'angular-aria'
import AngularAnimate from 'angular-animate'
import AngularMaterial from 'angular-material'
import AngularUiRouter from 'angular-ui-router'

import {todoService} from './services'
import {todoPage} from './pages'
import {todoDirective} from './directives'

angular.module('angular-webpack4', [
  AngularAria,
  AngularAnimate,
  AngularMaterial,
  AngularUiRouter,
  todoService,
  todoPage,
  todoDirective
]).config(($locationProvider, $stateProvider, $urlRouterProvider) => {
  $locationProvider.html5Mode(true)
  $locationProvider.hashPrefix('!')
  $urlRouterProvider.otherwise('/')
  $stateProvider.state('todos', {
    url: '/',
    template: '<todo-list></todo-list>'
  }).state('todo', {
    url: '/todo/:todoId',
    template: '<todo-view></todo-view>'
  })
}).
  component('app', AppComponent).
  run(() => {
    console.log('App Running')
  })
angular.element(document).ready(() => {
  angular.bootstrap(document, ['angular-webpack4'])
})