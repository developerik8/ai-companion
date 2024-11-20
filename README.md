The project was built using a combination of technologies:

Backend:

Flask was used to create a RESTful API for handling user requests (fetching and saving health data).
SQLite was used for database management, where user health metrics (steps, heart rate, and calories) are stored and retrieved.
Frontend:

HTML and CSS were used to build the static user interface.
JavaScript was used for dynamic interactions, including form submission and fetching data without reloading the page.
Features:

A chatbot interface was included (for future expansion) to provide personalized health tips based on user input.
The application allows users to input health metrics, such as steps taken, heart rate, and calories burned, and saves these metrics to the database.
The latest metrics can be fetched and displayed in real time using the frontend.
Deployment:

The app was run locally using Flask’s built-in server for testing. For production, it could be deployed on cloud platforms such as Heroku or AWS.
