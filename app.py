from flask import Flask, render_template, redirect, url_for # use Flask to render a template, redirecting to another url, and creating a URL
from flask_pymongo import PyMongo # use PyMongo to interact with Mongo database
import scraping # uses the scraping code 

app = Flask(__name__)

# telling Python how to connect to Mongo using PyMongo
#Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")# # tells Python that app will connect to Mongo using a URI (uniform resource idetifier)
#mongo = PyMongo(app) # is the URI to be used to connect to the app to Mongo. saying that the app can reach Mongo through the localhost server using port 27017, using a database named mars_app

@app.route("/")
def index():
    mars = mongo.db.mars.find_one() # uses PyMongo to find the mars collection in the database, which will be created when the the Jupyter scraping code is converted to Python script and assign it ot the mars variable
    return render_template("index.html", mars=mars) #tells Flask to return an HTML template using an index.html file (mars = mars) tells Python to use the mars collection in MongoDB


@app.route("/scrape") # defines the route flask will be using, will run the function tha we create just beneath it
def scrape(): # allows us to access the databases, scrape new data using the scraping.py script
    mars = mongo.db.mars # assigns a new variable that points to Mongo database mars = mongo.db.mars
    mars_data = scraping.scrape_all() # referencing the "scrape_all" function in the scraping.py file export
    mars.update({}, mars_data, upsert=True) # then update the database using .update(), "upsert=True" indicates to Mongo to create a new document if one doesn't already exist and new data will be saved. 
    return redirect('/', code=302) # navigate the page back to where the updated content can be seen.

if __name__ == "__main__":
    app.run