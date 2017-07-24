#simple GUI

from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Labeler")
root.geometry("200x50")

app = Frame(root)
app.grid()
label = Label(app, text = "This is a label!")

label.grid()

#kick off the event loop
root.mainloop()
