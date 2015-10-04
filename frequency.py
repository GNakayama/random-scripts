def frequency_count(c, n):
	c =  c.strip()

	total = len(c) - (n - 1)
	freq = {}
	
	for k in xrange(total):
		word = c[k: (k + n)]
		if word in freq:
			freq[word] += 1
		else:
			freq[word] = 1

	for f in freq:
		freq[f] = float(freq[f])/total		

	return freq
