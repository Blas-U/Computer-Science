n = float(input("Number divisible by three or not"))

d = n % 3

if d != 0:
    print(f"{n} is not divisible by 3")
else:
    print(f"{n} is divisible by 3")


