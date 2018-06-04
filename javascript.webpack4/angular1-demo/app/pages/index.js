import angular from 'angular'
import {TodoView} from './todo'
import {TodoList} from './todos'

export const todoPage = angular.module('todo.page', []).
  component(TodoView.selector, TodoView).
  component(TodoList.selector, TodoList).name