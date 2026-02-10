import sys
import math

#python3 22stats.py x y z...

vals = [float(x) for x in sys.argv[1:]]

def mean(vals):
	total = 0
	for val in vals:
		total += val
	return total / len(vals)

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini:
			mini = val
		if val > maxi:
			maxi = val
	return mini, maxi

def median(vals):
	vals.sort()
	n = len(vals)
	if n % 2 == 1:
		return vals[n // 2]
	else:
		return (vals[n // 2 - 1] + vals[n // 2]) / 2

def std_dev(vals):
	m = mean(vals)
	total = 0
	for val in vals:
		total += (val - m)**2
	return math.sqrt(total / len(vals))

mini, maxi = minmax(vals)

print('Count:', len(vals))
print('Min:', mini)
print('Max:', maxi)
print('Mean:', mean(vals))
print('Standard deviation:', std_dev(vals))
print('Median:', median(vals))
