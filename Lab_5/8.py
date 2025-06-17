import re
with open("row.txt") as f:
    data = f.read()
print("Task 8")
print(re.findall(r"[A-Z][^A-Z]*", data))