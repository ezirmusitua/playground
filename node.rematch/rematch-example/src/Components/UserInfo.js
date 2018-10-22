import React, { Component } from 'react';
import { connect } from 'react-redux';


class UserInfo extends Component {
  render() {
    const {props: {user: {name, todoCount, score}}} = this;
    return (<section className="user-info">
      <h3 className="name">{name}</h3>
      <p className="todo-count">Total todo count: <b>{todoCount}</b></p>
      <p className="score">Total score: <b>{score}</b></p>
    </section>);
  }
}

const mapState = (state) => ({user: state.user});
const mapDispatch = () => ({});

export default connect(mapState, mapDispatch)(UserInfo);
