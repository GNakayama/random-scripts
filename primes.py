import math

def is_prime(n):
	if n <= 0:
		return False

	if n <= 2:
		return True

	root = int(math.sqrt(n)) + 1

	for i in xrange(2, root):
		if n%i == 0:
			return False

	return True
