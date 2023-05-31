const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());

app.get('/proxy', async (req, res) => {
  const fetch = await import('node-fetch').then(module => module.default);
  const url = req.query.url;
  const response = await fetch(url);
  const data = await response.json();
  res.json(data);
});

app.listen(3000, () => {
  console.log('Proxy server listening on port 3000');
});
