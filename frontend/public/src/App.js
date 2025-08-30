import React, { useState } from 'react';
import { FILTERS, basicScan } from './components/Filters';
import { ULTRA_FILTERS, ultraScan } from './components/UltraFilters';
// import { PRO_FILTERS, proScan } from './components/ProFilters'; // Uncomment when ready

import TrafficTable from './components/TrafficTable';
import RiskChart from './components/RiskChart';

function App() {
  const [mode, setMode] = useState('basic');
  const [logs, setLogs] = useState([]);
  const [filteredLogs, setFilteredLogs] = useState([]);

  // Example function to simulate log input
  const addLogEntry = (url) => {
    const newLogs = [...logs, { url }];
    setLogs(newLogs);
    applyScan(newLogs, mode);
  };

  const applyScan = (logData, selectedMode) => {
    let results;
    switch (selectedMode) {
      case 'basic':
        results = basicScan(logData);
        break;
      case 'ultra':
        results = ultraScan(logData);
        break;
      case 'pro':
        // results = proScan(logData); // Uncomment when ProFilters ready
        results = logData; // Placeholder
        break;
      default:
        results = logData;
    }
    setFilteredLogs(results);
  };

  const handleModeChange = (e) => {
    const newMode = e.target.value;
    setMode(newMode);
    applyScan(logs, newMode);
  };

  return (
    <div className="app-container">
      <h1>Ultra Privacy Scan</h1>

      <div className="mode-selector">
        <label>
          <input
            type="radio"
            value="basic"
            checked={mode === 'basic'}
            onChange={handleModeChange}
          />
          Basic
        </label>
        <label>
          <input
            type="radio"
            value="ultra"
            checked={mode === 'ultra'}
            onChange={handleModeChange}
          />
          Ultra
        </label>
        <label>
          <input
            type="radio"
            value="pro"
            checked={mode === 'pro'}
            onChange={handleModeChange}
          />
          Pro (coming soon)
        </label>
      </div>

      <div className="scan-input">
        <button onClick={() => addLogEntry(prompt("Enter URL to scan:"))}>
          Add Log Entry
        </button>
      </div>

      <div className="results">
        <RiskChart logs={filteredLogs} />
        <TrafficTable logs={filteredLogs} />
      </div>
    </div>
  );
}

export default App;

