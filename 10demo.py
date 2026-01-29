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
	return 3 % ((1/x) + (1/y) + (1/z))
print(har_mean(8, 7, 3))

def distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance(3, 2, 5, 6))


#Strings
s = 'hello world'
print(s, type(s))

#Conditionals
##if
a = 2
b = 4
if a == b:
	print('a equals b')
print(a,b)

def is_even(x):
	if x % 2 == 0: return True
	return False
print(is_even(2))
print(is_even(3))

##Boolean
c = a == b
print(c)
print(type(c))

##if-elif-else
if a < b:	print('a < b')
elif a > b :	print('a > b')
else:		print('a == b')

if a < b:	print('a < b')
elif a <= b:	print('a <= b')
elif a == b:	print('this will never print')

##Boolean Chains
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('this is illogical')
if not False: print(True)

##Floating Point Warning
a = 0.3
b = 0.1 * 3
if a < b:	print('a < b')
elif a > b:	print('a > b')
else: 		print('a == b')

print(abs(a-b))
if abs(a - b) < 1e-9: print('close enough')
if math.isclose(a, b): print('close enough')

##String Comparison
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

a = 1
s = 'G'
#if a < s: print('a < s') results in "Type Error"

#None Type
## i.e. program with no 'return' function
def silly(m, x, b):
	y = m * x + b
print(silly(2, 3, 4))

#Function Practice
def is_integer(x):
	r = x % 1
	if math.isclose(0, r): return True
	else: return False
print(is_integer(3.0))

def is_prob(p):
	if 0 <= p <= 1: return True
	else: return False
print('10', is_prob(10))
print('0.6', is_prob(0.6))

def dna_weight(letter):
	if letter == 'A': return 313.2
	if letter == 'C': return 289.2
	if letter == 'G': return 329.2
	if letter == 'T': return 304.2
	else: return None
print(dna_weight('A'))
print(dna_weight('G'))
print(dna_weight('S'))

def dna_compliment(letter):
	if letter == 'A': return 'T'
	if letter == 'T': return 'A'
	if letter == 'C': return 'G'
	if letter == 'G': return 'C'
	else: return None
print(dna_compliment('A'))
print(dna_compliment('T'))
print(dna_compliment('G'))
print(dna_compliment('S'))	 

def max_number(a, b, c):
	if a > b and a > c: return a
	if b > a and b > c: return b
	if c > a and c > b: return c
	else: return 'More than one max'
print(max_number(10, 16, 3))
print(max_number(10, 8, 9))
print(max_number(10, 4, 29))
print(max_number(10, 10, 9))
print(max_number(10, 10, 10))

#while
i = 0
while True:
        i = i + 1
        print('hey', i)
        if i == 3: break

i = 0
while i < 3:
        i = i + 1 
        print('hey', i)

i = 1
while i < 10:
        print(i)   
        i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)

for i in range(0, 5, 1): print(i)

#Nesting
for i in range(7):
	if i % 2 == 0:	print(i, 'is even')
	else: 		print(i, 'is odd')

#Iteration Practice Problems
def triangular(n):
	tri = 0
	for i in range(n + 1):
		tri = tri + i
	return tri
print(triangular(10))

def factorial(n):
	fact = 1
	for i in range(1, n + 1):
		fact = fact * i
	return fact
print(factorial(0))
#Still works despite 'if n == 0: return 1' being missing

def poisson(n, k):
	return n**k * math.e**(-n) / factorial(k)
print(poisson(20, 15))

def nchoosek(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))
print(nchoosek(20, 15))

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e
print(euler(10))

def is_prime(n):
	for i in range(2, n//2):
		if n % i == 0: return False
	return True
print(is_prime(11))
print(is_prime(10))

def nilakantha(limit):
	pi = 3
	for i in range(1, limit + 1):
		n = 2 * i
		d = n * (n + 1) * (n + 1)
		if i % 2 == 0: pi = pi - 4 / d
		else: pi = pi + 4 / d
	return pi
print(nilakantha(10))

#Random Numbers
import random

for i in range(5):
	print(random.random())

for i in range(3):
	print(random.randint(1, 6))

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

#More Iteration Practice

#inside = 0
#total = 0
#while True:
       #x = random.random()
       #y = random.random()
       #distance = math.sqrt(x**2 + y**2)
       #total += 1
       #if distance <= 1:
               #inside += 1
       #pi = 4 * (inside / total)
       #print(pi)

def d6():
	return random.randint(1, 6)

def dnd_3d6():
	return d6() + d6() + d6()
print(dnd_3d6())

def dnd_3d6r1():
	total = 0
	for i in range(3):
		roll = d6()
		while roll == 1:
			roll = d6()
		total += roll
	return total
print(dnd_3d6r1())

def dnd_3d6x2():
	total = 0
	for i in range(3):
		total += max(d6(), d6())
	return total
print(dnd_3d6x2())
