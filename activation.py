import numpy as np
from matplotlib import pyplot as plt



X = np.linspace(-8., 8., 256, endpoint=True)


def sigmoid(z):
    s = 1.0 / (1.0 + np.exp(-1.0 * z))
    return s

def rel(z):
	return max(z, 0.)


rel_v = np.vectorize(rel)

Y_sigmoid = sigmoid(X)
Y_tanh = np.tanh(X)
Y_rel = rel_v(X)



plt.plot(X, Y_rel)

plt.ylim(-1.0, 1.0)

plt.savefig("rel.png", dpi=72)
