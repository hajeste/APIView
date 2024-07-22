import requests
from django.conf import settings


class WeatherAPI:
    def __init__(self):
        self.api_key = settings.OPENWEATHER_API_KEY
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            # Перевірка, що всі необхідні дані присутні
            required_keys = ['main', 'wind', 'weather', 'sys']
            if all(key in data for key in required_keys):
                # Додаємо конвертовані дані
                data['sys']['sunrise'] = self.convert_timestamp(data['sys']['sunrise'])
                data['sys']['sunset'] = self.convert_timestamp(data['sys']['sunset'])
                return data
            else:
                return {'error': 'Incomplete data from API'}
        else:
            return {'error': 'Error fetching data from API'}

    def convert_timestamp(self, timestamp):
        from datetime import datetime
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
