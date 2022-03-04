#lambda is an anomulus funtion which is not defined and syntax is lambda argument:expression can be done in one statement.

def multiply(n):
    return lambda a: a * n


num1 = multiply(6)
print(num1(2))

num2 = multiply(5)
print(num2(2))