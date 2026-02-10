import sys

alphabet = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

print(' ', end = '')
for column in alphabet:
	print(f'{column}', end = '')
print()

for i in range(len(alphabet)):
	print(alphabet[i], end = '')

	for j in range(len(alphabet)):
		if alphabet[i] == alphabet[j]:
			print(f'{match}', end = '')
		else: print(f'{mismatch}', end = '')
	print()
