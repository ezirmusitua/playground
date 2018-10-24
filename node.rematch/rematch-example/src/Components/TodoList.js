import React, { Component } from 'react';
import { connect } from 'react-redux';
import TodoItem from './TodoItem';

function throttle(action, lastUpdated = 0, waiting = 10000) {
  if (Date.now() - lastUpdated > waiting) {
    action();
  }
  console.warn('!!!!!!!!!!Action Throttled!!!!!!!!!!');
}

class TodoList extends Component {
  render() {
    const {
      props: {
        todos,
        newTodoContent,
        changeNewTodoContent,
        createTodo,
        creating,
        lastUpdated
      }
    } = this;
    return (<section className="todos">
      <div style={{
        minHeight: '80px',
        display: 'flex',
        alignItems: 'flex-start',
        justifyContent: 'center',
        padding: '12px',
        marginBottom: '24px',
        flexDirection: 'column'
      }}>
        {Object.entries(todos)
               .filter(([, todo]) => !todo.done)
               .map(([id, todo]) => <TodoItem key={id} todo={todo}/>)}
        {!Object.entries(todos).length && <p>Nothing to do now !</p>}
      </div>
      <div style={{
        width: '100%',
        height: '32px',
        display: 'flex',
        justifyContent: 'space-between'
      }}>
        <input style={{
          marginRight: '12px',
          width: '80%',
          border: 'none',
          borderBottom: '1px solid grey',
          outline: 'none'
        }} value={newTodoContent} onChange={(e) => {
          changeNewTodoContent({content: e.target.value});
        }}/>
        <button style={{
          border: 'none',
          outline: 'none',
          borderRadius: '12px',
          backgroundColor: 'skyblue',
          cursor: 'pointer',
          lineHeight: '32px',
          color: 'white',
          padding: '0 24px',
          boxShadow: '0px 4px 8px 2px rgba(233, 233, 233, .8)'
        }} onClick={() => throttle(createTodo, lastUpdated)}>{creating ? 'creating' : 'create'}
        </button>
      </div>
    </section>);
  }
}

const mapState = (state) => {
  console.log(state);
  return {
    // loading state
    creating: state.loading.effects.todos.createTodo,
    newTodoContent: state.todos.newTodoContent,
    todos: state.todos.items,
    // updated state
    lastUpdated: state.updated.todos.createTodo
  };
};
const mapDispatch = ({todos: {createTodo, changeNewTodoContent}, user: {updateTodoCount, updateScore}}) => ({
  async createTodo() {
    console.info('createTodo Clicked');
    await createTodo();
    await Promise.all([
      updateTodoCount({todoCount: 1}),
      updateScore({score: 1})
    ]);
  },
  changeNewTodoContent
});

export default connect(mapState, mapDispatch)(TodoList);
