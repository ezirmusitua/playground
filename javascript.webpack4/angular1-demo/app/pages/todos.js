import template from '../templates/todos.html'

export const TodoList = {
  selector: 'todoList',
  bindings: {},
  controllerAs: 'vm',
  template,
  controller: class {
    constructor() {
      console.log('Page: Todo List')
    }
  }
}