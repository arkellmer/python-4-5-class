from tkinter import *

class Application(Frame):

    """ a gui that lets you check a movie"""
    def __init__(self, master):

        """initialize frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        """creates a label for the name/instructions"""
        Label(self, text="Choose your favorite movie types").grid(row=0, column=0, sticky=W)

        """creates check boxes"""
        Label(self,
              text="Select all that apply:")\
            .grid(row=1, column=0, sticky=W)

        """makes check boxes"""
        """self.likes_comedy = BooleanVar()
        Checkbutton(self, text="Comedy", variable=self.likes_comedy, command=self.update_text)\
            .grid(row=2, column=0, sticky=W)

        self.likes_drama = BooleanVar()
        Checkbutton(self, text="Drama", variable=self.likes_drama, command=self.update_text)\
            .grid(row=3, column=0, sticky=W)

        self.likes_romance = BooleanVar()
        Checkbutton(self, text="Romance", variable=self.likes_romance, command=self.update_text)\
            .grid(row=4, column=0, sticky=W)"""

        """makes a radio button"""
        self.favorite = StringVar()
        self.favorite.set(None)

        """create a comeday radio button"""
        Radiobutton(self, text="Comedy", variable = self.favorite, value="comedy.", command = self.update_text)\
            .grid(row=2, column=0, sticky=W)

        Radiobutton(self, text="Drama", variable=self.favorite, value="drama.", command=self.update_text) \
            .grid(row=3, column=0, sticky=W)

        Radiobutton(self, text="Romance", variable=self.favorite, value="romance.", command=self.update_text) \
            .grid(row=4, column=0, sticky=W)

        """create text field to display results"""
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """update text widget to display favorite movies"""
        message = "Your favorite type of movie is "
        message += self.favorite.get()

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)


        # likes = ""
        # if self.likes_comedy.get():
        #     likes+="You like comedic movies.\n"
        #
        # if self.likes_drama.get():
        #     likes+="You like dramatic movies.\n"
        #
        # if self.likes_romance.get():
        #     likes+="You like romantic movies.\n"
        #
        # self.results_txt.delete(0.0, END)
        # self.results_txt.insert(0.0, likes)

root = Tk()
root.title("Movie Picker")
root.geometry("300x200")
app = Application(root)
root.mainloop()


