#!/usr/bin/env python
from random import normalvariate #Just for generating numbers for testing functions
from math import log,e

def ngram(n, words):
	"""Return a list of n (1 .. n)-gram dictionaries, n >= 1, l[0] is {}."""
	ngrams = [{}]
	for i in range(1, n+1):
		d = {}
		# compute the i-gram model data
		word_buffer = words[0:i-1]
		for word in words[i-1:]:
			word_buffer.append(word)
			t = tuple(word_buffer)
			if d.has_key(t):
				d[t] += 1
			else:
				d[t] = 1
			word_buffer.pop(0)
		ngrams.append(d)
	return ngrams


#Small things that we need to add at some point
def smooth_addone(ngrams):
	return ngrams

def C(ngram):
	#Return the count of a particular n-gram somehow
	return normalvariate(0.25,0.05)

def p_log(W):
	return 0.00023

def perplexity_log(W)
	#W = w_1 w_2 ... w_N
	#PP (W) = P (w1 w2 .. wN) ^ -1/N
	N=len(W)
	PP=(-1/N)*p_log(W)
	return PP
