// backend/server.js
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const axios = require('axios');
const cors = require('cors');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, { cors: { origin: '*' } });

app.use(cors());
app.use(express.json());

let trafficLog = [];

// Scan URL endpoint
app.post('/scan', async (req, res) => {
  const { url } = req.body;
  try {
    const response = await axios.get(url);
    const trackers = detectTrackers(response.headers, response.data);
    const riskScore = calculateRisk(trackers);

    const record = { url, trackers, riskScore, timestamp: new Date() };
    trafficLog.push(record);

    io.emit('new-traffic', record);
    res.json(record);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// History endpoint
app.get('/history', (req, res) => res.json(trafficLog));

// Basic tracker detection
function detectTrackers(headers, body) {
  const trackerList = ['google-analytics', 'facebook', 'mixpanel'];
  return trackerList.filter(t => body.includes(t) || (headers['set-cookie'] && headers['set-cookie'].join('').includes(t)));
}

// Simple risk scoring
function calculateRisk(trackers) {
  return Math.min(100, trackers.length * 33);
}

server.listen(4000, () => console.log('Backend running on port 4000'));
