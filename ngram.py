#!/usr/bin/env python
import gmpy
import mpmath as mp
from fractions import Fraction
from math import log,e
import math
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
		temp_words = list(word_list)
		while(True):
			if tuple(temp_words) in probs[len(temp_words)]:
				if use_fractions:
					prob *= probs[len(temp_words)][tuple(temp_words)]
				else:
					prob += probs[len(temp_words)][tuple(temp_words)]
				break
			else:
				unk_gram = list(temp_words[:-1])
				unk_gram.append(filters.UNK)
				if tuple(unk_gram) in probs[len(unk_gram)]:
					if use_fractions:
						prob *= probs[len(unk_gram)][tuple(unk_gram)]
					else:
						prob += probs[len(unk_gram)][tuple(unk_gram)]
					break
				else:
					temp_words.pop(0)
	if use_fractions:
		return mp.power((mp.mpf(prob.denom())/mp.mpf(prob.numer())), 1.0/len(words))
	else:
		return math.exp(-prob/len(words))

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
				d[k] = gmpy.mpq(numer, denom)
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
		prob_list = [(x) for x in probs[len(word_buffer)+1].items()\
				if x[0][0:-1] == tuple(word_buffer)]
		ngram = choose_prob(prob_list)
		w = ngram[-1]
		word_list.append(w)
		word_buffer.append(w)
		if len(word_buffer) == n:
			word_buffer.pop(0)
		if w == filters.SOS:
			break
	return word_list

#Small things that we need to add at some point
def p_log(W):
	return 0.00023

def perplexity_log(W):
	#W = w_1 w_2 ... w_N
	#PP (W) = P (w1 w2 .. wN) ^ -1/N
	N=len(W)
	PP=(-1/N)*p_log(W)
	return PP


#ngram.make_sentence(ngram.probabilities(ngram.good_turing(ngram.ngram(3,filters.unk(filters.shakespeare('Shakespeare/short.txt'))))))
