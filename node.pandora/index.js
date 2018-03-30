const express = require('express');

const app = express();

app.get('/', (__req, res) => {
  res.send('GET requests HOME')
});


app.listen(3000, '0.0.0.0');