import re
with open("row.txt") as f:
    data = f.read()
matches=re.sub(r"[A-Z]",'_',data)
print(matches)