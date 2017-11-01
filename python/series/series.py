def slices(number, n):
	if n > len(number) or n == 0:
		raise ValueError
	res = []
	for i, j in enumerate(number):
		if i+n > len(number):
			return res
		res.append([])
		for k, l in enumerate(number[i:i+n]):
			res[-1].append(int(l))
	return res


#print(slices('01234', 1))
#print(slices('97867564', 2))
#print(slices('97867564', 3))