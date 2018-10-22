import React, { Component } from 'react';
import TodoList from './TodoList';
import UserInfo from './UserInfo';


export default class HomeScreen extends Component {
  render() {
    return (<article style={{
      height: '100%',
      maxWidth: '1440px',
      margin: '0 auto',
      display: 'flex'
    }}>
      <TodoList/>
      <UserInfo/>
    </article>);
  }
}
