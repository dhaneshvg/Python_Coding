# Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.

# x = lambda x: x * (x + 5) ** 2
# print(x(5))


def multiply():
    return lambda x: x * (x + 5) ** 2


num1 = multiply()
print(num1(5))
