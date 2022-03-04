class computer:
    def __init__(self, ram, drivespace, motherboard, processor, displaysize, refreshrate):
        self.ram = ram
        self.drivespace = drivespace
        self.motherboard = motherboard
        self.processor = processor
        self.diplaysize = displaysize
        self.refeshrate = refreshrate

    def getSpecs(self):
        print("Ram:", self.ram)
        print("Drive Space:", self.drivespace)
        print("Motherboard Manufacturer:", self.motherboard)
        print("Processor:", self.processor)

    def displaySpecs(self):
        print("Display Size:", self.diplaysize)
        print("Refesh rate:", self.refeshrate)


class desktop(computer):
    def connetivity(self):
        print("Desktop can connect Multiple drives")

    def cost(self):
        print("Desktop is cheaper")


class laptop(computer):
    def weight(self):
        print("Weight of the Laptop = 800grams")


obj = laptop("4GB", "1TB", "Asus", "Intel", "15 inch", "25Hz")
print("\n","Laptop Specs")
obj.getSpecs()
obj.displaySpecs()
obj.weight()

print("\n","Desktop Specs")
obje = desktop("2GB", "500GB", "Gigabyte", "AMD", "24 inch", "30Hz")
obje.getSpecs()
obje.displaySpecs()
obje.cost()
obje.connetivity()
