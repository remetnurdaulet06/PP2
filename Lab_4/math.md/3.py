import math
n=int(input())
a=int(input())
area = (n * a**2) / (4 * math.tan(math.pi / n))
print(area)