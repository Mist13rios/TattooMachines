import React, {Provider} from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import { ConnectedRouter, syncHistoryWithStore, routerReducer } from 'react-router-redux';

import { Landing } from './containers'

const SPAPage = document.getElementById('main');


if (SPAPage) {
    ReactDOM.render(
        <Landing />,
        SPAPage,
    );
}
