def sum_digits(n):
	result = 0

	n = int(n)

	while n > 0:
		result += n%10
		n //= 10
	
	return result
