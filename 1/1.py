import random
import math
from matplotlib import pyplot as plt

def random_walk(num_steps):
    x = 0
    for i in range(num_steps):
        if (random.random() < 0.5):
            x += 1
        else:
            x -= 1
    return x

def prob2_sim(num_steps, num_iters=5000):
    '''
    Probability of 2 drunkards meeting after num_steps steps calculated by simulation
    '''
    num_meet = 0
    for i in range(num_iters):
        x1 = random_walk(num_steps)
        x2 = random_walk(num_steps)
        if x1 == x2: num_meet += 1
    
    return num_meet/num_iters

def prob2_ana(num_steps):
    '''
    Probability of 2 drunkards meeting after num_steps steps calculated analytically
    '''
    return math.comb(2*num_steps, num_steps) * (0.5**(2*num_steps))

def prob_origin_sim(num_steps, num_iters=5000):
    '''
    Probability of a drunkard being at origin after num_steps calculated by simulation
    '''
    num_at_0 = 0
    for i in range(num_iters):
        x = random_walk(num_steps)
        if x == 0: num_at_0 += 1
    
    return num_at_0/num_iters  

def prob_origin_ana(num_steps):
    '''
    Probability of a drunkard being at origin after num_steps calculated analytically
    '''
    if num_steps % 2 == 1:
        return 0
    else:
        return math.comb(num_steps, num_steps//2) * (0.5**num_steps)

def mean_disp_sim(num_steps, num_iters=10000):
    x = 0
    for i in range(num_iters):
        x += random_walk(num_steps)
    return x/num_iters

def mean_square_disp_sim(num_steps, num_iters=5000):
    x = 0
    for i in range(num_iters):
        x += (random_walk(num_steps))**2
    return x/num_iters

def two_drunk_sim():
    X = []
    Ysim = []
    Yana = []
    for i in range(100):
        X.append(i)
        Ysim.append(prob2_sim(i))
        Yana.append(prob2_ana(i))
    plt.clf()
    plt.plot(X, Ysim)
    plt.plot(X, Yana)
    plt.legend(["simulated", "analytical"])
    plt.xlabel("No. of steps")
    plt.ylabel("Probability of meeting")
    #plt.show()
    plt.savefig("p_meeting.png")

def one_drunk_sim():
    X = []
    Ysim = []
    Yana = []
    for i in range(100):
        X.append(i)
        Ysim.append(prob_origin_sim(i))
        Yana.append(prob_origin_ana(i))
    plt.clf()
    plt.plot(X, Ysim)
    plt.plot(X, Yana, ":")
    plt.legend(["simulated", "analytical"])
    plt.xlabel("No. of steps")
    plt.ylabel("Probability of being at origin")
    #plt.show()
    plt.savefig("p_origin.png")

def mean_disp():
    X = []
    Ysim = []
    Yana = []
    for i in range(100):
        X.append(i)
        Ysim.append(mean_disp_sim(i))
        Yana.append(0)
    plt.clf()
    plt.plot(X, Ysim)
    plt.plot(X, Yana)
    plt.legend(["simulated", "analytical"])
    plt.xlabel("No. of steps")
    plt.ylabel("Mean displacement")
    #plt.show()
    plt.savefig("mean_displacement.png")
    
def mean_square_disp():
    X = []
    Ysim = []
    Yana = []
    for i in range(100):
        X.append(i)
        Ysim.append(mean_square_disp_sim(i))
        Yana.append(i)
    plt.clf()
    plt.plot(X, Ysim)
    plt.plot(X, Yana)
    plt.legend(["simulated", "analytical"])
    plt.xlabel("No. of steps")
    plt.ylabel("Mean square displacement")
    #plt.show()
    plt.savefig("meansq_displacement.png")

if __name__ == '__main__':
    two_drunk_sim()
    one_drunk_sim()
    mean_disp()
    mean_square_disp()