# Firebase App Check Device Verification Application

This Python application uses Firebase App Check to verify that requests come from authorized devices. Built with Flask, the app integrates with Firebase to ensure that only legitimate requests are processed.

## Features

- Device verification using Firebase App Check.
- Simple API with a sample endpoint.
- Containerization with Docker for easy deployment.

## Requirements

- Docker
  
  or

- Python 3.X.X

##  Steps before run

**Obtain your Firebase `serviceAccountKey.json`:**

Make sure you have your Firebase credentials file. To generate it, follow these steps:

- Go to the [Firebase Console](https://console.firebase.google.com/).
- Select your project.
- Navigate to **Project Settings** (click the gear icon in the sidebar).
- Go to the **Service accounts** tab.
- Click **Generate new private key** to download the `serviceAccountKey.json` file.

For more information, visit the official Firebase guide on [service accounts](https://firebase.google.com/support/guides/service-accounts).

## Run the application 
Use your preferred method (Docker or Python) to start the application.

**Running the Application with Docker:**

1. Install Docker Desktop if you don't have it already. You can download it [here](https://www.docker.com/products/docker-desktop).

2. Download the Docker image from Docker Hub by running the following command:

   ```bash
   docker pull koke050800/app-check-test
   ```

3. Configure the container:
   - Expose the port: `5001`
     
   - In Volumes, map the service account JSON file from your host machine (PC) to the container:
     - **Host path:** `/absolute/path/to/yourServiceAccountKey.json`
     - **Container path:** `/app/yourServiceAccountKey.json`
   
   - In Environment Variables, add the following variable:
     - **Variable:** ```GOOGLE_APPLICATION_CREDENTIALS_PATH```
     - **Value:** `/app/yourServiceAccountKey.json`
   

   You can refer to the image below for a better understanding:
   ![App Screenshot](images/images/config_container.png)


**Running the Application with Python:**
1. Add the following lines to your .env file. Make sure the .env file is located at the highest level within your project folder (root directory):
   
   Add the following lines to your `.env` file:

   GOOGLE_APPLICATION_CREDENTIALS_FILE=serviceAccountKey.json
   GOOGLE_APPLICATION_CREDENTIALS_PATH=/absolute/path/to/serviceAccountKey.json

2. Create a virtual environment and:
   
   For Mac:
   ```bash
   python3 -m venv .venv
   ```
3. Activate virtual environment:
   
   For Mac:
   ```bash
   source .venv/bin/activate 
   ```
4. Install all python requirements:
   
   For Mac:
   ```bash
   pip3 install -r requirements.txt 
   ```
5. Run app
   
   For Mac:
   ```bash
   dotenv run -- python src/firebase_app_check.py
   ```
## Create your own image and container
If you prefer, you can modify or extend the project as needed. The repository includes a pre-configured Dockerfile and docker-compose.yml to help you easily containerize the application.

**Create your own Docker image:**
You can build and run the application using Docker with the following steps:

1. Add the following lines to your .env file. Make sure the .env file is located at the highest level within your project folder (root directory):
   
   Add the following lines to your `.env` file:

   GOOGLE_APPLICATION_CREDENTIALS_FILE=serviceAccountKey.json
   GOOGLE_APPLICATION_CREDENTIALS_PATH=/absolute/path/to/serviceAccountKey.json

2. Run the command of docker compose:
   
   For Mac:
   ```bash
   docker-compose up --build
   ```
