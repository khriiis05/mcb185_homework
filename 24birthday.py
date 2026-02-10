import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0

for i in range(trials):
	calendar = [0] * days
	shared = False

	for i in range(people):
		bday = random.randrange(days)
		calendar[bday] += 1

		if calendar[bday] >= 2:
			shared = True
			break

	if shared:
		matches += 1

percent = (matches / trials) * 100

print('Percentage of shared bdays:', percent)
