#!/usr/bin/env python
import argparse as ap
import copy
import gmpy
import mpmath as mp
from math import log,e,exp
import filters
import gmpy
import math
import random

#K for good-turing
K=5

def set_fractions(fractions):
	global use_fractions
	use_fractions = fractions

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

def get_n_c(ngrams):
	n_c = [{}]
	for n in range(1,len(ngrams)):
		counts=(ngrams[n].values())
		#counts is the number of times each n-gram occurs
		d = {}
		for count in counts:
			if d.has_key(count):
				d[count] += 1
			else:
				d[count] = 1
		n_c.append(d)
	return n_c

def good_turing(ngrams):
	#Get the number of n-grams with a particular count c
	#Smooth the counts
	#c_ = (c+1)*n_c(n,c+1)/n_c(n,c)
	#Put this in a dictionary in the format of ngrams
	ngrams_smoothed=[{}]
	n_c=get_n_c(ngrams)
	for n in range(1,len(ngrams)):
		ngrams_smoothed.append({})
		for gram in ngrams[n].keys():
			c=ngrams[n][gram]
			if c > K:
				c_ = c
			elif n_c[n].has_key(c+1):
				nc1=n_c[n][c+1]
				n1 =n_c[n][1]
				nc =n_c[n][c]
				nk1=n_c[n][K+1]
				c_ = ((c+1.0)*nc1/nc-c*(K+1)*nk1/n1)/(1-(K+1)*nk1/n1) #Page 137
			else:
				c_ = c
			ngrams_smoothed[n][gram]=c_
	return ngrams_smoothed

def perplexity(probs, words):
	global use_fractions
	print "perplexity use_fractions: %s" % use_fractions
	n = len(probs) - 1
	if use_fractions:
		prob = gmpy.mpq(1,1)
	else:
		prob = 0
	word_list = []
	i = 0
	for w in words:
		i += 1
		if i % 10000 == 0:
			print "processing word %d" % i
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
	global use_fractions
	print "probabilities use_fractions: %s" % use_fractions
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
	if l == []:
		return filters.UNK
	if l[0][1]<=0:
		l = [(t, exp(p)) for (t,p) in l]
	total_prob = 0
	for (t,v) in l:
		total_prob += v
	n = random.uniform(0,total_prob)
	for item, weight in l:
		if n <= weight:
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
		prob_list = [(x) for x in probs[len(word_buffer)+1].items()\
				if x[0][0:-1] == tuple(word_buffer)]
		ngram = choose_prob(prob_list)
		if ngram==None:
			print 'n-gram is none'
		w = ngram[-1]
		word_list.append(w)
		word_buffer.append(w)
		if len(word_buffer) == n:
			word_buffer.pop(0)
		print " ".join(word_list)
		if w == filters.SOS:
			break
	return word_list

def main():
	parser = ap.ArgumentParser(description='Play with some ngrams')
	parser.add_argument('-n', '--n-gram', metavar='N', type=int,
		dest='n', action='store', default=3,
		help='n-gram to compute')
	parser.add_argument('-t', '--train', metavar='FILE', type=file,
		dest='training', action='store', default='Shakespeare/Train.txt',
		help='Train ngrams from this file')
	parser.add_argument('-p', '--perplexity', metavar='FILE', type=file,
		dest='perplexity', action='store', default=None, help='measure'+
		' perplexity against this file')
	parser.add_argument('-l', '--logs', dest='use_logs', action='store_true',
		help='compute using logs, default is arbitrary-precision')
	parser.add_argument('-s', '--smooth', dest='smooth', action='store_true',
		help='smooth using Good-Turing smoothing')
	parser.add_argument('-m', '--make-sentence', dest='make_sentence',
	action='store_true', help='produce a sentence')
	args = parser.parse_args()
	if not args.make_sentence and args.perplexity is None:
		parser.print_help()
		exit()
	global use_fractions
	use_fractions = not args.use_logs

	print "main use_fractions: %s" % use_fractions

	words = filters.shakespeare(args.training)

	if args.perplexity is not None:
		unked_words = filters.unk(words)
		unked_ng = ngram(args.n, unked_words)
		if args.smooth:
			unked_ng = good_turing(unked_ng)
		unked_probs = probabilities(unked_ng)
	else:
		ng = ngram(args.n, words)
		if args.smooth:
			ng = good_turing(ng)
		probs = probabilities(ng)

	if args.perplexity is not None:
		print "this might take a while..."
		perplex_data = filters.unk(filters.shakespeare(args.perplexity))
		print "Perplexity: %s" % perplexity(unked_probs, perplex_data)

	if args.make_sentence:
		print " ".join(make_sentence(probs))

if __name__ == "__main__":
	main()
