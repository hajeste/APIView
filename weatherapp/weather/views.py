from django.shortcuts import render
from .utils import WeatherAPI


def weather_view(request):
    city = request.GET.get('city')
    weather_data = None
    error = None

    if city:
        weather_api = WeatherAPI()
        weather_data = weather_api.get_weather(city)
        if not weather_data:
            error = 'Could not retrieve weather data'

    return render(request, 'weather/weather.html', {
        'weather_data': weather_data,
        'error': error
    })
