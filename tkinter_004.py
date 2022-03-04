from tkinter import *
root = Tk()

Label(root,text="X direction",bg="red").pack(fill=X)
Label(root,text="Y direction",bg="blue").pack(side=LEFT,fill=Y)

root.mainloop()