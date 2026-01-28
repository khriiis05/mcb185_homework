import math

def char_to_prob(q):
	Q = ord(q) - 33
	if Q < 0: return None
	return 10**(-Q/10)
print(char_to_prob('A'))


def prob_to_char(p):
	if p <= 0 or p >= 1: return None
	return chr(round(-10 * math.log10(p)) + 33)
print(prob_to_char(0.001))
	
