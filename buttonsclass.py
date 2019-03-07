from tkinter import *
from tkinter import font

root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")
root.configure(bg="red")

app = Frame(root)
app.grid()
app.configure()

bttn1 = Button(app, text="i do nothing!")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text="dont click me")
bttn2.configure(bg="yellow")
bttn2.configure(fg="red")






root.mainloop()
