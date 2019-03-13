#calculator gui
#andrew kellmer

from tkinter import *

class Application(Frame):

    """a gui that sets up a calcualtor"""

    def __init__(self, master):

        """initialize frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        value1 = 0
        value2 = 0
        operator = ""

        self.display = Text(self, width=20, height=1, wrap=WORD).grid(row=0,column=0, columnspan=4, sticky=W)

        self.button7 = Button(self, text="7", command=self.update, width=5).grid(row=1, column=0, sticky=W)
        self.button8 = Button(self, text="8", command=self.update, width=5).grid(row=1, column=1, sticky=W)
        self.button9 = Button(self, text="9", command=self.update, width=5).grid(row=1, column=2, sticky=W)

        self.division = Button(self, text="/", width=5).grid(row=1, column=3, sticky=W)

        self.button4 = Button(self, text="4", command=self.update, width=5).grid(row=2, column=0, sticky=W)
        self.button5 = Button(self, text="5", command=self.update, width=5).grid(row=2, column=1, sticky=W)
        self.button6 = Button(self, text="6", command=self.update, width=5).grid(row=2, column=2, sticky=W)

        self.multiplication = Button(self, text="*", width=5).grid(row=2, column=3, sticky=W)

        self.button1 = Button(self, text="1", command=self.update, width=5).grid(row=3, column=0, sticky=W)
        self.button2 = Button(self, text="2", command=self.update, width=5).grid(row=3, column=1, sticky=W)
        self.button3 = Button(self, text="3", command=self.update, width=5).grid(row=3, column=2, sticky=W)

        self.subtraction = Button(self, text="-", width=5).grid(row=3, column=3, sticky=W)

        self.button0 = Button(self, text="0", command=self.update, width=5).grid(row=4, column=1, sticky=W)

        self.calc = Button(self, text="=", command=self.calculate, width=5).grid(row=4, column=2, sticky=W)
        self.addition = Button(self, text="+", width=5).grid(row=4, column=3, sticky=W)




    def update(self):
        pass

    def calculate(self):
        pass



root = Tk()
root.title("Calculator")
root.geometry("600x600")
app = Application(root)
root.mainloop()