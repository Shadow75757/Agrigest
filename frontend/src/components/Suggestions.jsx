import React from "react";

export default function Suggestions({ suggestions }) {
  return (
    <div className="suggestions">
      <h2>Sugestões Agrícolas</h2>
      <ul>
        {suggestions.map((s, i) => (
          <li key={i}>{s}</li>
        ))}
      </ul>
    </div>
  );
}
