import angular from 'angular'

const env = process.env.NODE_ENV
const region = process.env.REGION
export const config = angular.module('todo.config', []).constant('Config', class {
  static get env() {
    return env
  }

  static get region() {
    return region
  }
}).name