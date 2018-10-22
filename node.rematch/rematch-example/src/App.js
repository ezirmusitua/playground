import React from 'react';
import { Provider } from 'react-redux';
import HomeScreen from './Components/HomeScreen';
import store from './store';

export default () => (<Provider store={store}>
  <HomeScreen/>
</Provider>);


