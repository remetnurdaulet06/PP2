import re
with open("row.txt") as f:
    data=f.read()
print(re.findall(r"[A-Z][a-z]*", data))