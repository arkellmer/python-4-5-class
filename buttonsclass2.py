from tkinter import *

class Application(Frame):

    def __init__(self, master):
        """initialize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.bttn1 = Button(self, text="i do nothing!")
        self.bttn1.grid()

        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="dont click me")
        self.bttn2.configure(bg="yellow")
        self.bttn2.configure(fg="red")