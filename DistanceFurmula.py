from vpython import *

sphere()
def f2(x):
    q = 2*(x)**2 + 3*x + 4
    return q

x3 = 1
x4 = 5

y4 = f2(x4)
y3 = f2(x3)

dx2 = x4 - x3
dy2 = y4 - y3

distance2 = (dx2**2 + dy2**2)**.5
#distance between two points given two x-values and a function

def f1(x):
    y = 2*x + 3
    return y


#function

#calculate distance

#distance = (dx**2 + dy**2)**.5

#inputs
x1 = 1
x2 = 5
#function
y2 = f1(x2)
y1 = f1(x1)
#calculate distance
dx = x2 - x1
dy = y2 - y1
#distance = (dx**2 + dy**2)**.5
#slope
m = dy / dx

#d = (((x2 -x1) ** 2) + ((y2 - y1) ** 2))**.5
#print(d)
#print(distance)
print(m)
print(distance2)