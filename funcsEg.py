from tkinter import Y


def q1(x):
    y = 2*x**2 + x - 2
    return y

x = 5 
print( q1(x) )
#loop

#for i in range(5):
#    x = input("Enter a number: ")
#    n = float(x)
#    print(x)
#    print( q1(n) )

doAgain = True

while doAgain:
    x = input("ender a number: ")
    if x == "stop":
        doAgain = False
        print("stop")
    else:
        n = float(x)
        print( q1(n) )