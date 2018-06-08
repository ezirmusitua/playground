import template from '../templates/todos.html'

export const TodoList = {
  selector: 'todoList',
  bindings: {},
  controllerAs: 'vm',
  template,
  controller: class {
    constructor($transitions) {
      console.log('Page: Todo List')
      $transitions.onSuccess({to: 'todo'}, function (trans) {
        console.log(trans.from(), ' -> ', trans.to())
      })
    }
  }
}