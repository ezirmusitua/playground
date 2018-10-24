export function createMyRematchPlugin(config) {
  const myPluginModel = {
    name: config.name || 'MyRematchPlugin',
    throttleTime: config.throttleTime || 500,
    state: {},
    reducers: {
      onUpdate: (state, payload) => ({
        ...state,
        [payload.name]: {
          ...state[payload.name],
          [payload.action]: Date.now()
        }
      })
    }
  };
  return {
    config: {...config, models: {myPluginModel}},
    exposed: {
      loading: {}
    },
    onModel(model) {
      console.info(`[CreateMyRematchPlugin]: ${model.name} created`);
      const name = model.name;
      if ([myPluginModel.name, 'loading', 'updated'].includes(name)) return;
      const modelActions = this.dispatch[name];
      myPluginModel.state[name] = {};
      for (const action of Object.keys(modelActions)) {
        const fn = this.dispatch[name][action];
        this.dispatch[name][action] = async props => {
          const targetModelStatus = this.storeGetState()[myPluginModel.name][name];
          if (!targetModelStatus[action] || Date.now() - targetModelStatus[action] > myPluginModel.state.throttleTime) {
            await fn(props);
            this.dispatch[myPluginModel.name].onUpdate({name, action});
          } else {
            console.warn(`[CreateMyRematchPlugin]: ${name}/${action} Throttled`);
          }
        };
      }
    },
    middleware(store) {
      return (next) => {
        return (action) => {
          console.info(`[CreateMyRematchPlugin] Middleware`);
          return next(action);
        };
      };
    },
    onStoreCreated(store) {
      console.info('[CreateMyRematchPlugin]: store created: ', store);
    }
  };

}
