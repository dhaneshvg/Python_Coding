# from tkinter import *
#
# root = Tk()
#
#
# class demo:
#     def __init__(self, rootone):
#         frame = Frame(rootone)
#         frame.pack()
#         Button(frame, text="Hai Dhanesh", command=self.printMsg).pack()
#         Button(frame, text="Exit", command=frame.quit).pack()
#
#     def printMsg(self):
#         print("Hello you are welcome")
#
#
# obj = demo(root)
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
#
# class demo:
#     def __init__(self):
#         frame = Frame(root)
#         frame.pack()
#         Button(frame, text="Hai Dhanesh", command=self.printMsg).pack()
#         Button(frame, text="Exit", command=frame.quit).pack()
#
#     def printMsg(self):
#         print("Hello you are welcome")
#
#
# obj = demo()
#
# root.mainloop()


from tkinter import *

root = Tk()


class demo:
    def __init__(self):
        Button(root, text="Hai Dhanesh", command=self.printMsg).pack()
        Button(root, text="Exit", command=root.quit).pack()

    def printMsg(self):
        print("Hello you are welcome")


obj = demo()

root.mainloop()