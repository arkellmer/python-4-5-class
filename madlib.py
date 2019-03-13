#simple gui
#demonstrates creating a window

from tkinter import *

#create the root window
# root = Tk()
# #modify the window
# root.title("Simple GUI")
# root.geometry("999x666")
# root.configure(bg = "green")
# # changes icon #root.wm_iconbitmap("")
#
# # creates a frame in hte window to hold other widgets
# app = Frame(root)
# app.grid()

#creates a label in the frame
# label = Label(app, text = "this is a fancy Label")
# label.config(bg = "purple")
# label.config(fg = "purple")
#
# lbl = Label(app, text = "i'm a label")
# lbl.config(font=("",55))
#
# lbl3 = Label(app, text = "this is another label")
# lbl3.config(font=("roman"))
#
# #displays labels
# lbl3.grid()
# label.grid()
# lbl.grid()
#

#
# #kick off the windows event-loop
# root.mainloop()
#

class Application(Frame):

    """a gui that sets up a mad lib"""
    def __init__(self, master):

        """initialize frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        """creates a label for instructions"""
        Label(self, text="Enter words or check boxes to fill out the mad lib.")\
            .grid(row=0, column=0, columnspan=2, sticky=W)

        """creates labels and text boxes for input"""
        Label(self, text="Enter a name:").grid(row=1, column=0, sticky=W)
        self.input_txt1 = Text(self, width=10, height=1, wrap=WORD)
        self.input_txt1.grid(row=1, column=1, sticky=W)

        Label(self, text="Enter a noun:").grid(row=2, column=0, sticky=W)
        self.input_txt2 = Text(self, width=10, height=1, wrap=WORD)
        self.input_txt2.grid(row=2, column=1, sticky=W)

        Label(self, text="Enter a noun:").grid(row=3, column=0, sticky=W)
        self.input_txt3 = Text(self, width=10, height=1, wrap=WORD)
        self.input_txt3.grid(row=3, column=1, sticky=W)

        """makes check boxes"""
        Label(self, text="Check any that you want.").grid(row=4, column=0, sticky=W)
        self.check1 = BooleanVar()
        Checkbutton(self, text="annoying", variable=self.check1)\
            .grid(row=4, column=1, sticky=W)

        self.check2 = BooleanVar()
        Checkbutton(self, text="snobby", variable=self.check2) \
            .grid(row=4, column=2, sticky=W)

        self.check3 = BooleanVar()
        Checkbutton(self, text="dumb", variable=self.check3)\
            .grid(row=4, column=3, sticky=W)

        """makes radio box"""
        Label(self, text="Check the one you want.").grid(row=5, column=0, sticky=W)
        self.time_radio = StringVar()
        self.time_radio.set(None)

        Radiobutton(self, text="Lunch", variable=self.time_radio, value="lunch.")\
            .grid(row=5, column=1, sticky=W)

        Radiobutton(self, text="Dinner", variable=self.time_radio, value="dinner.")\
            .grid(row=5, column=2, sticky=W)

        Radiobutton(self, text="Midnight", variable=self.time_radio, value="midnight.")\
            .grid(row=5, column=3, sticky=W)

        """makes a button to submit them"""
        self.submit_bttn = Button(self, text="Submit", command=self.finish)
        self.submit_bttn.grid(row=6, column=0, sticky=W)

        """makes a blank box for text to be shown in."""
        self.story_txt = Text(self, width=50, height=7, wrap=WORD).grid(row=7, column=0, sticky=W)

    def finish(self):
        """gets variables"""
        #name1 = self.input_txt1.get()
        #noun1 = self.input_txt2.get()
        #noun2 = self.input_txt3.get()
        adjective = ""
        if self.check1.get():
            adjective += "annoying, "
        if self.check2.get():
            adjective += "snobby, "
        if self.check3.get():
            adjective += "dumb, "
        time1 = self.time_radio.get()

        """creates story"""
        story = "Hey there "
        #story += name1
        story += "! How is your day going? Hopefully you haven't stepped in any "
        #story += noun1
        story += " today. I saw a puddle of it back in the parking lot. Anyway, Timothy said you had to finish the "
        #story += noun2
        story += " paperwork by the end of today. Those "
        story += adjective
        story += "guys in marketing needed it by tomorrow. Hopefully we finish it before "
        story += time1

        """display story"""
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)




root = Tk()
root.title("Mad Lib")
root.geometry("900x600")
app = Application(root)
root.mainloop()




