from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

API_KEY = '8308621c89d7d1f83e27b92133cd6a04'

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>Clima</title>
    <style>
        body { background-color: #111; color: #eee; font-family: sans-serif; padding: 20px; }
        input, button { padding: 6px 12px; font-size: 16px; }
        .result { margin-top: 20px; }
    </style>
</head>
<body>
    <h1>Consultar Clima</h1>
    <form method="get">
        <input type="text" name="city" placeholder="Digite o nome da cidade" required>
        <button type="submit">Buscar</button>
    </form>

    {% if weather %}
        <div class="result">
            <h2>{{ weather['name'] }} - {{ weather['sys']['country'] }}</h2>
            <p>Temperatura: {{ weather['main']['temp'] }}°C</p>
            <p>Clima: {{ weather['weather'][0]['description'] }}</p>
            <p>Umidade: {{ weather['main']['humidity'] }}%</p>
        </div>
    {% elif error %}
        <div class="result">
            <p style="color: red;">Erro: {{ error }}</p>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    city = request.args.get("city")
    weather = None
    error = None

    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                weather = response.json()
            else:
                error = f"Cidade não encontrada ou erro na API (status {response.status_code})"
        except Exception as e:
            error = f"Erro ao conectar à API: {e}"

    return render_template_string(HTML_TEMPLATE, weather=weather, error=error)
