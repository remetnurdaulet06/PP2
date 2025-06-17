import math
import time
time_milliseconds = int(input("Enter milliseconds: "))
value = int(input("Enter number: "))
time.sleep(time_milliseconds / 1000)
print(f"Square root of {value} after {time_milliseconds} milliseconds is {result}")