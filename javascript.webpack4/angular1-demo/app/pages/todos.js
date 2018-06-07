import template from '../templates/todos.html'

export const TodoList = {
  selector: 'todoList',
  bindings: {},
  controllerAs: 'vm',
  template,
  controller: class {
    constructor($transitions) {
      console.log('Page: Todo List')
      console.log($transitions)
      $transitions.onStart({to: 'todos'}, function (trans) {
        console.log(trans)
      })
    }
  }
}