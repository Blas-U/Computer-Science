f1=1  #initialization 
f2 = 1
for i in range(2,31):
    fnew = f1 + f2
    print(fnew)
    f1 = f2    #Update section.
    f2 = fnew
