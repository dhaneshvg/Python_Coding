from tkinter import *
import tkinter.messagebox

root = Tk()

# tkinter.messagebox.showinfo("Title", "This is a Info")
# tkinter.messagebox.showerror("Title", "This is an Error")
# tkinter.messagebox.showwarning("Title", "This is a Warning")
# tkinter.messagebox.askquestion("Title", "This is a Question")
# tkinter.messagebox.askokcancel("Title", "This is a OK Cancel")
tkinter.messagebox.askretrycancel("Title", "This is a Retry Cancel")

root.mainloop()
