#Learning about flask and api

from flask import Flask, jsonify
#Flask: Flask is a web development framework for Python, by which you can create web applications, including APIs.
#jsonify: jsonify is a supporting function to send Python dictionaries back as JSON. APIs usually talk in terms of JSON.

app = Flask(__name__)
#This line creates a new instance of the Flask class. Flask uses this instance to set up routes and handle requests.
#__name__ is the name of the module which is passed to Flask in order to enable it to locate the app.


# Weather data examples
weather_data = {
    "london": {"temperature": "15°C", "condition": "Cloudy"},
    "konya": {"temperature": "20°C", "condition": "Sunny"},
    "tokyo": {"temperature": "18°C", "condition": "Rainy"},
    "dubai": {"temperature": "17°C", "condition": "Partly Cloudy"},}

@app.route('/') #This is the route for the home page of the web application. It maps the root URL to a specific function, allowing us to define what the user sees when they first access the site.
def home(): #Defines the content a user sees on the homepage, its like a greeting to the user.
    return """ 
           Welcome to the Weather API! Use /weather/[city] to get the weather 
           eg --> /weather/london.
           Available cities: London, Konya, Tokyo and Dubai
           
           """
#These are the sentences the user will see when they click on the link.

@app.route('/weather/<city>', methods=['GET']) #creates another URL path. Flask captures the value in <city> and passes it to the function.
def get_weather(city): #It takes the city string from the URL, looks it up in the weather_data dictionary, and returns the weather information in JSON format.
    if city in weather_data:
        return jsonify({ "city": city, **weather_data[city] }) #Returns the information if the city exists in my dictionary.
    else:
        return jsonify({"error": "City not found"}), 404 #Error handling if the city isnt included.


if __name__ == '__main__': #It checks whether this script is run directly or imported as a module from some other program.If run directly: It executes the code inside the if block.If imported: It skips the code inside the if block
    app.run(debug=True) #Starts the local server at http://127.0.0.1:5000/ With debug=True:Auto-reloads your app when you change code.Shows detailed error messages in the browser.