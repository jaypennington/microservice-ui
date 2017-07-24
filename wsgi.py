from flask import Flask
application = Flask(__name__)

from Tkinter import *

@application.route("/")
def hello():
    #create the window
    root = Tk()

    #modify root window
    root.title("Simple GUI")
    root.geometry("200x100")

    #kick off the event loop
    root.mainloop()
    return "Oh hai Mark!"

if __name__ == "__main__":
    application.run()
