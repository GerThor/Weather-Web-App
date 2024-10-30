// Function to fetch data from the server
function fetchData() {
    // Get the parameters from the input fields
    const city = document.getElementById("cityInput").value;
    const state = document.getElementById("state").value;

    // Send a GET request to the /api/data endpoint with the parameters
    fetch(`/api/GetWeatherData?city=${encodeURIComponent(city)}&state=${encodeURIComponent(state)}`)
        .then(response => response.json())
        .then(data => {
            // Display the response message in the responseData div
            const responseDataDiv = document.getElementById("responseData");
            responseDataDiv.innerHTML = `
                <div class="weather-info">
                    <h1>Weather Information</h1>

                    <h2>Location</h2>
                    <p><strong>City:</strong> ${ data.weather.city }</p>
                    <p><strong>State:</strong> ${ data.weather.state } (${ data.weather.state_code })</p>
                    <p><strong>Country:</strong> ${ data.weather.country }</p>

                    <div class="coordinates">
                        <h2>Coordinates</h2>
                        <p><strong>Longitude:</strong> ${ data.weather.longitude }</p>
                        <p><strong>Latitude:</strong> ${ data.weather.latitude }</p>
                    </div>

                    <div class="condition">
                        <h2>Weather Condition</h2>
                        <p><strong>Condition:</strong> ${ data.weather.weather_condition }</p>
                        <p><strong>Temperature:</strong> ${ data.weather.weather_temperature }°F</p>
                    </div>
                </div>`;
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            const responseDataDiv = document.getElementById("responseData");
            responseDataDiv.innerHTML = `<p>Error fetching data. Please try again.</p>`;
        });
}

// Attach an event listener to the button
document.getElementById("getDataBtn").addEventListener("click", fetchData);
