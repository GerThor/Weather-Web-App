from flask import Flask, jsonify, request, render_template
from weather_app.weather import Weather



# def state_code_convert(state):
#     state_code = ''
#     state_input_lower_case = state.lower()
#     match state_input_lower_case:
#         case "alabama":
#             state_code = "AL"
#         case "alaska":
#             state_code = "AK"
#         case "arizona":
#             state_code = "AZ"
#         case "arkansas":
#             state_code = "AR"
#         case "california":
#             state_code = "CA"
#         case "colorado":
#             state_code = "CO"
#         case "connecticut":
#             state_code = "CT"
#         case "delaware":
#             state_code = "DE"
#         case "florida":
#             state_code = "FL"
#         case "georgia":
#             state_code = "GA"
#         case "hawaii":
#             state_code = "HI"
#         case "idaho":
#             state_code = "ID"
#         case "illinois":
#             state_code = "IL"
#         case "indiana":
#             state_code = "IN"
#         case "iowa":
#             state_code = "IA"
#         case "kansas":
#             state_code = "KS"
#         case "kentucky":
#             state_code = "KY"
#         case "louisiana":
#             state_code = "LA"
#         case "maine":
#             state_code = "ME"
#         case "maryland":
#             state_code = "MD"
#         case "massachusetts":
#             state_code = "MA"
#         case "michigan":
#             state_code = "MI"
#         case "minnesota":
#             state_code = "MN"
#         case "mississippi":
#             state_code = "MS"
#         case "missouri":
#             state_code = "MO"
#         case "montana":
#             state_code = "MT"
#         case "nebraska":
#             state_code = "NE"
#         case "nevada":
#             state_code = "NV"
#         case "new hampshire":
#             state_code = "NH"
#         case "new jersey":
#             state_code = "NJ"
#         case "new mexico":
#             state_code = "NM"
#         case "new york":
#             state_code = "NY"
#         case "north carolina":
#             state_code = "NC"
#         case "north dakota":
#             state_code = "ND"
#         case "ohio":
#             state_code = "OH"
#         case "oklahoma":
#             state_code = "OK"
#         case "oregon":
#             state_code = "OR"
#         case "pennsylvania":
#             state_code = "PA"
#         case "rhode island":
#             state_code = "RI"
#         case "south carolina":
#             state_code = "SC"
#         case "south dakota":
#             state_code = "SD"
#         case "tennessee":
#             state_code = "TN"
#         case "texas":
#             state_code = "TX"
#         case "utah":
#             state_code = "UT"
#         case "vermont":
#             state_code = "VT"
#         case "virginia":
#             state_code = "VA"
#         case "washington":
#             state_code = "WA"
#         case "west virginia":
#             state_code = "WV"
#         case "wisconsin":
#             state_code = "WI"
#         case "wyoming":
#             state_code = "WY"
#     return state_code


# def get_coordinates(city_input, state_code, country_code, api_key):
#     city_input_formatted = city_input.title()
#     response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_input_formatted},{state_code},{country_code}&limit=5&appid={api_key}")

#     if response.status_code == 200:
#         print("City Coordinates response status was successful")
#         data = response.json()

#         # Use latitude and longitude from "data" to make another API Call
#         # Example of a parameterized API Call that can contain weather data we want to extract: https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

#         # Example of a real API Call that can contain weather data we want to extract: https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}
#         if data:
#             print("data if-statement was successful")
#             print(data)
#             longitude = round(data[0]['lon'], 2)
#             latitude = round(data[0]['lat'], 2)
#             print("Now will print lat-long coordinates for:", city_input_formatted, state_input.title(), country_code)
#             print(city_input_formatted,", ", state_input.title(), ", ", country_code, ", ", "Longitude: ", longitude, sep='')
#             print(city_input_formatted,", ", state_input.title(),", ", country_code,", ", "Latitude: ", latitude, sep='')
#     else:
#             print("Response status failed.")
#             return None


# Create a Flask application instance
app = Flask(__name__)


# Define the root route ('/') that renders index.html
@app.route('/')
def home():
    return render_template('index.html')


"""
    route that accepts a city as the query parameters. Pass that city to the weather API and return it.
"""
@app.route('/api/GetWeatherData', methods=['GET'])
def get_data():
    # Extract city and state parameters from the request
    city_input = request.args.get('city', 'unknown city')
    state_input = request.args.get('state', 'unknown state')


    """
     TODO:  This method will call the method you create that makes the API call.
            The response from the API should map to an object (create it based on the response)
            so that we can serialize it to a json
    """
    weather_object = Weather(city_input)
    weather_object.state_code_convert(state_input)
    weather_object.get_coordinates(city_input)
    weather_object.get_weather_data()

    return jsonify({"message": f"You sent: City - {weather_object.city}, State - {weather_object.state}"})


    # # Return a JSON response
    # return jsonify({"message": f"You sent: City - {city}, State - {state}"})





# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
