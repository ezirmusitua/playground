const express = require('express');

const PORT = 3002;
const HOST = '127.0.0.1';
const app = express();

app.post('/graphql', (req, res) => {
    res.send('hello');
});

app.listen(PORT, HOST, () => {
    console.log('GraphQL Server is listening at http://%s:%s', HOST, PORT);
});