const express = require('express');
const graphql = require('graphql').graphql;
const bodyParser = require('body-parser');

const schema = require('./schema');

// === constants
const PORT = 3002;
const HOST = '127.0.0.1';

// === express app
const app = express();

// === middlewares
app.use(bodyParser.text({ type: 'application/graphql' }));

// === routes
app.post('/graphql', (req, res) => {
    graphql(schema, req.body).then((query) => {
        res.send(JSON.stringify(query, null, null));
    });
});

// === start application
app.listen(PORT, HOST, () => {
    console.log('GraphQL Server is listening at http://%s:%s', HOST, PORT);
});