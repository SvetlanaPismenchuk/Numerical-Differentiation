import numpy as np
import time

def dydx(f, x0, h=0.01):
    return (f(x0 + h) - f(x0 - h)) / (2*h)

def g(x):
    return 3*x**4 - 3*x**2 + 12*x

x = np.linspace(0, 1, 10000001)

start = time.time()

gprime_loop = [0]*len(x)
for i in range(len(x)):
    gprime_loop[i] = dydx(g, x[i])

end = time.time()
print("Loop time:", end - start)

start = time.time()

gprime_vec = dydx(g, x)

end = time.time()
print("Vectorized time:", end - start)

input()
