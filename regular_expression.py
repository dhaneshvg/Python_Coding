import re

# pattern = r"dhanesh"
# if re.match(pattern, "dhanesh Hai How are you"):
#     print("Matched")
# else:
#     print("Not matched")

# pattern = r"dhanesh"
# if re.match(pattern, "Hai dhanesh How are you"):
#     print("Matched")
# else:
#     print("Not matched")

# pattern = r"dhanesh"
# if re.search(pattern, "Hai dhanesh How are you"):
#     print("Matched")
# else:
#     print("Not matched")

# patt = r"dhanesh"
# print(re.findall(patt, "dhanesh Hai dhanesh How are youdhanesh hope you are fine dhanesh"))

print(re.findall("dhanesh", "dhanesh Hai dhanesh How are youdhanesh hope you are fine dhanesh"))
