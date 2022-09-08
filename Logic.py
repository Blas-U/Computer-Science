n = input("Enter your name")

len = len(n)

if len < 6:
    print(f"{n} your name is short.")
else:
    print(f"Your name sucks {n}. It has {len} letters")

print(len)