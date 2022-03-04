class a:
    def __init__(self, name, hodName):
        self.name = name
        self.hodName = hodName

    def getData(self):
        self.name = input("Enter Student Name:")


class b(a):
    def putData(self):
        self.hodName = input("Enter HOD Name:")

    def display(self):
        print("Student Name is: ", self.name, "/n""HOD Name is: ", self.hodName)


class c(b):
    def fun3(self):
        print("Displaying Method/ Function in class C")


class d(c):
    def fun4(self):
        print("Displaying Mmethod/Function in class D")


objc = d("", "")
objc.getData()
objc.putData()
objc.display()
objc.fun3()
objc.fun4()
