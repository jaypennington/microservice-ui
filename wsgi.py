from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    #return "Existance is pain to a Meeseeks."
    return render_template('index.html')

if __name__ == "__main__":
    application.run()
