# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Zayan" # write your name
    age = "12" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/")
def father():

    name = "Ajit" # write your name
    age = "51" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/")
def mother():

    name = "Raiyanath" # write your name
    age = "41" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/")
def friend():

    name = "Omar" # write your name
    age = "12" # write your age

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
