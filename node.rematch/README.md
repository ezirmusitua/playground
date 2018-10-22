## Rematch Example  
Introduction to rematch - the best **Redux** practices without the boilerplate  

### Getting Started  
1. what is redux: state management library for react  
2. what is rematch: the redux best practices without the boilerplate  
3. why rematch: redux is to complicated  

How to use rematch  

use `model` object to define state, actions and reducers  
```js
export const state1 = {
  state: 0, // initial state
  reducers: {
    // handle state changes with pure functions
    doSomething(state, payload) {
      return 'something'
    }
  },
  effects: {
    // handle state changes with impure functions.
    // use async/await for async actions
    async doSomethingAsync(payload, rootState) {
      return 'something'
    }
  }
};
```

use `init` from `@rematch/core` to setup a store simply
```js
import {init} from '@rematch/core'
import models from './models'
const options = {models}
const store = init(options)
```

use store in View in redux way  
```js
import React from 'react'
import {connect, Provider} from 'react-redux'
import store from './store'

const mapState = (state) => ({prop1: state.state1})
const mapDispatch = (dispatch) => ({
  doSomething: dispatch.state1.doSomething(),
  doSomethingAsync: dispatch.state1.doSomethingAsync(),
})

const Component1 = connect(mapState, mapDispatch)(props => <div>{props.prop1}</div>)

export default props => <Provider store={store}><Component1 /></Provider>
```
