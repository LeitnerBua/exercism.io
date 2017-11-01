def to_rna(rna):
	res = ''
	dicDNAtoRNA = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'U'}
	for char in rna:
		if char in dicDNAtoRNA.keys():
			res += dicDNAtoRNA[char]
		else:
			return ''
	return res