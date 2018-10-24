export function autoLoggerEnhancer() {
  /**
   * author: 艾特老干部
   * link://juejin.im/post/5a4874096fb9a044fa1a34c7
   **/
  return createStore => (reducer, initialState, enhancer) => {
    const store = createStore(reducer, initialState, enhancer);

    function dispatch(action) {
      console.info(`${initialState.version} - dispatch an action: ${JSON.stringify(action)}`);
      const res = store.dispatch(action);
      const newState = store.getState();
      console.info(`${initialState.version} - current state: ${JSON.stringify(newState)}`);
      return res;
    }

    return {...store, dispatch};
  };
}
