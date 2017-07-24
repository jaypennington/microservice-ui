from Tkinter import *
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Oh hai Mark!"

if __name__ == "__main__":
    application.run()
    #create the window
    root = Tk()

    #modify root window
    root.title("Simple GUI")
    root.geometry("200x100")

    #kick off the event loop
    root.mainloop()
