import template from '../templates/todo.html'

export const TodoView = {
  selector: 'todoView',
  bindings: {},
  template,
  controllerAs: 'vm',
  controller: class {
    constructor($state) {
      console.log('Page: Todo View')
      Object.assign(this, $state)
      console.log(this, $state.params)
      this.todoId = $state.params.todoId
    }
  }
}