import math
from scipy.misc import *

a = 0
b = 1
step = 0
eps = 0.5*10**-4
c = (a+b)/2
i = 5


def f(x):
	return 1.4 * math.cos(x) - math.exp(x)


def derivF(x):
	return derivative(f, x)


def deriv2F(x):
	return derivative(derivF,x)


def mpd(a, b, c, eps, step):
	while (abs(a-b) >= eps and f(c)!=0):
		step += 1
		if f(a) * f(c) < 0:
			b = c
		elif f(b) * f(c) < 0:
			a = c
		c = (a + b) / 2
	print('Метод Дифотомии: за '+str(step)+' шагов', 'был получен корень ' + f'{c:.{i}f}' + ' c точностью до ' + str(i) +' знака после запятой')


mpd(a, b, c, eps, step)


def chooseX(a,b):
	if (deriv2F(a) * f(a)>0):
			v = a
	elif (deriv2F(b) * f(b)>0):
			v = b
	else:
		v = c
	return v


chooseX(a,b)


def modOfNewton(a,b,step):
	x0 = chooseX(a,b)
	x = x0
	z = deriv2F(x0)
	y = x - f(x) / z
	while (abs(y-x)>=eps):
		c = y - f(y) / z
		x = y
		y = c
		step +=1
	print('Модиф.метод Ньютона: за '+str(step)+' шагов', 'был получен корень ' + f'{c:.{i}f}' + ' c точностью до ' + str(i) +' знака после запятой')


modOfNewton(a,b,step)


def mpi(a,b,step):
	x0 = chooseX(a,b)
	x = x0
	p = 2/(-1-3.9)
	x1 = x - p*f(x)
	while (abs(x1-x)>eps):
		x = x1
		step += 1
		x1 = x - p * f(x)
	print('МПИ: за '+str(step)+' шагов', 'был получен корень ' + f'{x:.{i}f}' + ' c точностью до ' + str(i) +' знака после запятой ')


mpi(a,b,step)
