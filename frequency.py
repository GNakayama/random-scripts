import operator


def frequency_count(c, n):
	c =  c.replace(" ", "")

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

def display_table(freq):
	print '_____________'

	
	sorted_freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)

	for f in sorted_freq:
		print '| ' + f[0] + ' | %.4f |' % f[1]
	
