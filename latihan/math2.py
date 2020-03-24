import numpy as np

# intergral


def integrate(f, a, b, N):
    x = np.linspace(a, b, N)
    fx = f(x)
    area = np.sum(fx)*(b-a)/N
    return area


def integrate1(f, a, b, N):
    x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = f(x)
    area = np.sum(fx)*(b-a)/N
    return area


print(integrate(np.sin, 0, np.pi/2, 100))
print(integrate1(np.sin, 0, np.pi/2, 100))
