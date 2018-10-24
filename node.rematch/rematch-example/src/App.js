import React from 'react';
import { Provider } from 'react-redux';
import { getPersistor } from '@rematch/persist';
import { PersistGate } from 'redux-persist/es/integration/react';
import HomeScreen from './Components/HomeScreen';
import { store } from './store/index';

const persistor = getPersistor();
export default () => (<PersistGate persistor={persistor}>
  <Provider store={store}>
    <HomeScreen/>
  </Provider>
</PersistGate>);


