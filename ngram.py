#!/usr/bin/env python
from random import normalvariate #Just for generating numbers for testing functions
from math import log,e
from fractions import Fraction

use_fractions = True

def dict_sum(d):
	s = 0
	for k in d.keys():
		s += d[k]
	return s

def ngram(n, words):
	"""Return a list of n (1 .. n)-gram dictionaries, n >= 1, l[0] is {}, where
	the keys are tuples of words"""
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

def n_c(n,c,ngrams):
	sorted(ngrams[n].values())
	#For a particular value c of the above line
	#count the number of different ngrams with that value c
	#This can be done more fancy-like and all-at-once by checking for unique values (http://www.google.com/search?client=ubuntu&channel=fs&q=unique+python&ie=utf-8&oe=utf-8)

def good_turing(ngrams):
	for n in range(1,len(ngrams)-1):
		counts=(ngrams[n].values())
		#counts is the number of times each n-gram occurs
		#For each unique count c (http://www.google.com/search?client=ubuntu&channel=fs&q=unique+python&ie=utf-8&oe=utf-8),
		#c_ = (c+1)*n_c(n,c+1)/n_c(n,c)
		#Do what I mean by this ngrams[n].values()=counts
	return ngrams

def probabilities(ngrams):
	totals = [dict_sum(x) for x in ngrams]
	probabilities = {}
	ngram = ngrams[-1]
	prevgram = ngrams[-2]
	for k in ngram.keys():
		num = ngram[k]
		if len (ngrams) > 2:
			denom = prevgrams[k[0:-1]]
		else:
			denom = totals[1]
		import code
		code.interact(local=locals())
		print "num: %s, denom: %s" % (num, denom)
		if use_fractions:
			probabilities[k] = Fraction(num, denom)
		else:
			probabilities[k] = log(num) - log(denom)
	return probabilities
	

#Small things that we need to add at some point
def p_log(W):
	return 0.00023

def perplexity_log(W):
	#W = w_1 w_2 ... w_N
	#PP (W) = P (w1 w2 .. wN) ^ -1/N
	N=len(W)
	PP=(-1/N)*p_log(W)
	return PP


#ngram.good_turing(ngram.ngram(3,filters.unk(filters.shakespeare('Shakespeare/short.txt'))))
