import math
from matplotlib import pyplot as plt

#########################
# 1D Diffusion equation #
#########################

L = 50
X = list(range(-L, L+1))
P = [0 for i in X]
P[L] = 1

D = 0.5
delta_t = 0.1

legend = []

times = [0, 10, 100, 1000, 10000]

for t in range(10001):
    if t in times:
        plt.plot(X, P)
        legend.append("t = " + str(t))
    dP = [0 for i in X]
    for i in range(1, len(X)-1):
        dP[i] = ((P[i-1] + P[i+1] - 2*P[i]) * D * delta_t)
    for i in range(1, len(X) - 1):
        P[i] += dP[i]

plt.xlabel("x")
plt.ylabel("P(x,t)")
plt.legend(legend)
plt.savefig("1d-diffusion.png")


#########################
# 2D Diffusion equation #
#########################

def diffuse2d(Dx, Dy):
    L = 20

    X = [0 for i in range(-L, L+1)]
    P = [[0 for i in range(-L, L+1)] for j in range(-L, L+1)]
    P[L][L] = 1

    delta_t = 0.1

    times = [0, 10, 100, 1000, 10000]

    ticks = [i for i in range(2*L + 1) if i % 10 == 0]
    labels = [i for i in range(-1 * L, L + 1) if i % 10 == 0]

    for t in range(10001):
        if t in times:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            cax = ax.matshow(P, interpolation='none', cmap='hot')
            fig.colorbar(cax)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title(f"P(x,y,t) at t={t}")
            plt.xticks(ticks, labels)
            plt.yticks(ticks, labels)
            plt.savefig("2d-diffusion-Dx"+str(Dx) +
                        "-Dy"+str(Dy)+"-n"+str(t)+".png")
        dP = [[0 for i in range(-L, L+1)] for j in range(-L, L+1)]
        for i in range(1, len(X)-1):
            for j in range(1, len(X)-1):
                dP[i][j] = ((P[i-1][j] + P[i+1][j] - 2*P[i][j]) * Dy * delta_t) + \
                    ((P[i][j-1] + P[i][j+1] - 2*P[i][j]) * Dx * delta_t)
        for i in range(1, len(X)-1):
            for j in range(1, len(X)-1):
                P[i][j] += dP[i][j]


# Case I: Dx = Dy
diffuse2d(0.5, 0.5)

# Case II: Dx > Dy
diffuse2d(0.5, 0.1)

# Case III: Dy > Dx
diffuse2d(0.1, 0.5)
