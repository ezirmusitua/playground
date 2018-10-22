import { init } from '@rematch/core';
import models from './models';

export default init({
  name: 'TodoApp',
  models,
  plugin: [],
  redux: {}
});
