const express = require('express');
const os = require('os');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// Returns a fixed string
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Returns the hostname of the instance/container/pod
app.get('/gethostname', (req, res) => {
  console.log(os.hostname());
  res.send(os.hostname());
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);