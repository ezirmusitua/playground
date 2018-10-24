export function doNothingMiddleware({dispatch, getState}) {
  console.info(`Do nothing middleware created`);
  return next => action => {
    console.info(`Do nothing middleware called`);
    if (typeof action === 'function') {
      return action(dispatch, getState);
    }
    return next(action);
  };
}
