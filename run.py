import os
from flask import Flask, render_template  #importing our flask class, capital F indicates it is a class. render template help you avoid typing all your code into the python file


app = Flask(__name__)  #creates an instance of this class and storing in a veriable called "app"
                    #the first argument of flask class is the name of applications module - our package (flack needs this to know where to look for templates and static files)

@app.route("/")        #uses a route decorater to tell flask what URl to trigger the function that follows(decorator is a way of wrapping functions.all functions are objects and can be passed around)
def index():           #when we try to browse the root directory, as indicated by the "/", then Flask triggers the index function underneath and returns ....
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__": #if name is equal to main then we are goin to wrap our app with the following arguments
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),   #we are using the os module from teh stanard libary to get hte ip enviorment variable if it exists but set a default value if its not found
        port=int(os.environ.get("PORT", "5000")),
        debug=True) #debug=true will allow us to debug our code much easier (NB should not be set to debug=true in a production application or when we submit our project for assessment)
                    # as it allows arbitary code to run and this is a security flaw