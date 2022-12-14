import numpy as np
import matplotlib.pyplot as plt
import time

# INPUT
target = 25     # value to find the square root of

# INITIALIZATON SETTINGS
g = 1         # initial guess

conv = 0.001    # convergence criteria (run progra until we're this
                #  close to the target)

# INITIAL TEST
test = g * g    # square the guess to see if it is the same as the target
diff = abs(test-target) # the difference between the target and the test
i = 0           # itteraton 

# SET UP FOR OUTPUT FOR EACH ITERATION
x = []          # make array for iteration number
y = []
x.append(i)     # add initial values to data array for graphing
y.append(g)
print (i, ":", g, test, diff)   # print output to screen

while (diff > conv):    # run while the difference is greater than our convergence criteria 
    i += 1
    g = (g + target/g)/2
    test = g * g
    diff = abs(test-target) # check how close to the target we are

    # gather output data for this iteration
    x.append(i)
    y.append(g)
    print (i, ":", g, test, diff)

# DRAW GRAPH
fig, ax = plt.subplots()    # initialize matplotlib plot
ax.plot(x, y)               # put data into plot
plt.show()                  # show the plot