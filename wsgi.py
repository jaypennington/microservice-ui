from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return "Existance is pain to a Meeseeks."

if __name__ == "__main__":
    application.run()
