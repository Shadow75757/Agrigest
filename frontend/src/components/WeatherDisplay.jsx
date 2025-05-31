import React from "react";

export default function WeatherDisplay({ data }) {
  if (!data || !data.main) return null;

  const { temp, humidity } = data.main;
  const weatherDesc = data.weather[0]?.description || "";

  return (
    <div className="weather-display">
      <h2>Dados Meteorológicos</h2>
      <p>Temperatura: {temp} °C</p>
      <p>Humidade: {humidity} %</p>
      <p>Descrição: {weatherDesc}</p>
    </div>
  );
}
