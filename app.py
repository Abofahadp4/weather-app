from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Weather App</h1>
        <form action="/weather" method="get">
            <label for="city">Enter city name:</label>
            <input type="text" id="city" name="city" required>
            <button type="submit">Get Weather</button>
        </form>
    '''

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return "City name is required!", 400

    api_key = "9336a7dfa301b6356c322cd359ea34ab"  # Your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return f"Error: {data.get('message', 'Unknown error')}", 400

    main = data['main']
    weather_description = data['weather'][0]['description']
    temperature = main['temp']
    pressure = main['pressure']
    humidity = main['humidity']

    return f'''
        <h1>Weather for {city}</h1>
        <p>Temperature: {temperature}°C</p>
        <p>Pressure: {pressure} hPa</p>
        <p>Humidity: {humidity}%</p>
        <p>Description: {weather_description}</p>
        <br><br>
        <a href="/">Back</a>
    '''

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")