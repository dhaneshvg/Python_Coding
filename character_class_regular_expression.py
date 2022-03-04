import re

# pattern = r"[A-Z][a-z][0-9]"
# if re.search(pattern, "At3"):
#     print("Correct pattern format ")
# else:
#     print("Not correct pattern format")

pattern = r"[0-9][a-z][A-Z]"
if re.search(pattern, "At3"):
    print("Correct pattern format ")
else:
    print("Not correct pattern format")
