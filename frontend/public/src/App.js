import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import RiskChart from './components/RiskChart';
import TrafficTable from './components/TrafficTable';

const socket = io('http://localhost:4000');

function App() {
  const [traffic, setTraffic] = useState([]);

  useEffect(() => {
    socket.on('new-traffic', data => setTraffic(prev => [...prev, data]));
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>Ultra Digital Privacy Dashboard</h2>
      <div style={{ display: 'flex', gap: '20px', marginBottom: '20px' }}>
        <div>Active Scans: {traffic.length}</div>
        <div>High Risk: {traffic.filter(t => t.riskScore > 60).length}</div>
      </div>

      <RiskChart traffic={traffic} />
      <TrafficTable traffic={traffic} />
    </div>
  );
}

export default App;
