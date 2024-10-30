import requests
from weather_app.utils import get_state_name
from weather_app.weather_data import WeatherData, Weather, Sys


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
        self.weather_condition = ''  # This is the info/variable you want if you want to display
        self.weather_temperate = 0  # This is the info/variable you want if you want to display

    # Function to obtain geo coordinates for a specific city in the US, returns a dictionary containing the longitude
    # and latitude
    def initialize_coordinates(self):

        # Converted Geo Coordinates to names API Call example http://api.openweathermap.org/geo/1.0/direct?q={city
        # name},{state code},{country code}&limit={limit}&appid={API key} Must use q=city,state_code,country_code or
        # else you will get an object containing too many different Dallas location data and it will be messy to
        # extract the correct coordinates

        response = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={self.city},{self.state_code},{self.country}&limit=5&appid={self.api_key}")

        if response.status_code == 200:
            print("City Coordinates response status was successful")
            data = response.json()

            # Use latitude and longitude from "data" to make another API Call
            # Example of a parameterized API Call that can contain weather data we want to extract: https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

            # Example of a real API Call that can contain weather data we want to extract: https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}
            if data:
                print("data if-statement was successful")
                print(data)
                self.longitude = round(data[0]['lon'], 2)
                self.latitude = round(data[0]['lat'], 2)

                print("Now will print lat-long coordinates for:", self.city, self.state, self.country)
                print(self.city, ", ", self.state, ", ", self.country, ", ", "Longitude: ", self.longitude, sep='')
                print(self.city, ", ", self.state, ", ", self.country, ", ", "Latittude: ", self.latitude, sep='')
                return True
            else:
                print("Data object error")
                return False
        else:
            print("Response status failed.")
            return False

    def initialize_weather_data(self):

        # Use latitude and longitude from "data" to make another API Call
        # 'units': 'imperial' # imperial = Fahrenheit, metric = celsius
        weather_response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&units=imperial&appid={self.api_key}")

        if weather_response.status_code == 200:
            print("Weather_response status was successful")
            self.weather_data = OpenWeatherMap.parse_weather_data_json(weather_response.json())
            print(self.weather_data)

            # print(f"Weather main in ", city_input_formatted, ": ", weather_data['weather'][0]['main'], sep='')  // This gives main weather, but weather description provides better weather info
            print(f"Weather description in ", self.city, ": ", self.weather_data.weather[0].description, sep='')

            return True
        else:
            print("Weather_response status failed with code:",
                  weather_response.status_code)  # Currently failing with Error 401, meaning unauthorized
            return False

    # Method to Convert object to dictionary
    def to_dict(self):
        return {
            'city': self.city,
            'state': self.state,
            'state_code': self.state_code,
            'country': self.country,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'weather_condition': self.weather_condition,
            'weather_temperature': self.weather_temperate
            # 'weather_data': self.weather_data  # You may want to serialize this as well
        }

    # convert the json property weather data form the repsonse to an object
    @staticmethod
    def parse_weather_data_json(json_data: dict) -> WeatherData:
        weather = [Weather(**w) for w in json_data['weather']]
        sys_data = Sys(**json_data['sys'])

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
