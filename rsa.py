import math


def get_pq(n):
	r = math.sqrt(n)
	p = 0
	q = 0

	for i in xrange(2, int(math.ceil(r + 1))):
		if n%i == 0:
			p = i
			break
	
	if not p == 0:
		q = n/p

		return (p, q)
	
	return None

def get_inverse(a, m):
	x = 0
	r = m
	newx = 1
	newr = a

	while not newr == 0:
		q = r//newr
		(x, newx) = (newx, x - q*newx)
		(r, newr) = (newr, r - q*newr)

	if r > 1:
		return None

	if x < 0:
		inv = x + m
	else:
		inv = x
		
	return inv


def apply_exp(msg, e, m):
	index = 1
	cipher = msg

	if e == 1:
		return cipher%m

	while (index + index) <= e:
		cipher *= cipher
		cipher %= m
		index += index
	else:
		if (e - index) > 1:
			cipher *= apply_exp(msg, e - index, m)
		else:
			cipher *= msg
	return cipher%m


def convert_26(msg):
	a = msg%26

	msg -= a
	msg /=26

	b = msg%26

	msg -= b

	c = msg/26

	return  str(unichr(c + 65)) + str(unichr(b + 65)) + str(unichr(a + 65))
