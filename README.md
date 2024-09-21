# Firebase App Check Device Verification Application

This Python application uses Firebase App Check to verify that requests come from authorized devices. Built with Flask, the app integrates with Firebase to ensure that only legitimate requests are processed.

## Features

- Device verification using Firebase App Check.
- Simple API with a sample endpoint.
- JWT for handling authentication and token verification.
- Containerization with Docker for easy deployment.

## Requirements

- Python 3.x
- (Optional) Docker

## Instructions to Run the Application

1. **Obtain your Firebase `serviceAccountKey.json`:**  
   Make sure you have your Firebase credentials file.

2. **Set environment variables in your `.env` file:**  
   Add the following lines to your `.env` file:

   GOOGLE_APPLICATION_CREDENTIALS_FILE=serviceAccountKey.json
   GOOGLE_APPLICATION_CREDENTIALS_PATH=/absolute/path/to/serviceAccountKey.json

3. **Run the application:**  
Use your preferred method (Python or Docker) to start the application.

### Running the Application with Python

3. **Set up a virtual environment:**  
If you want to run the application using Python, create a virtual environment and activate it:

For Mac:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```





