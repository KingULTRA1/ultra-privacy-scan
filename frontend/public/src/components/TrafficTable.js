import React from 'react';

const TrafficTable = ({ traffic }) => (
  <div>
    <h3>Live Traffic Feed</h3>
    <table border="1" cellPadding="5">
      <thead>
        <tr><th>URL</th><th>Trackers</th><th>Risk</th></tr>
      </thead>
      <tbody>
        {traffic.map((t, i) => (
          <tr key={i}>
            <td>{t.url}</td>
            <td>{t.trackers.join(', ')}</td>
            <td>{t.riskScore}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

export default TrafficTable;
