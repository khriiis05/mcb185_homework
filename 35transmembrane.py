import sys

kd = {
	'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5,
	'M': 1.9, 'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
    'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5,
    'N': -3.5, 'K': -3.9, 'R': -4.5
}
    
def avg_kd(seq):
	return sum(kd[aa] for aa in seq) /len(seq)
	
def has_signal_peptide(seq):
	region = seq[:30]
	for i in range(len(region) - 8 + 1):
		window = region[i:i+8]
		if 'P' in window: continue
		if avg_kd(window) >= 2.5:
	return False
	
def has_transmembrane(seq):
	region = seq[30:]
	for i in range(len(region) - 11 + 1):
		window = region[i:i+11]
		if 'P' in window: continue
		if avg_kd(window) >= 2.0:
			return True
	return False
	
name = None
seq = []

for line in sys.stdin:
	line = line.rstrip()
	
	if line.startswith('>'):
		if name:
			protein = ''.join(seq)
			if has_signal_peptide(protein) and has_transmembrane(protein):
				print(name)
		name = line[1:]
		seq = []
	else: seq.append(line)
	
if name:
	protein = ''.join(seq)
	if has_signal_peptide(protein) and hastransmembrane(protein):
		print(name)