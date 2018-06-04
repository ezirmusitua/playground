import angular from 'angular'
import {demoButton} from './demo-button'

export const todoDirective = angular.module('todo.directive', []).directive(demoButton.name, demoButton).name