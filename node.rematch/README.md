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

[Here]() is a complete example that using rematch in react app.  
The example is a simple todo-app, in the left side, user can add new todo item and mark item done.  
In the right side, user can see how many todos remained, and his/her score(add +1, done +2).   

As described, this app contain 2 model:  
1. todos model - use to store the todo items info and actions  
2. user model - use to store user info  

```js
export const user = {
  name: 'user',
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
```  

For example, user model's state is an object, it store user's name, remained todo count and score, we defined 2 reducers use to change state, and 2 effects use to update data in backend(use timeout to mock).  

Rest of the example is just like what we do before.  

### The `redux` option in `init` method  
In my opinion, the `redux` option in `init` function is a way to customize the store creation.  
The detail of `redux` option describe below:  
```js
{
  redux: {
    // initial state in store
    initialState?: any,
    // reducer functions
    reducers: ModelReducers,
    // enhancers
    enhancers: Redux.StoreEnhancer<any>[],
    // middlwares
    middlewares: Middleware[],
    // a way use to set hook in root reducer, hook would return next state
    rootReducers?: RootReducers,
    // overwrite combineReducers
    combineReducers?: (reducers: Redux.ReducersMapObject) => Redux.Reducer<any, Action>,
    // overwrite createStore
    createStore?: Redux.StoreCreator,
    // devtool options
    devtoolOptions?: DevtoolOptions,
  }
}
```  
In most case, you do not need to set it unless you want to create plugin or middleware.  

[Here]() is the example, in the example, we set redux option:  
1. initial state version  
2. a do nothing middleware(just prove that middleware has been called)   
3. a enhancer use to log automatically  

**middleware and enhancer write with the same way we do in react-redux**  

### How to use and create plugin  
In rematch, everything is is `plugin`(dispatch, effects, ...), developer can use or create plugin.  

#### Supplied plugins   
rematch has supply 7 plugin, they are:  

1. [Rematch Select](https://github.com/rematch/rematch/tree/master/plugins/select) - add memorized state selection
2. [Rematch Loading](https://github.com/rematch/rematch/tree/master/plugins/loading) - add automated loading indicators for effects
3. [Rematch Persist](https://github.com/rematch/rematch/tree/master/plugins/persist) - [Redux-Persist](https://github.com/rt2zz/redux-persist)
4. [Rematch Updated](https://github.com/rematch/rematch/tree/master/plugins/updated) - optimizing effects(debounce and throttle)
5. [React Navigation](https://github.com/rematch/rematch/tree/master/plugins/react-navigation) - [React Navigation](https://reactnavigation.org/) 
6. [Rematch Immer](https://github.com/rematch/rematch/tree/master/plugins/immer) - [Immer](https://github.com/mweststrate/immer)  
7. [Rematch typed-state](https://github.com/rematch/rematch/tree/master/plugins/typed-state) - runtime type-checking state   

[Here] is the example show how to use `persist`, `loading` and `updated` plugin  

**remember to check the version of plugin**   

#### Create plugin  
A plugin object should contain:  
```js
const plugin = {
  config: {
    // same as the options of `init` method
  },
  exposed: {
    // key-value pair that assigned the communicable plugin
  },
  onModel: (model) => {
   // called while model created 
  },
  middleware: (store) => {
    // (store: Model) => (next: Dispatch) => (action: Action): NextState, use to customize middleware  
  },
  onStoreCreated: (store) => {
    // called while store created
  }
}
``` 
[Here]() is an example show how to write a plugin, this plugin use to throttle action.  
While model created, it will wrap model's action, in the wrapped action, if the action called within throttle time, it won't act again, otherwise, action will execute and plugin will update the model action's last called time.  
It is just like updated plugin, but add throttle.  


### References  
* [Rematch Handbook](https://rematch.gitbook.io/handbook/)  
* [Redux Enhancer](https://juejin.im/post/5a4874096fb9a044fa1a34c7)  
* [react-redux tutorial](https://github.com/reduxjs/react-redux/blob/master/docs/introduction/basic-tutorial.md)  






