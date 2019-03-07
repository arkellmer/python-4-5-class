from tkinter import *

class Application(Frame):
    """gui application which can reveal the secret of longevity"""
    def __init__(self, master):
        """initialize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #create instruction label
        self.inst_lbl = Label(self, text="enter password for the secret life")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky = W)
        #create label for password
        self.pw_lbl = Label(self, text= "Password:")
        self.pw_lbl.grid(row=1,column=0, sticky = W)
        #create input box for password
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row= 1, column=1, sticky=W)

        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row=2,column=0, sticky=W)

        #create text widget to display message
        self.secret_txt = Text(self, width=35, height=5, wrap = WORD)
        self.secret_txt.grid(row=3,column=0,columnspan=2,sticky=W)

    def reveal(self):
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "42"
        else:
            message = ("thats not the correct password")
        self.secret_txt.delete(0.0,END)
        self.secret_txt.insert(0.0,message)

root = Tk()
root.title("Longevity")
root.geometry("300x150")
app = Application(root)
root.mainloop()