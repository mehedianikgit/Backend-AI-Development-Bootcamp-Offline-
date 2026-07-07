import math

a = 5
b = 3
c = 2
d = 16
e = 10

X = ((((a+b)**2 - math.sqrt(d) * c) / 4) + ((e**2 - a * c) + math.sqrt(b-1)) - ((a-c) * (b+2)) + (math.sqrt(a**2 + d)/2))**3

print(X)