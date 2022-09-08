from cmath import pi
h = float(input("hight"))
r = float(input("radius"))

vS = (pi*r**2) * h

if vS > 1000:
    print(f"Bigger {vS}")
else:
    print (f"Smaller {vS}")

