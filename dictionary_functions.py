# dict1 = {
#     1: "apple",
#     2: "orange",
#     3: "banana",
#     4: 1996
# }
# print(dict1)
# print(dict1.get(4))
# print(dict1.get(7, "key not found"))
# dict1[1] = "carrot"
# print(dict1)


# dict2 = {
#     "a": "apple",
#     "b": "ball",
#     "c": "cat",
#     "d": 1993
# }
# for x in dict2:
#     print(dict2[x])
#     print(x)

dict3 = {
    1: "apple",
    2: "ball",
    3: "cat"
}
# if 5 in dict3:
#     print("Available")
# else:
#     print("Not Available")
# print(len(dict3))
#
dict3[4] = "dog"
# print(dict3)
# print(dict3[4])

# dict3.pop(3)
# print(dict3)
print(dict3)
# dict3.popitem()
# print(dict3)
# del dict3[1]
# print(dict3)

dict4 = dict3.copy()
print(dict4)
mydic = dict(dict3)
print(mydic)
