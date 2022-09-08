#x1 = 2
#y1 = 4
#x2 = 3
#y2 = 5

#slope = (y2 - y1)/(x2 - x1)
#print(slope)

x1 = float(input("x1 ="))
y1 = float(input("y1 ="))
x2 = float(input("x2 ="))
y2 = float(input("y2 ="))


slope = (y2 - y1)/(x2 - x1)
xInter = -(y1/slope) + x1
b = y1 - (slope * x1)

print(f'slope = {slope}')
print(f'xInter = {xInter}')
print(f'b = {b}')