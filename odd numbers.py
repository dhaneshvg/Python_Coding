# List out  all the odd numbers from 1 to 100 using lists in Python

odd = []
for i in range(100):
    if i % 2 != 0:
        odd.append(i)
print(odd)

# odd = [i for i in range(100) if i % 2 != 0]
# print(odd)
