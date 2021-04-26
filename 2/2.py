import random
import math
from matplotlib import pyplot as plt

def pi_calc(num_iters):
    num_in_circle = 0
    for i in range(num_iters):
        x = random.random()
        y = random.random()
        if (x*x + y*y < 1): num_in_circle += 1
    
    return 4 * num_in_circle/num_iters

def pi_plot():
    X = []
    Y = []
    for i in range(1,1000):
        X.append(i)
        Y.append(pi_calc(i))
    plt.plot(X, Y)
    plt.xlabel("Number of simulations")
    plt.ylabel("Calculated value of pi")
    #plt.show()
    plt.savefig("PIvN.png")

if __name__ == '__main__':
    pi_plot()