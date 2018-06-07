import template from '../templates/todo.html'

export const TodoView = {
  selector: 'todoView',
  bindings: {todo: '<'},
  template,
  controllerAs: 'vm',
  controller: class {
    constructor($state) {
      console.log('Page: Todo View')
      this.$onInit = function $onInit() {
        console.log(this.todo)
      }
      this.todoId = $state.params.todoId
    }
  }
}