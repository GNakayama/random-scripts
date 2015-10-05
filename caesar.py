import substitution


def encrypt(key, msg):
	return substitution.encrypt(key, msg) 

def decrypt(key, cipher):
	return substitution.decrypt(key, cipher) 

def gen_key(n):
	key = {}

	for i in xrange(26):
		key[chr(65 + i)] = chr((i + n)%26 + 65)

	return key
