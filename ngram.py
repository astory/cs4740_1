#!/usr/bin/env python
from fractions import Fraction
from math import log,e
import random
from random import normalvariate #Just for generating numbers for testing functions
import filters

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

def perplexity(probs, words):
	n = len(probs) - 1
	if use_fractions:
		prob = Fraction(1,1)
	else:
		prob = 0
	word_list = []
	for w in words:
		word_list.append(w)
		if len(word_list) > n:
			word_list.pop(0)
		if use_fractions:
			# TODO(astory): unk
			prob *= probs[len(word_list)][tuple(word_list)]
		else:
			# word list is already log in this case
			prob += probs[len(word_list)][tuple(word_list)]
	if use_fractions:
		return prob
	else:
		return exp(prob)

def probabilities(ngrams):
	totals = [dict_sum(x) for x in ngrams]
	probabilities = []

	prevgram = None
	for ngram in ngrams:
		d = {}
		for k in ngram.keys():
			prefix = k[0:-1]
			numer = ngram[k]
			if prefix in prevgram:
				# more than unigram
				denom = prevgram[prefix]
			else:
				denom = totals[1]
			if use_fractions:
				d[k] = Fraction(numer, denom)
			else:
				d[k] = log(numer) - log(denom)
		probabilities.append(d)
		prevgram = ngram
	return probabilities

def choose_prob(l):
	n = random.uniform(0,1)
	for item, weight in l:
		if n < weight:
			return item
		n -= weight

def make_sentence(probs):
	n = len(probs) - 1
	if n > 1:
		word_list = [filters.SOS]
	else:
		word_list = []
	word_buffer = list(word_list)
	while(True):
		# TODO(astory): unk
		print "word_buffer: %s" % word_buffer
		prob_list = [(x) for x in probs[len(word_buffer)+1].items()\
				if x[0][0:-1] == tuple(word_buffer)]
		ngram = choose_prob(prob_list)
		import code
		#code.interact(local = locals())
		print "ngram: %s" % (", ".join(ngram))
		w = ngram[-1]
		word_list.append(w)
		word_buffer.append(w)
		if len(word_buffer) == n:
			word_buffer.pop(0)
		if w == filters.SOS:
			break
	return word_list

#Small things that we need to add at some point
def smooth_addone(ngrams):
	return ngrams

def C(ngram):
	#Return the count of a particular n-gram somehow
	return normalvariate(0.25,0.05)

def p_log(W):
	return 0.00023

def perplexity_log(W):
	#W = w_1 w_2 ... w_N
	#PP (W) = P (w1 w2 .. wN) ^ -1/N
	N=len(W)
	PP=(-1/N)*p_log(W)
	return PP
