def encrypt(msg, key):
	cipher = ""	

	for letter in msg:
		if letter in key:
			cipher += key[letter]
		else:
			cipher += letter

	return cipher

def decrypt(cipher, key):
	msg = ""

	inverse_key = {v: k for k, v in key.items()}

	for letter in cipher:
		if letter in inverse_key:
			msg += inverse_key[letter]
		else:
			msg += letter

	return msg

def gen_key(n):
	key = {}

	for i in xrange(26):
		key[chr(65 + i)] = chr((i + n)%26 + 65)

	return key
