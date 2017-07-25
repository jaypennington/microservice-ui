from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Oh hai Mark!"

if __name__ == "__main__":
    #application.run()
    return render_template('index.html')

    
