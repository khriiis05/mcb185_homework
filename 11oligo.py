def oligo_melt(A, C, G, T):
	total = A + T + G + C
	if total <= 13: return (A + T)*2 + (G + C)*4
	if total > 13: return 64.9 + 41*(G + C - 16.4)/(A + T + G + C)

print(oligo_melt(5, 7, 3, 4))
print(oligo_melt(1, 2, 1, 4))
