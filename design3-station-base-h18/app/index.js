import React from 'react';
import { render } from 'react-dom';
import { AppContainer } from 'react-hot-loader';
import { configureStore, history } from './store/configureStore';
import Root from './containers/Root';
import insertCss from 'insert-css';
import css from '../node_modules/re-bulma/build/css';

try {
    if (typeof document !== 'undefined' || document !== null) {
        insertCss(css, { prepend: true });
    }
} catch (e) {
    throw(e);
}

const store = configureStore();

render(
  <AppContainer>
    <Root store={store} history={history} />
  </AppContainer>,
  document.getElementById('root')
);

if (module.hot) {
    module.hot.accept('./containers/Root', () => {
        const newConfigureStore = require('./store/configureStore');
        const newStore = newConfigureStore.configureStore();
        const newHistory = newConfigureStore.history;
        const NewRoot = require('./containers/Root').default;
        render(
        <AppContainer>
            <NewRoot store={newStore} history={newHistory} />
        </AppContainer>,
        document.getElementById('root')
    );
    });
}
