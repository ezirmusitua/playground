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

### Use rematch in detail  
A react-redux [example](https://codesandbox.io/s/9on71rvnyo) from [react-redux repo](https://github.com/reduxjs/react-redux/blob/master/docs/introduction/basic-tutorial.md)  

As can see, to use react-redux, developer should:  

1. create reducers(state and actions dispatcher)   
2. define action types accord to reducers  
3. implement action types  
4. create store  
5. use Provider Component to wrap App Component(and supply store props)  

In above section, use redux with rematch is quite simpler:  

1. define models(state, reducers, effects, ...)  
2. use init to with models to create store  
3. use Provider Component to wrap App Component(and supply store props)  

We do not need to define Action Types, cause in rematch, reducers and effects do it for us.  

Following is the detail about what can we define in model.  
```js
import {init} from '@rematch/core'  

const model = {
  name: 'nameOfThisModel',
  // equal to initialState in creating redux while using react-redux
  state: 'state',   
  // reducers are the pure functions use to change model state, is some kind of redux action 
  reducers: {
    doSomething: (state, payload) => {
      // do something
      return state
    }
    // ...
  },
  // effects are the functions that can change not only current models' state
  // usually, it can be the async function that use to react with backend  
  effects: {
    doSomethingWithEffect: (payload, rootState) => {
      // do something has side effect
    },
    async doSomethingWithEffectAsync: (payload, rootState) => {
      // do something has side effect async
    },
    // ...
  }
}
```  

Following is the detail about what options can pass to init function.
```js
import {init} from '@rematch/core'
import models from './models'

export default init({
  name: 'nameOfStore',
  // model we defined before
  models,
  // Plugin would be introduce in following section
  plugin: [],
  // redux would be introduce in follwoing section
  redux: {}
})
```  

In the end we will show how to use it in react view, it is similar to use in react-redux, just simply the `connect` with destructing:  
```js
import React from 'react'
import {connect} from 'react-redux'
import store from './store'  

const mapStateToProps = (state) => ({count: state.count})
// NOTE: can use dispatch with destructing
const mapDispatchWithDestructure = ({count: {increment}}) => ({increment})
const Counter = connect(mapState, mapDispatch)(props => <div>{props.count}</div>)

export default props=> <Provider store={store}>Counter</Provider>
```
