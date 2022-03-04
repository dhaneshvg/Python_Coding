dic = {"apple": 200, "orange": 250, "banana": 800, "sbargilly": 420}
print(dic)
# for i in dic:
#     print(i)

# for i in dic.keys():
#     print(i)

# for i in dic.values():
#     print(i)

for i in dic.items():
    print(i)

dic["apple"] = 800
print(dic)
del dic["banana"]
print(dic)