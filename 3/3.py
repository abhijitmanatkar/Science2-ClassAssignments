import math
from matplotlib import pyplot as plt

k = 1
m = 1

legend = []


def hamilton_path(H):
    x = 0
    p = math.sqrt(2*m*H)

    t = []
    X = []
    P = []

    num_steps = 10000
    delta = 0.001

    for i in range(num_steps):
        t.append(i)
        X.append(x)
        P.append(p)
        delta_x = (p / m) * delta
        delta_p = ((-1) * k * x) * delta
        x += delta_x
        p += delta_p

    return (t, X, P)


# Plotting phase space trajectory
legend = []
for H in range(0, 10):
    t, X, P = hamilton_path(H)
    plt.plot(X, P)
    legend.append("H = " + str(H))
plt.xlabel("position")
plt.ylabel("momentum")
plt.legend(legend)
plt.savefig("phase-space.png")

# Plotting mean square displacement
plt.clf()
legend = []
for H in range(0, 5):
    t, X, P = hamilton_path(H)
    X2 = [x*x for x in X]
    plt.plot(t, X2)
    legend.append("H = " + str(H))

plt.xlabel("time")
plt.ylabel("Mean square displacement")
plt.legend(legend)

plt.savefig("mean-sq-displacement.png")
