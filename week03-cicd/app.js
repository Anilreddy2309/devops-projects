const express = require('express');
const app = express();

// Health check endpoint
// Kubernetes and load balancers ping this to know if your app is alive
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Simple API endpoint
app.get('/items', (req, res) => {
  res.json([
    { id: 1, name: 'laptop' },
    { id: 2, name: 'keyboard' },
    { id: 3, name: 'monitor' }
  ]);
});

app.listen(3000, () => {
  console.log('API running on port 3000');
});
