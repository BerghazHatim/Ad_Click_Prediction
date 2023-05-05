### Ad Click Prediction Web App
This is a web application that predicts whether a particular user is likely to click on an advertisement or not. The application uses a machine learning model that was developed using the Ad_Click_project file in this repository, and parameters were fetched using the GridSearch file.

### Project Structure
The project contains the following files and folders:

Data: This folder contains the data file used in the project.
FlaskApp: This folder contains the Flask application code and the necessary files to run the web application.
static: This folder contains the images folder, which has an image used in the background of the web app.
templates: This folder has the HTML file used to create the user interface.
app.py: This file contains the Flask code that takes values from the HTML page, links them to the machine learning model and displays the results.
model.pkl: This file is where the trained machine learning model is saved.
Usage
To run the application, follow these steps:


If you would like to run this app on ur local computer
Clone the repository to your local machine.
Navigate to the FlaskApp folder.
Open a terminal and run the following command: pip install -r requirements.txt
Run the application by typing: python app.py
Open your web browser and navigate to http://localhost:5000/ to access the application.
Credits
This application was developed by Berghaz Hatim. Feel free to contact me if you have any questions or suggestions.
