import os
with open("sometext.txt", "r") as f:
    data = f.readlines()
print("Number of lines:", len(data))