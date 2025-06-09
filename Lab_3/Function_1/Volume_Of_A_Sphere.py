import math
def Volume_Of_A_Sphere(r):
    volume = (4/3) * math.pi * r ** 3
    return f"Volume of a Sphere with a {r} radius = {volume}\n"
print(Volume_Of_A_Sphere(5))