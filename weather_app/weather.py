import requests

class Weather:
    def __init__(self, city= '', state= '', state_code= '', country= 'US', api_key = 'bd3844093fc57703b2cc41751e23f944', longitude = 0, latitude = 0, weather_data = {}, weather_condition = '', weather_temperature = 0):
        self.city = ''
        self.state = ''
        self.state_code = ''
        self.country = 'US'
        self.api_key = 'bd3844093fc57703b2cc41751e23f944'
        self.longitude = 0
        self.latitude = 0
        self.weather_data = {}
        self.weather_condition = '' # This is the info/variable you want if you want to display 
        self.weather_temperate = 0  # This is the info/variable you want if you want to display 


    # Function to convert the user State Input into a State Code for use to obtain weather data in the API Call
    def state_code_convert(self, state_input):
        self.state = state_input.title()
        state_input_lower_case = state_input.lower()
        match state_input_lower_case:
            case "alabama":
                self.state_code = "AL"
            case "alaska":
                self.state_code = "AK"
            case "arizona":
                self.state_code = "AZ"
            case "arkansas":
                self.state_code = "AR"
            case "california":
                self.state_code = "CA"
            case "colorado":
                self.state_code = "CO"
            case "connecticut":
                self.state_code = "CT"
            case "delaware":
                self.state_code = "DE"
            case "florida":
                self.state_code = "FL"
            case "georgia":
                self.state_code = "GA"
            case "hawaii":
                self.state_code = "HI"
            case "idaho":
                self.state_code = "ID"
            case "illinois":
                self.state_code = "IL"
            case "indiana":
                self.state_code = "IN"
            case "iowa":
                self.state_code = "IA"
            case "kansas":
                self.state_code = "KS"
            case "kentucky":
                self.state_code = "KY"
            case "louisiana":
                self.state_code = "LA"
            case "maine":
                self.state_code = "ME"
            case "maryland":
                self.state_code = "MD"
            case "massachusetts":
                self.state_code = "MA"
            case "michigan":
                self.state_code = "MI"
            case "minnesota":
                self.state_code = "MN"
            case "mississippi":
                self.state_code = "MS"
            case "missouri":
                self.state_code = "MO"
            case "montana":
                self.state_code = "MT"
            case "nebraska":
                self.state_code = "NE"
            case "nevada":
                self.state_code = "NV"
            case "new hampshire":
                self.state_code = "NH"
            case "new jersey":
                self.state_code = "NJ"
            case "new mexico":
                self.state_code = "NM"
            case "new york":
                self.state_code = "NY"
            case "north carolina":
                self.state_code = "NC"
            case "north dakota":
                self.state_code = "ND"
            case "ohio":
                self.state_code = "OH"
            case "oklahoma":
                self.state_code = "OK"
            case "oregon":
                self.state_code = "OR"
            case "pennsylvania":
                self.state_code = "PA"
            case "rhode island":
                self.state_code = "RI"
            case "south carolina":
                self.state_code = "SC"
            case "south dakota":
                self.state_code = "SD"
            case "tennessee":
                self.state_code = "TN"
            case "texas":
                self.state_code = "TX"
            case "utah":
                self.state_code = "UT"
            case "vermont":
                self.state_code = "VT"
            case "virginia":
                self.state_code = "VA"
            case "washington":
                self.state_code = "WA"
            case "west virginia":
                self.state_code = "WV"
            case "wisconsin":
                self.state_code = "WI"
            case "wyoming":
                self.state_code = "WY"
            case _:
                return False
        return True

    # Function to obtain geo coordinates for a specific city in the US, returns a dictionary containing the longitude and latitude
    def get_coordinates(self, city_input):
        self.city = city_input.title()


        # Converted Geo Coordinates to names API Call example
        # http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
        # Must use q=city,state_code,country_code or else you will get an object containing too many different Dallas location data and it will be messy to extract the correct coordinates

        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={self.city},{self.state_code},{self.country}&limit=5&appid={self.api_key}")

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
                print(self.city,", ", self.state, ", ", self.country, ", ", "Longitude: ", self.longitude, sep='')
                print(self.city,", ", self.state, ", ", self.country, ", ", "Latittude: ", self.latitude, sep='')
                return True
            else:
                print("Data object error")
                return False
        else:
            print("Response status failed.")
            return False

    def get_weather_data(self):

        # Use latitude and longitude from "data" to make another API Call
        # 'units': 'imperial' # imperial = Fahrenheit, metric = celsius
        weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&units=imperial&appid={self.api_key}")

        if weather_response.status_code == 200:
            print("Weather_response status was successful")
            self.weather_data = weather_response.json()
            print(self.weather_data)

            # print(f"Weather main in ", city_input_formatted, ": ", weather_data['weather'][0]['main'], sep='')  // This gives main weather, but weather description provides better weather info
            print(f"Weather description in ", self.city, ": ", self.weather_data['weather'][0]['description'], sep='')
            print(f"Temperature in ", self.city, ": ", self.weather_data['main']['temp'], " fahrenheit", sep='')
            return True
        else:
            print("Weather_response status failed with code:", weather_response.status_code) #Currently failing with Error 401, meaning unauthorized 
            return False