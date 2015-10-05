def calc_ic(cipher, n):
	cipher = cipher.replace(' ', '')
	result = []
	matrix =  calc_matrix(cipher, n)

	for line in matrix:
		result.append(ic(line))

	return result

def calc_mg(cipher, n):
	cipher = cipher.replace(' ', '')
	result = []
	matrix = calc_matrix(cipher, n)

	for line in matrix:
		result.append(mg(line))

	return result

def calc_matrix(cipher, n):
	cipher = cipher.replace(' ', '')
	matrix = ['']*n
	
	if n == 1:
		matrix[0] = cipher
	else:
		for i in range(0, len(cipher), n):
			for t in xrange(n):
				if (i + t) < len(cipher):
					matrix[t] += cipher[i + t]

	return matrix

def ic(line):
	sum = 0
	n = len(line)
	f =  freq(line)

	for i in xrange(26):
		sum += float(f[i]*(f[i] - 1))/(n*(n - 1))

	return sum

def freq(line):
	total = len(line)
	result = [0]*26

	for l in line:
		result[ord(l) - 65] += 1

	return result


def mg(line):
	p = [.082, .015, .028, .043, .127, .022, .02, .061, .07, .002, 0.008, .04, .024, .067, .075, .019, 0.01, .060, .063, .091, .028, .010, .023, .001, .02, .001]
	result = [0]*26
	n = len(line)	

	f = freq(line)

	for i in xrange(26):
		f[i] /= float(n)
		

	for g in xrange(26):
		for j in xrange(26):
			result[g] += float(p[j]*f[(j + g)%26])
	
	return result


def decrypt(key, cipher):
	msg = ''
	index = 0
	n = len(key)
	
	for letter in cipher:
		if not letter == ' ':
			a = ord(letter) - 65
			msg += chr((a - (ord(key[index%n]) - 65))%26 + 65)
			index += 1
		else:
			msg += ' '
	return msg

def encrypt(key, msg):
	cipher = ''
	index = 0
	n = len(key)
	
	for letter in cipher:
		if not letter == ' ':
			a = ord(letter) - 65
			msg += chr((a + (ord(key[index%n]) - 65))%26 + 65)
			index += 1
		else:
			msg += ' '

