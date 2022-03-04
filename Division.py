x = int(input("Enter a dividend:"))
y = int(input("Enter the divisor:"))


def divide(a, b):
    try:
        c = a / b
        print(c)
    except:
        print("Please enter the divisor is greater than Zero")


divide(x, y)
