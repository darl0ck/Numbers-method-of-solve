# coding=utf-8

import math

import matplotlib.pyplot as plt
from matplotlib import mlab

n=int(input('n='))

# начальные условия
x0 = 0
y0 = 0.5
# шаг
# отрезок [x0, xn], где x0 = 0, xn = 1
xn = 1
h = ((xn-x0)/n)
print(h)
f = lambda x, y: -20*y**2 * (x-0.4)
f_2= lambda x, y: 20*y**2 -800 *y**3*(x-0.4)**2

ilist = mlab.frange(0, n, 1)
xlist = [(x0 + h * i) for i in ilist]
ylist = []

prev = y0
print("euler")
for x in xlist:
    y = prev + h * f(x, prev)
    prev = y
    ylist.append(prev)
    print(y)

# массив со значениями точного решения
lst = []
print("\nSolver",)
for x in xlist:
    func = 1/(10*x**2-8*x+2) # точное решение
    lst.append(func)
    print(func)


# массив со значениями метода Тейлора 2го порядка

teylor = []
prev2 = y0
print("Тейлор",)
for x in xlist:
    y2 = 1/(10*x**2-8*x+2)+h*f(x,prev2)+h**2*f_2(x,prev2) # точное решение
    prev2 = y2
    teylor.append(prev2)
    print(y2)


s3 = [5./12, -4./3, 23./12]

adams=[]
def adams_bashforth(f, ta, tb, xa, n, sn=s3):
    print('adams')
    last_n = []
    h = (tb - ta) / float(n)
    t = ta
    x = xa
    # first n steps made by Euler method
    for i in range(len(sn)):
        last_n.append(h * f(t, x))
        x += last_n[-1]
        t += h
    # Adams-Bashforth method
    for i in range(n+1):
        x += h * sum([last_n[i] * sn[i] for i in range(len(sn))])
        last_n = last_n[1:]
        last_n.append(f(t, x))
        t += h
        adams.append(x)
    return adams

print(adams_bashforth(f, 0, 1, y0, n))

print(adams)

plt.rc('font', **{'family': 'verdana'})
plt.xlabel("abciss")
plt.ylabel("ordinat")
plt.plot(xlist, ylist, "b-", label=" euler")
plt.plot(xlist, lst, "g-", label=" first solve")
plt.plot(xlist, adams, "y-", label="adams")
plt.plot(xlist, teylor, "r-", label=" teylor")

plt.legend()
plt.grid()
plt.show()