t = ("apple", "orange", "banana", "carrot")
print(t)
print(type(t))
# print(t[1])
# # t[3]= "beatroot"
# # t[1]= "cabbage"
# print(t[-1])
# print(t[3])

n = list(t)
n[1] = "new"
print(type(n))
m = tuple(n)
print(n)
print(type(m))

if "apple" in m:
    print("yes apple is  available")
