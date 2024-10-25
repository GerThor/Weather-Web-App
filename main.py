from flask import Flask, jsonify, request, render_template
from weather_app.weather import Weather

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

    weather_object.state_code_convert(state_input) # Returns True or False
    # TO DO: Error Handling, based on return value True or False

    weather_object.get_coordinates(city_input) # Returns True or False
    # TO DO: Error Handling, based on return value True or False

    weather_object.get_weather_data() # Returns True or False
    # TO DO: Error Handling, based on return value True or False.
    # Then display the weather data on website, we can get temperature and weather description, there is already output of these two values in the output terminal


    return jsonify({"message": f"You sent: City - {weather_object.city}, State - {weather_object.state}"})






# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
