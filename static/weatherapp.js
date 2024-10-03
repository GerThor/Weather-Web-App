// Function to fetch data from the server
function fetchData() {
    // Get the parameters from the input fields
    const city = document.getElementById("cityInput").value;
    const state = document.getElementById("stateInput").value;

    // Send a GET request to the /api/data endpoint with the parameters
    fetch(`/api/GetWeatherData?city=${encodeURIComponent(city)}&state=${encodeURIComponent(state)}`)
        .then(response => response.json())
        .then(data => {
            // Display the response message in the responseData div
            const responseDataDiv = document.getElementById("responseData");
            responseDataDiv.innerHTML = `<p>${data.message}</p>`;
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            const responseDataDiv = document.getElementById("responseData");
            responseDataDiv.innerHTML = `<p>Error fetching data. Please try again.</p>`;
        });
}

// Attach an event listener to the button
document.getElementById("getDataBtn").addEventListener("click", fetchData);
