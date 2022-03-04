w = int(input("Enter the Height in Kg:"))
h = float(input("Enter the Weight in Cm:"))
h = h / 100


def bmi(a, b):
    c = b / a**2
    print(c)


bmi(h, w)
