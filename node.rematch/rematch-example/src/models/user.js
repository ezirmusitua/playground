export const USER_MODEL = 'user';
export const user = {
  name: USER_MODEL,
  state: {
    name: 'DemoUser',
    todoCount: 0,
    score: 0
  },
  reducers: {
    changeTodoCount: (state, {todoCount}) => {
      return Object.assign({}, {...state, todoCount: state.todoCount + todoCount});
    },
    changeScore: (state, {score}) => {
      return Object.assign({}, {...state, score: state.score + score});
    }
  },
  effects: {
    async updateTodoCount({todoCount}) {
      await new Promise(resolve => setTimeout(resolve, 500));
      this.changeTodoCount({todoCount});
    },
    async updateScore({score}) {
      await new Promise(resolve => setTimeout(resolve, 500));
      this.changeScore({score});
    }
  }
};
