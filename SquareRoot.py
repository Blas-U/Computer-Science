import matplotlib.pyplot as pit 
#target = 25
#g = 2
#test = g*g
#g = (g + (target/g))/2   #each time its ran is an iteration
#test = g*g
#g = (g + (target/g))/2
#test = g*g
#g = (g + (target/g))/2
#print(g)
target = 25
g = 2
offset = .001
diff = 1
while diff > offset:
    g= (g+(target/g))/2
    test = g*g
    diff = abs(target - test)
print(g)
