def distance(fromDNA, toDNA):
	c = 0
	if len(fromDNA) != len(toDNA):
		raise ValueError(fromDNA, toDNA)
	for i in range(len(fromDNA)):
			if fromDNA[i] != toDNA[i]:
				c += 1
	
	return c