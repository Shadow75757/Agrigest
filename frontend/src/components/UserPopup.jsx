import React, { useState } from "react";

export default function UserPopup({ onSubmit }) {
  const [choice, setChoice] = useState(null);
  const [username, setUsername] = useState("");

  const handleGuest = () => {
    onSubmit("Guest");
  };

  const handleUser = () => {
    if (username.trim()) {
      onSubmit(username.trim());
    }
  };

  return (
    <div className="popup-backdrop">
      {!choice ? (
        <div className="popup-content">
          <h2>Bem-vindo ao Agrigest</h2>
          <button onClick={() => setChoice("guest")}>Guest</button>
          <button onClick={() => setChoice("user")}>User</button>
        </div>
      ) : choice === "user" ? (
        <div className="popup-content">
          <h3>Introduza seu nome</h3>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Nome"
          />
          <button onClick={handleUser} disabled={!username.trim()}>
            Confirmar
          </button>
        </div>
      ) : (
        <div className="popup-content">
          <h3>Entrou como Guest</h3>
          <button onClick={handleGuest}>Continuar</button>
        </div>
      )}
    </div>
  );
}
