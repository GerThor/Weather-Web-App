from flask import Flask, jsonify, request, render_template
from weather_app.openweathermap import OpenWeatherMap

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

    weather_object = Weather(city=city_input, state_code=state_input)

    weather_object.initialize_coordinates()

    weather_object.initialize_weather_data()

    return jsonify({"weather":weather_object.to_dict()})






# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
