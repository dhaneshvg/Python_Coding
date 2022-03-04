from tkinter import *

root = Tk()
frame1 = Frame(root)
frame1.pack()


def fun():
    print("Hai Dhanesh")


def cancel():
    print("Cancelled")


Button(frame1, text="Login", bg="red", fg="white", command=fun).pack()
Button(frame1, text="Cancel", bg="blue", fg="white", command=cancel).pack()
root.mainloop()
