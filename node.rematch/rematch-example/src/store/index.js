import { init } from '@rematch/core';
import createLoadingPlugin from '@rematch/loading';
import createRematchPersist from '@rematch/persist';
import createUpdatedPlugin from '@rematch/updated';
import models, { getTodosActionName } from '../models/index';
import { TODO_MODEL } from '../models/todos';
import { USER_MODEL } from '../models/user';
// import { doNothingMiddleware } from './middlewares';
// import { autoLoggerEnhancer } from './enhancers';
import { createMyRematchPlugin } from './plugins';


export const store = init({
  name: 'TodoApp',
  models,
  plugins: [
    createLoadingPlugin({
      whitelist: [
        getTodosActionName('createTodo'),
        getTodosActionName('markDone')
      ]
    }),
    createRematchPersist({
      whitelist: [TODO_MODEL, USER_MODEL],
      throttle: 1000,
      version: 1
    }),
    createUpdatedPlugin(),
    createMyRematchPlugin({name: 'UserCustomPlugin'})
  ],
  redux: {
    initialState: {
      version: process.env.VERSION || '0.0.1'
    },
    // middlewares: [doNothingMiddleware],
    middlewares: [],
    // enhancers: [autoLoggerEnhancer()]
    enhancers: []
  }
});
