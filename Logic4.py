d = input("What size drink do you want.") #function and method 

d = d.lower().strip().replace(" ", "")
#d = d.strip() #only beggining or end of the word.
#d = d.replace(" ", "")


if d == "venti" :
    print("your fat")
elif d == "tall":
    print("Your still fat")
elif d == "grande":
    print("cool")
else:
    print("everthing else")
