import React, {Provider} from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import { ConnectedRouter, syncHistoryWithStore, routerReducer } from 'react-router-redux';

const SPAPage = document.getElementById('main');

if (SPAPage) {
    ReactDOM.render(
        <h1>Test case</h1>,
        SPAPage,
    );
}
