import React from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';

const RiskChart = ({ traffic }) => (
  <LineChart width={600} height={300} data={traffic}>
    <Line type="monotone" dataKey="riskScore" stroke="#ff0000" />
    <CartesianGrid stroke="#ccc" />
    <XAxis dataKey="timestamp" />
    <YAxis />
    <Tooltip />
  </LineChart>
);

export default RiskChart;
