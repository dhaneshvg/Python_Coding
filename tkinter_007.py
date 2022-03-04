# window with file menus
from tkinter import *

root = Tk()

def fun():
    print("Function Activated")

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="save", command=fun)
submenu.add_separator()
submenu.add_command(label="Exit",command=root.quit)

newmenu = Menu(mymenu)

mymenu.add_cascade(label="Edit", menu=newmenu)
newmenu.add_command(label="Undo")
newmenu.add_command(label="Redo")

freshmenu= Menu(mymenu)

mymenu.add_cascade(label="Window", menu=freshmenu)
freshmenu.add_command(label="Filter")
freshmenu.add_command(label="Adjust")

root.mainloop()
