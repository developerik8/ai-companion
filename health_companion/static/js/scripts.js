// static/js/scripts.js

// Function to fetch the latest metrics from the backend
function fetchMetrics() {
    fetch('/api/metrics')
        .then(response => response.json())
        .then(data => {
            const metricsDiv = document.getElementById('metrics');
            metricsDiv.innerHTML = `
                <p>Steps: ${data.steps}</p>
                <p>Heart Rate: ${data.heart_rate}</p>
                <p>Calories: ${data.calories}</p>
            `;
        })
        .catch(error => console.error('Error fetching metrics:', error));
}

// Function to save health metrics to the backend
function saveMetrics() {
    const steps = document.getElementById('steps').value;
    const heartRate = document.getElementById('heart_rate').value;
    const calories = document.getElementById('calories').value;

    if (steps && heartRate && calories) {
        const data = { steps: steps, heart_rate: heartRate, calories: calories };
        
        fetch('/api/metrics', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            alert('Metrics saved successfully!');
            fetchMetrics(); // Refresh metrics after saving
        })
        .catch(error => console.error('Error saving metrics:', error));
    } else {
        alert('Please fill in all fields');
    }
}
