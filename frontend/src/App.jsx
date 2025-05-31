import React, { useState, useEffect } from "react";
import UserPopup from "./components/UserPopup.jsx";
import CityInput from "./components/CityInput.jsx";
import WeatherDisplay from "./components/WeatherDisplay.jsx";
import Suggestions from "./components/Suggestions.jsx";
import History from "./components/History.jsx";
import Dashboard from "./components/Dashboard.jsx";
import websocketService from "./services/websocket.js";


export default function App() {
  const [user, setUser] = useState(null);
  const [city, setCity] = useState("");
  const [weatherData, setWeatherData] = useState(null);
  const [suggestions, setSuggestions] = useState([]);
  const [history, setHistory] = useState([]);

  const [ws, setWs] = useState(null);

  useEffect(() => {
  if (user) {
    websocketService.connect();
    websocketService.addListener(onMessage);

    setWs(websocketService.ws);

    return () => {
      websocketService.removeListener(onMessage);
      if (websocketService.ws) {
        websocketService.ws.close();
      }
    };
  }
}, [user]);


  const onMessage = (data) => {
    if (data.weather) {
      setWeatherData(data.weather);
    }
    if (data.suggestions) {
      setSuggestions(data.suggestions);
    }
  };

  const sendCity = (cityName) => {
    setCity(cityName);
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ city: cityName, user: user }));
      // Atualizar histórico localmente para demo
      fetch("/api/weather/history")
        .then((res) => res.json())
        .then(setHistory)
        .catch(console.error);
    }
  };

  if (!user) {
    return <UserPopup onSubmit={setUser} />;
  }

  return (
    <div className="app-container">
      <h1>Agrigest - Gestão Agrícola Inteligente</h1>
      <CityInput onSendCity={sendCity} />
      {weatherData && <WeatherDisplay data={weatherData} />}
      {suggestions.length > 0 && <Suggestions suggestions={suggestions} />}
      <History history={history} />
      <Dashboard history={history} />
    </div>
  );
}
