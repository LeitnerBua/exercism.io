def sieve(number):
	primes = []
	for i in range(2, number+1):
		isPrime = True
		for j in range(2, i):
			if j != i and i % j == 0:
					isPrime = False
		if isPrime:
			primes.append(i)
	return primes
