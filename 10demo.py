# 10demo.py by Khristina Lopez

import math

print('hello, again') # greeting

# Numbers
print(1.5e-2)

# Math Operators
print(1 + 3)
print(4 - 2)
print(198 * 278)
print(55044 / 278)
print(2 ** 4)
print(5 // 2)
print(5 % 2)
print(5 * (2 + 2))

# Math Functions
print(abs(-7))
print(pow(2,3))
print(round(0.789, ndigits=2))
print(math.ceil(576.87))
print(math.floor(576.87))
print(math.log(4))
print(math.log2(4))
print(math.log10(4))
print(math.sqrt(25))
print(math.pow(2, 3))
print(math.factorial(6))
print(math.e)
print(math.pi)
print(math.inf)
print(math.nan)

# Numbers Aren't Real
print(0.1 * 1)
print(0.1 * 3)

#Variables
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)
print(type(a), type (b), type(c), sep='', end='!\n')

#Functions
def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
print(pythagoras(3,4))

#Function Practice
def circle_area(r):
	return math.pi * r**2
print(circle_area(4))

def rectangle_area(w, h):
	return w * h
print(rectangle_area(6, 7))

def triangle_area(w, h):
	return rectangle_area(w, h) / 2
print(triangle_area(6, 7))

def fah_to_cel(fah):
	return (fah - 32) * 5/9
print(fah_to_cel(99))

def cel_to_fah(cel):
	return (cel * 9/5) + 32
print(cel_to_fah(37))

def mph_to_kph(mph):
	return mph * 1.609
print(mph_to_kph(79))

def DNA(OD260):
	return OD260 * 50
print(DNA(0.8))

def arith_mean(x, y, z):
	return (x + y + z) / 3
print(arith_mean(10, 15, 20))

def geo_mean(x, y, z):
	return (x * y * z)**(1/3)
print(geo_mean(3, 6, 12))

def har_mean(x, y, z):
	return 3 / ((1 / x) + (1 / y) + (1 / z))
print(har_mean(8, 7, 3))

def distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance(3, 2, 5, 6))
