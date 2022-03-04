# Write Python code which accepts name of a product and in turn returns their respective prices.

dic = {}
ch = 'y'
while ch == 'y' or ch == 'Y':
    name = input("Enter name of product : ")
    price = eval(input("Enter the price of product : "))
    dic[name] = price
    ch = input("Want to add more items (Y/N) : ")
for i in dic.items():
    print(i)
