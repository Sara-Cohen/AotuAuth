// Example: script.js

// Sample JavaScript code
document.addEventListener('DOMContentLoaded', function() {
    // Code to execute after the page has loaded
    console.log('JavaScript loaded!');

    // Example: Fetch data from the server
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            console.log('Data from server:', data);
            // Manipulate DOM or perform other operations based on data
        })
        .catch(error => console.error('Error fetching data:', error));
});
