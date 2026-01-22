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
