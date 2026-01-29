import random

def d20():
	return random.randint(1, 20)

def dnd_normal(dc):
	roll = d20()
	return roll >= dc

def dnd_advantage(dc):
	roll = max(d20(), d20())
	return roll >= dc

def dnd_disadvantage(dc):
	roll = min(d20(), d20())
	return roll >= dc

def sim(dc, trials = 1000):
	normal = 0
	advantage = 0
	disadvantage = 0
	for i in range(trials):
		if dnd_normal(dc):
			normal += 1
		if dnd_advantage(dc):
			advantage += 1
		if dnd_disadvantage(dc):
			disadvantage += 1
	print('Normal:', normal / trials)
	print('Advantage:', advantage / trials)
	print('Disadvantage:', disadvantage / trials)
	print()

for dc in [5, 10, 15]:
	sim(dc)
