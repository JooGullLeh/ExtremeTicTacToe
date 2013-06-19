from Tkinter import *
#must separately import messagebox because of the way tkinter is designed
from Tkinter import messagebox

class Application (Frame):
    def __init__(self, masterWindow):
        #initialize parent object
        super().__init__(masterWindow)
        #call parent function
        self.grid()
        #call fn to set up widgets (this is a new fn)
        self.createWidgets()

    def createWidgets(self):

        self.btn = Button(self, text="Warning")
        self.btn["command"] = self.showWarningBox
        self.btn.grid(row=0, column=0)

        self.btn2 = Button(self, text="Info")
        self.btn2["command"] = self.showInfoBox
        self.btn2.grid(row=0, column=1)

        self.btn3 = Button(self, text="Error")
        self.btn3["command"] = self.showErrorBox
        self.btn3.grid(row=0, column=2)

        self.btn4 = Button(self, text="Ok / Cancel")
        self.btn4["command"] = self.showOkCancelBox
        self.btn4.grid(row=1, column=0)

        self.entry = Entry(self)
        self.entry.grid(row=2, column=0, columnspan=3)


    def showWarningBox(self):
        messagebox.showwarning("Invalid Move", "Beware")

    def showInfoBox(self):
        messagebox.showinfo("Message", "Today is Thursday")

    def showErrorBox(self):
        messagebox.showerror("Error", "You can't do that")

    def showOkCancelBox(self):
        if messagebox.askokcancel("Question", "This will delete the text"):
            self.entry.delete(0,END)

def main():
    root = Tk()
    root.title("Welcome")
    root.geometry("300x300")

    app = Application(root)

    root.mainloop()

main()


__author__ = 'BYH'
