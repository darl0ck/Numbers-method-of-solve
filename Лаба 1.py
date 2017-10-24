# -*- coding: utf-8 -*- 
import math

i = 10
r = 0.3
p = math.pi ** 2 / 6

def sum1():
	s1 = 0
	for n in range(1, 20000000):
		s1 += n * (n - r) / ((n ** 2 + r) ** 2)
	print(f'{s1:.{i}f}')

sum1()


def sum2():
	s2 = 0
	p = math.pi ** 2 / 6
	for n in range(1, 2000):  # 2500
		s2 += n * (n - r) / ((n ** 2 + r) ** 2) - 1 / (n ** 2)
	s2 += p
	print(f'{s2:.{i}f}')

sum2()

def sum3():
	s3 = 0
	for n in range(1, 237):
		s3 += n * (n - r) / ((n ** 2 + r) ** 2) - 1 / (n ** 2) + (r / n ** 3)
	s3 += p - (1.2020569032 * r)
	print(f'{s3:.{i}f}')

sum3()
