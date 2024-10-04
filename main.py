from flask import Flask, jsonify, request, render_template
import requests
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
    city = request.args.get('city', 'unknown city')
    state = request.args.get('state', 'unknown state')

    """
     TODO:  This method will call the method you create that makes the API call.
            The response from the API should map to an object (create it based on the response)
            so that we can serialize it to a json
    """

    # /* Old Code, left here for reference in case

    # base_url = "http://api.openweathermap.org/data/2.5/weather"
    # parameters = {
    #     'city': "London",
    #     'appid': 'bd3844093fc57703b2cc41751e23f944', # Our OpenWeather API Key
    #     'units': 'imperial' # imperial = Fahrenheit, metric = celsius
    # }

    # */ End of Old Code


    # Converted Geo Coordinates to names API Call example
    # http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

    # This is an example of a correct API Call for converted geo coordinates into city/state/country names
    # http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API key}
    
    # response = request.get(base_url, params=parameters) # Old Code, left here for reference in case

    # Use the below response line of code to obtain "data", and use "data" to extract latitude and longitude for another API Call 
    # that will obtain more fields such as temperature and etc.


    # Must use q=city,state_code,country_code or else you will get an object containing too many different Dallas location data and it will be messy to extract the correct coordinates
    # state_code = 'TX'
    # country_code = 'US'
    

    # city_code = 'Dallas'
    # state_code = 'TX'
    
    # api_key = 
    country_code = 'US'

    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country_code}&limit=5&appid=bd3844093fc57703b2cc41751e23f944") #Currently Using Oroville as static API Call, change to [city] later




    if response.status_code == 200:
        print("City Coordinates response status was successful")
        data = response.json()

        # Use latitude and longitude from "data" to make another API Call
        # Example of a parameterized API Call that can contain weather data we want to extract: https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

        # Example of a real API Call that can contain weather data we want to extract: https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}
        if data:
            print("data if-statement was successful")
            print(data)
            longitude = data[0]['lon']
            latitude = data[0]['lat']
            print("Now will print lat-long coordinates for Dallas,TX,US")
            print("Dallas,TX,US Longitude:", longitude)
            print("Dallas,TX,US Latitude:", latitude)

            #Code is failing, I believe it is failing on the request line below
            weather_response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat=32.77&lon=-96.79&exclude=minutely,hourly,daily,alerts&appid=bd3844093fc57703b2cc41751e23f944")

            if weather_response.status_code == 200:
                print("Weather_response status was successful")
                weather_data = weather_response.json()
                print(weather_data)
            else:
                print("Weather_response status failed with code:", weather_response.status_code) #Currently failing with Error 401, meaning unauthorized 
                return None

            # print(f"Weather in London:")
            # print(f"Temperature: {data['main']['temp']} Fahrenheit")
        else:
            print("Data retrieval failed")
        return jsonify({"message": f"You sent: City - {city}, State - {state}"})
    else:
        print("Response status failed.")
        return None

    # # Return a JSON response
    # return jsonify({"message": f"You sent: City - {city}, State - {state}"})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
