import React, { Component } from 'react';
import { connect } from 'react-redux';


class TodoItem extends Component {
  render() {
    const {props: {todo: {id, content}, markDone}} = this;
    return (<section className="todo">
      <p style={{width: '80%'}}>{content}</p>
      <span style={{
        cursor: 'pointer',
        fontSize: '16px'
      }} onClick={() => markDone({id})}>{String.fromCodePoint(0x2714)}</span>
    </section>);
  }
}

const mapState = () => ({});
const mapDispatch = ({todos: {markDone}, user: {updateTodoCount, updateScore}}) => ({
  async markDone({id}) {
    await markDone({id});
    await Promise.all([
      updateTodoCount({todoCount: -1}),
      updateScore({score: 2})
    ]);
  }
});

export default connect(mapState, mapDispatch)(TodoItem);
