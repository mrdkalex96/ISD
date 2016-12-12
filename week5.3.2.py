import math
x = int(input("Insert a integer for x "))
y = int(input("Insert a integer for y "))
if 1+ x > x ** math.sqrt(2):
    y=y+x
    print(x)
    print(y)
else:
    print(y)
