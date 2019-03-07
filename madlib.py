#simple gui
#demonstrates creating a window

from tkinter import *

#create the root window
root = Tk()
#modify the window
root.title("Simple GUI")
root.geometry("999x666")
root.configure(bg = "green")
# changes icon #root.wm_iconbitmap("")

# creates a frame in hte window to hold other widgets
app = Frame(root)
app.grid()

#creates a label in the frame
label = Label(app, text = "this is a fancy Label")
label.config(bg = "purple")
label.config(fg = "purple")

lbl = Label(app, text = "i'm a label")
lbl.config(font=("",55))

lbl3 = Label(app, text = "this is another label")
lbl3.config(font=("roman"))

#displays labels
lbl3.grid()
label.grid()
lbl.grid()



#kick off the windows event-loop
root.mainloop()




