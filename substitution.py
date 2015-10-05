def encrypt(key, msg):
	cipher = ""

	for letter in msg:	
		if letter in key:
			cipher += key[letter]
		else:
			cipher += letter

	return cipher

def decrypt(key, cipher):
	msg = ""
	inv_key = {v: k for k, v in key.items()}

	for letter in cipher:
		if letter in inv_key:
			msg += inv_key[letter]
		else:
			msg += ' '
	return msg
