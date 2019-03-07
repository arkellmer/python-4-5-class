from tkinter import *

class Application(Frame):

    def __init__(self, master):
        """initialize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        """create a button which displays clicks"""
        self.lable = Label(self, text="Click Count:")
        self.lable.grid()

        self.lable2 = Label(self, text=self.bttn_clicks)
        self.lable2.grid()

        self.bttn = Button(self)
        self.bttn["text"] = "add"
        self.bttn["command"] = self.add_count
        self.bttn.grid()

        self.bttn2 = Button(self)
        self.bttn2["text"] = "subtract"
        self.bttn2["command"]=self.sub_count
        self.bttn2.grid()

        self.bttn3 = Button(self)
        self.bttn3["text"]="multiply"
        self.bttn3["command"]=self.mul_count
        self.bttn3.grid()

        self.bttn4 = Button(self)
        self.bttn4["text"] = "divide"
        self.bttn4["command"] = self.div_count
        self.bttn4.grid()

    def add_count(self):
        self.bttn_clicks += 1
        self.lable2["text"] = str(self.bttn_clicks)

    def sub_count(self):
        self.bttn_clicks -= 1
        self.lable2["text"] = str(self.bttn_clicks)

    def mul_count(self):
        self.bttn_clicks= self.bttn_clicks*2515664
        self.lable2["text"] = str(self.bttn_clicks)

    def div_count(self):
        self.bttn_clicks= self.bttn_clicks/2
        self.lable2["text"] = str(self.bttn_clicks)

root = Tk()
root.title("Click Counter")
root.geometry("200x200")
app = Application(root)
root.mainloop()