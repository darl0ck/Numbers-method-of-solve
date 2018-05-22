import math
import matplotlib.pyplot as plt
from matplotlib import mlab
import numpy as np

a = 0
b = 1

N = int(input('введите N '))



xKosh = []
yKosh = []
h = (b - a) / N
t = np.arange(a, b + h, h)


def exact(x1):
    return np.exp(x1) + np.exp(-x1) + 2.9 * x1 ** 2 - 2.9 * x1 - 2


def koshi(N):
    n = N
    h = (b - a) / N
    ilist = np.arange(0, n, 1)

    xlist = [(a + h * i) for i in ilist]

    x = [0 for z in range(n + 1)]
    y = [0 for z in range(n + 1)]
    l = [0 for z in range(n + 3)]
    m = [0 for z in range(n + 3)]

    l[1] = 0
    m[1] = 0
    x[0] = 0
    for i in range(1,N):
        x[i] = x[i - 1] + h

        l[i + 1] = 1 / (-l[i] + 2 + h * h)

        m[i + 1] = (m[i] - h * h * (7.8 + 2.9 * x[i] * (1 - x[i]))) / (-l[i] + 2 + h * h)


    x[N] = b

    y[N] = (m[n] + (2 * math.exp(1) + 0.9) * h) / (1 + h - l[n])

    i = N
    while i > 1:
        y[i - 1] = l[i] * y[i] + m[i]
        i -= 1
    y[0] = l[1] * y[1] + m[1]

    for i in range(N):
        i += 1

    print(y)
    plt.plot(x, y, "r-", label=" progonka")


def Teylor_m(y0, z0, h):
    global x2,y2

    x2 = [0 for z in range(N + 1)]
    y2 = [0 for e in range(N + 1)]
    z = [0 for w in range(N + 1)]

    y2[0] = y0
    x2[0] = a
    z[0] = z0

    for j in range(N):
        x2[j + 1] = x2[j] + h

        y2[j + 1] = y2[j] + z[j] * h

        z[j + 1] = z[j] + h * (y2[j] + 7.8 + 2.9 * x2[j] - 2.9 * x2[j] * x2[j]) + h * h / 2 * (
                2.9 - 5.8 * x2[j] + y2[j] + 7.8 + 2.9 * x2[j] - 2.9 * x2[j] * x2[j]) + (h * h * h / 6) * (-5.8 + 2.9 - 5.8 * x2[j] + y2[j] + 7.8 + 2.9 * x2[j] - 2.9 * x2[j] * x2[j])


    return y2[N]+z[N]


def Teylor_m_print(y0, z0, h):

    x2 = [0 for z in range(N + 1)]
    y2 = [0 for e in range(N + 1)]
    z = [0 for w in range(N + 1)]

    print(z0)
    y2[0] = y0
    x2[0] = a
    z[0] = z0

    for j in range(N):
        x2[j + 1] = x2[j] + h

        y2[j + 1] = y2[j] + z[j] * h

        z[j + 1] = z[j] + h * (y2[j] + 7.8 + 2.9 * x2[j] - 2.9 * x2[j] * x2[j]) + h * h / 2 * (
                2.9 - 5.8 * x2[j] + y2[j] + 7.8 + 2.9 * x2[j] - 2.9 * x2[j] * x2[j]) + (h * h * h / 6) * (
                           -5.8 + 2.9 - 5.8 * x2[j] + y2[j] + 7.8 + 2.9 * x2[j] - 2.9 * x2[j] * x2[j])

    plt.plot(x2, y2, "g-", label=" Teylor_m")


def F(m, h):
    return Teylor_m(0, m, h) - 2 * np.exp(1) - 0.9


def mm_1():
    mm = [0 for z in range(N+1)]
    mm[2] = 2
    mm[1] = 1
    m=0
    for i in range(2,N):
        mm[i + 1] = mm[i] - (F(mm[i], h)) * (mm[i] - mm[1]) / (F(mm[i], h) - F(mm[1], h))
        if abs(mm[i + 1] - mm[i]) > 0.0001:
            m = mm[i + 1]
    return m


koshi(N)

Teylor_m_print(0, mm_1(), h)


plt.rc('font', **{'family': 'verdana'})
plt.xlabel("abciss")
plt.ylabel("ordinat")
plt.plot(t, exact(t), "b-", label=" exact")

plt.legend()
plt.grid()
plt.show()
