# Firebase App Check Device Verification Application

This Python application uses Firebase App Check to verify that requests come from authorized devices. Built with Flask, the app integrates with Firebase to ensure that only legitimate requests are processed.

## Features

- Device verification using Firebase App Check.
- Simple API with a sample endpoint.
- Containerization with Docker for easy deployment.

## Requirements

- Python 3.x
- (Optional) Docker

## Instructions to config the Application

1. **Obtain your Firebase `serviceAccountKey.json`:**  
   Make sure you have your Firebase credentials file.

2. **Set environment variables in your `.env` file:**  
   Add the following lines to your `.env` file:

   GOOGLE_APPLICATION_CREDENTIALS_FILE=serviceAccountKey.json
   GOOGLE_APPLICATION_CREDENTIALS_PATH=/absolute/path/to/serviceAccountKey.json

### Run the application 
Use your preferred method (Python or Docker) to start the application.

**Running the Application with Python:**

1. Create a virtual environment and:
   For Mac:
   ```bash
   python3 -m venv .venv
   ```
2. Activate virtual environment:
   
   For Mac:
   ```bash
   source .venv/bin/activate 
   ```
4. Install all python requirements:
   
   For Mac:
   ```bash
   python -m pip install -r requirements.txt 
   ```
6. Run app
   
   For Mac:
   ```bash
   dotenv run -- python src/firebase_app_check.py
   ```
