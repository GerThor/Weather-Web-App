from flask import Flask, jsonify, request, render_template

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

    # Return a JSON response
    return jsonify({"message": f"You sent: City - {city}, State - {state}"})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
