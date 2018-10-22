import React from 'react';
import { connect, Provider } from 'react-redux';
import store from './store/index';

const mapState = state => ({count: state.count});

const mapDispatch = ({count: {increment, incrementAsync}}) => ({
  increment: () => increment(1),
  incrementAsync: () => incrementAsync(1)
});


const Count = connect(mapState, mapDispatch)(props => (
  <div style={{
    height: '100vh',
    width: '100vw',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center'
  }}>
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center'
    }}>
      <p style={{
        fontSize: '24px',
        marginBottom: '12px'
      }}>Current count is: <b>{props.count}</b></p>
      <button style={{
        width: '120px',
        height: '48px',
        border: 'none',
        backgroundColor: 'skyblue',
        marginTop: '12px',
        borderRadius: '12px',
        color: 'white',
        cursor: 'pointer'
      }} onClick={props.increment}>increment
      </button>
      <button style={{
        width: '120px',
        height: '48px',
        border: 'none',
        backgroundColor: 'skyblue',
        marginTop: '12px',
        borderRadius: '12px',
        color: 'white',
        cursor: 'pointer'
      }} onClick={props.incrementAsync}>incrementAsync
      </button>
    </div>
  </div>)
);


export default props => (<Provider store={store}>
  <Count/>
</Provider>);


