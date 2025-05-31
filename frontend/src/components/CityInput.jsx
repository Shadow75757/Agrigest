import React, { useState } from "react";

export default function CityInput({ onSendCity }) {
  const [city, setCity] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (city.trim()) {
      onSendCity(city.trim());
      setCity("");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="city-input-form">
      <input
        type="text"
        placeholder="Introduza o nome da cidade"
        value={city}
        onChange={(e) => setCity(e.target.value)}
        required
      />
      <button type="submit">Consultar</button>
    </form>
  );
}
