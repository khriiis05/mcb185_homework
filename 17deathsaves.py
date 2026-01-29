import random

def death_save():
	success = 0
	fail = 0
	while True:
		roll = random.randint(1, 20)
		if roll == 1:
			fail += 2
		elif roll == 20:
			return 'revived'
		elif roll < 10:
			fail += 1
		else:
			success += 1
		if fail >= 3:
			return 'died'
		if success >= 3:
			return 'stable'

def sim(trials = 1000):
	died = 0
	stable = 0
	revived = 0
	for i in range(trials):
		result = death_save()
		if result == 'died':
			died += 1
		elif result == 'stable':
			stable += 1
		else:
			revived += 1
	print('Died:', died / trials)
	print('Stable:', stable / trials)
	print('Revived:', revived / trials)
sim()
