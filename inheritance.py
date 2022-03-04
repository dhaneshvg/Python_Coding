class student:
    def __init__(self, name):
        self.name = name

    def getData(self):
        self.name = input("Enter Student Name:")


class hod(student):
    def __init__(self, hodName):
        self.hodName = hodName

    def putData(self):
        self.hodName = input("Enter HOD Name:")

    def dispaly(self):
        print("Student name is: ", self.name, "\n", "HOD name is: ", self.hodName)


obj = hod("")
obj.getData()
obj.putData()
obj.dispaly()
