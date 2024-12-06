# main.py
import requests
import logging
from weather_app.LogConfig import configure_logging
from weather_app.utils import get_state_name
from weather_app.weather_data import WeatherData, Weather, Sys

# Configure logging from LogConfig
configure_logging()
logger = logging.getLogger(__name__)

class OpenWeatherMap:
    def __init__(self, city='', state='', state_code='', country='US', api_key='bd3844093fc57703b2cc41751e23f944',
                 longitude=0, latitude=0, weather_data={}, weather_condition='', weather_temperature=0):
        self.city = city
        self.state = get_state_name(state_code)
        self.state_code = state_code
        self.country = country
        self.api_key = api_key
        self.longitude = 0
        self.latitude = 0
        self.weather_data = {}
        self.weather_condition = ''
        self.weather_temperature = 0

        logger.info(f"Initialized OpenWeatherMap with city={city}, state_code={state_code}, country={country}")

    def initialize_coordinates(self):
        try:
            response = requests.get(
                f"http://api.openweathermap.org/geo/1.0/direct?q={self.city},{self.state_code},{self.country}&limit=5&appid={self.api_key}"
            )

            if response.status_code == 200:
                logger.info("City coordinates API response successful")
                data = response.json()

                if data:
                    logger.info(f"Data received for {self.city}: {data}")
                    self.longitude = round(data[0]['lon'], 2)
                    self.latitude = round(data[0]['lat'], 2)

                    logger.info(f"Coordinates for {self.city}: Longitude={self.longitude}, Latitude={self.latitude}")
                    return True
                else:
                    logger.error("No data returned from city coordinates API", exc_info=True)
                    return False
            else:
                logger.error(f"Failed to get city coordinates, status code: {response.status_code}", exc_info=True)
                return False
        except Exception as e:
            logger.exception(f"Error in initialize_coordinates: {e}")
            return False

    def initialize_weather_data(self):
        try:
            weather_response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&units=imperial&appid={self.api_key}"
            )

            if weather_response.status_code == 200:
                logger.info("Weather data API response successful")
                self.weather_data = OpenWeatherMap.parse_weather_data_json(weather_response.json())
                logger.info(f"Weather data for {self.city}: {self.weather_data}")

                return True
            else:
                logger.error(f"Failed to get weather data, status code: {weather_response.status_code}", exc_info=True)
                return False
        except Exception as e:
            logger.exception(f"Error in initialize_weather_data: {e}")
            return False

    def to_dict(self):
        logger.info(f"Converting OpenWeatherMap object to dictionary for {self.city}")
        return {
            'city': self.city,
            'state': self.state,
            'state_code': self.state_code,
            'country': self.country,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'weather_condition': self.weather_condition,
            'weather_temperature': self.weather_temperature
        }

    @staticmethod
    def parse_weather_data_json(json_data: dict) -> WeatherData:
        try:
            weather = [Weather(**w) for w in json_data['weather']]
            sys_data = Sys(**json_data['sys'])

            logger.info("Parsing weather data JSON")
            return WeatherData(
                weather=weather,
                base=json_data['base'],
                visibility=json_data['visibility'],
                dt=json_data['dt'],
                sys=sys_data,
                timezone=json_data['timezone'],
                id=json_data['id'],
                name=json_data['name'],
                cod=json_data['cod']
            )
        except Exception as e:
            logger.exception(f"Error parsing weather data JSON: {e}")
            raise
