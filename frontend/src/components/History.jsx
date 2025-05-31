import React, { useEffect, useState } from 'react';

function History() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/weather/history')
      .then(res => res.json())
      .then(data => {
        setHistory(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Erro ao carregar histórico:', err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Carregando histórico...</div>;

  if (history.length === 0) return <div>Nenhum histórico encontrado.</div>;

  return (
    <div className="history-container">
      <h2>Histórico de Consultas</h2>
      <table>
        <thead>
          <tr>
            <th>Cidade</th>
            <th>Data/Hora</th>
            <th>Temperatura (ºC)</th>
            <th>Humidade (%)</th>
            <th>Precipitação (mm)</th>
            <th>Sugestão Agrícola</th>
          </tr>
        </thead>
        <tbody>
          {history.map((entry, index) => (
            <tr key={index}>
              <td>{entry.city}</td>
              <td>{new Date(entry.timestamp).toLocaleString()}</td>
              <td>{entry.weather.temperature}</td>
              <td>{entry.weather.humidity}</td>
              <td>{entry.weather.precipitation ?? '0'}</td>
              <td>{entry.suggestion}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default History;
