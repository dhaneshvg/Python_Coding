class student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def getData(self):
        self.name = input("Enter the Name:")
        self.mark = input("Enter the Mark:")

    def showData(self):
        print(self.name, "\n", self.mark)


obj = student("", "")
obj.getData()
obj.showData()
