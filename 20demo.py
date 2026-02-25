#Strings
s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')


#Method Syntax
print(s.upper())
print(s)

print(s.replace('o', '')) #erases all o's and replaces them with nothing
print(s.replace('o', '').replace('r', 'i')) #erases all o's + replace 'r' w/ 'i'


#String Formatting

import math

print(f'{math.pi}')
print(f'{math.pi:.3f}')		#3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')	#exponent notation
print(f'{"hello world":>20}')	#right justify w/ space filler
print(f'{"hello world":.>20}')	#right justify w/ dot filler
print(f'{20:<10} {10}')		#left justify

print('{} {:.3f}'.format('str.format', math.pi))	#str.format()
print('%s %.3f' % ('printf', math.pi)) 			#printf


#Indexes
seq = 'GAATTC'
print(seq[0], seq[1])	#1st and 2nd letters of sequence
print(seq[-1])		#Final letter of sequence

for nt in seq:
	print(nt, end = '')
print()

for i in range(len(seq)):
	print(i, seq[i])


#Slices
s = 'ABCDEFGHIJ'
print(s[0:5])		#First 5 letters of a string

print(s[0:8:2])		#First 8 letters of string, jumping in twos

print(s[0:5], s[:5])		#both ABCDE
print(s[5:len(s)], s[5:])	#both FGHIJ

print(s, s[::], s[::1], s[::-1])	#All same except last (reversed string)

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)


#Tuples
tax = ('Homo', 'sapiens', 9606)
print(tax)

#s[0] = 'C'
#tax[0] = 'human'

print(tax[0])
print(tax[::-1])


#enumerate() and zip()
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):	#Preferred method of index and value
	print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):	#Preferred method of element retrieval
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)


#Lists
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

#nts.copy()

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alph)
aas = list(alph)
print(aas)

text = 'good day           to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)


#Searching
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))


#Practice Problems
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

def min_max(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy([0.2, 0.3, 0.5]))

def kl_distance(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(kl_distance(p1, p2))


#External Data
line = input('type something and hit return: ')
print('that line was', len(line), 'characters long')

import sys
print(sys.argv)

i = int('42')
x = float('0.61803')
print(i * x)

x = float('howdy')


#Pairwise Comparison
##for i in range(0, len(list)):
	##for j in range(x, len(list)):
## X = 0
## X = i 
## X = i+1
