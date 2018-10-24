export const TODO_MODEL = 'todos';
export const todos = {
  name: TODO_MODEL,
  state: {
    items: {},
    itemIds: [],
    currentId: 0,
    newTodoContent: ''
  }, // initial state
  reducers: {
    // handle state changes with pure functions
    addTodo(state) {
      return Object.assign(state, {
        items: {
          ...state.items,
          [state.currentId]: {
            id: state.currentId,
            content: state.newTodoContent,
            done: false
          }
        },
        currentId: state.currentId + 1,
        newTodoContent: '',
        itemIds: [...state.itemIds, state.currentId]
      });
    },
    removeTodo(state, {id}) {
      const items = Object.entries(state.items)
                          .reduce((res, [_id, todo]) => {
                            if (parseInt(_id, 10) === id) {
                              todo.done = true;
                            }
                            res[_id] = todo;
                            return res;
                          }, {});
      console.log(items);
      const itemIds = Object.keys(items);
      return Object.assign(state, {...state, items, itemIds});
    },
    changeNewTodoContent(state, {content}) {
      return Object.assign({}, {...state, newTodoContent: content});
    }
  },
  effects: {
    // handle state changes with impure functions.
    // use async/await for async actions
    async createTodo() {
      await new Promise(resolve => setTimeout(resolve, 1000));
      this.addTodo();
    },
    async markDone({id}) {
      await new Promise(resolve => setTimeout(resolve, 1000));
      this.removeTodo({id});
    }
  }
};
