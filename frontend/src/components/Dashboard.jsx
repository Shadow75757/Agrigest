import React, { useEffect, useState } from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function Dashboard() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetch('/api/weather/history')
      .then(res => res.json())
      .then(data => setHistory(data))
      .catch(console.error);
  }, []);

  // Formatar dados para gráfico de temperatura e humidade ao longo do tempo
  const formattedData = history.map(entry => ({
    timestamp: new Date(entry.timestamp).toLocaleString(),
    temperature: entry.weather.temperature,
    humidity: entry.weather.humidity,
  }));

  return (
    <div className="dashboard-container">
      <h2>Dashboard Climático</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={formattedData}>
          <CartesianGrid stroke="#ccc" />
          <XAxis dataKey="timestamp" tick={{ fontSize: 10 }} />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="temperature" stroke="#ff7300" name="Temperatura (ºC)" />
          <Line type="monotone" dataKey="humidity" stroke="#387908" name="Humidade (%)" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default Dashboard;
