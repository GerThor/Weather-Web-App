import json
from typing import List, Optional

class Weather:
    def __init__(self, id: int, main: str, description: str, icon: str):
        self.id = id
        self.main = main
        self.description = description
        self.icon = icon

    def __repr__(self):
        return f"Weather(id={self.id}, main='{self.main}', description='{self.description}', icon='{self.icon}')"


class Sys:
    def __init__(self, type: int, id: int, country: str, sunrise: int, sunset: int):
        self.type = type
        self.id = id
        self.country = country
        self.sunrise = sunrise
        self.sunset = sunset

    def __repr__(self):
        return (f"Sys(type={self.type}, id={self.id}, country='{self.country}', "
                f"sunrise={self.sunrise}, sunset={self.sunset})")

class Main:
    def __init__(self, temp, feels_like: int, temp_min: int, temp_max: int, pressure: int, humidity: int, sea_level: int, grnd_level: int):
        self.temp = temp
        self.feels_like = feels_like
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.pressure = pressure
        self.humidity = humidity
        self.sea_level = sea_level
        self.grnd_level = grnd_level


    def __repr__(self):
        return (f"Main(temp={self.temp}, feels_like={self.feels_like}, temp_min={self.temp_min}', "
                f"temp_max={self.temp_max}, pressure={self.pressure}, humidity={self.humidity}, "
                f"sea_level={self.sea_level}, grnd_level={self.grnd_level})")

class WeatherData:
    def __init__(self, weather: List[Weather], base: str, main: Main,
                 visibility: int, dt: int, sys: Sys,
                 timezone: int, id: int, name: str, cod: int):
        self.weather = weather
        self.base = base
        self.main = main
        self.visibility = visibility
        self.dt = dt
        self.sys = sys
        self.timezone = timezone
        self.id = id
        self.name = name
        self.cod = cod

    def __repr__(self):
        return (f"WeatherData( weather={self.weather}, base='{self.base}', "
                f"main={self.main}, "
                f"visibility={self.visibility}, "
                f"dt={self.dt}, sys={self.sys}, timezone={self.timezone}, "
                f"id={self.id}, name='{self.name}', cod={self.cod})")



