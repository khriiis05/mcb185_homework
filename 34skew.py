#gc_comp()
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	

#gc_skew()
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)
	

#More Efficient Method(?)
import sys
import sequence

w = 1000

seq = ''
for line in sys.stdin:
	if line.startswith('>'): continue
	seq += line.strip()
	
window = seq[0:w]
c = window.count('C')
g = window.count('G')

gc_comp = (c + g) / w
gc_skew = 0 if (c + g) == 0 else (g - c) / (g + c)
print(0, gc_comp, gc_skew)

for i in range(1, len(seq) - w + 1):
	
	left = seq[i - 1]
	right = seq[i + w - 1]
	
	if left == 'C': c -= 1
	if left == 'G': g -= 1
	
	if right == 'C': c += 1
	if right == 'G': g += 1
	
	gc_comp = (c + g) / w
	gc_skew = 0 if (c + g) == 0 else (g - c) / (g + c)
	
	print(i, gc_comp, gc_skew)