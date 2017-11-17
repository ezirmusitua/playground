const express = require('express');
const graphql = require('graphql').graphql;
const bodyParser = require('body-parser');
const cors = require('cors');

const {DemoSchema} = require('./schema');

// === constants
const PORT = 3002;
const HOST = '127.0.0.1';

// === express app
const app = express();

// === middlewares
app.use(bodyParser.text({ type: 'application/graphql' }));
app.use(cors());

// === routes
app.post('/graphql', (req, res) => {
    console.log(req.body);
    graphql(DemoSchema, req.body).then((query) => {
        console.log('query in: ', query);
        res.send(JSON.stringify(query, null, null));
    });
});

// === error handler
app.use((err, req, res, next) => {
    console.error(err);
});

// === start application
app.listen(PORT, HOST, () => {
    console.log('GraphQL Server is listening at http://%s:%s', HOST, PORT);
});