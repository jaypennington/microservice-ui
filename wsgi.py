from flask import Flask
import render_template, json, fetch-everywhere
application = Flask(__name__)

@application.route("/")
def hello():
    #return "Existance is pain to a Meeseeks."
    return render_template('index.html')

if __name__ == "__main__":
    application.run()
