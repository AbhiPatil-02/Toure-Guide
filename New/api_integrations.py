import requests

def get_weather(city):
    API_KEY = '<YOUR_OPENWEATHER_API_KEY>'  # get your free key from openweathermap.org
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    resp = requests.get(url)
    if resp.status_code == 200:
        w = resp.json()
        desc = w['weather'][0]['description']
        temp = w['main']['temp']
        return f"{temp}°C, {desc}"
    return "Weather unavailable"

def get_hotels(city):
    # Implement using Booking.com or Google Places API (add authentication and parsing logic)
    return "Live hotels API integration coming soon"
