import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0

for i in range(trials):
	birthdays = []

	for i in range(people):
		bday = random.randrange(days)
		birthdays.append(bday)

	if len(birthdays) != len(set(birthdays)):
		matches += 1

print((matches / trials) * 100)
