import { todos, TODO_MODEL } from './todos';
import { user, USER_MODEL } from './user';

export function getModelActionName(model, action) {
  return `${model}/${action}`;
}

export function getTodosActionName(action) {
  return getModelActionName(TODO_MODEL, action);
}

export function getUserActionName(action) {
  return getModelActionName(USER_MODEL, action);
}

export default {todos, user};
