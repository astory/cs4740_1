#!/usr/bin/env python
import ngram
import filters
import csv
import random

ngram.good_turing =lambda x:x

def trial(train,n,p,probs):
	"""n is n-gram size. p is whether it's log, arbitrary precision or float"""
	#Start timer
	sentence=ngram.make_sentence(probs[0:(n+1)])
	pp=ngram.perplexity(probs[0:(n+1)],sentence)
	#End timer
	time='NA'
	return [n,p,pp,time,' '.join(sentence)]

def sentence_generation(train,filename,nmax,reps,probs):
	out=csv.writer(open(filename, 'wb'), delimiter='|', quotechar='&', quoting=csv.QUOTE_NONE)
	out.writerow(['n','use fractions','perplexity','time','sentence'])
	for i in range(0,nmax*reps):
		n=random.randint(1,nmax)
		#ngram.use_fractions=random.randint(0,1)
		ngram.use_fractions=True
		out.writerow(trial(train,n,ngram.use_fractions,probs))
		ngram.use_fractions=False
		out.writerow(trial(train,n,ngram.use_fractions,probs))

def main():
	nmax=3
	reps=3
	#train='Shakespeare/short.txt'
	train='War and Peace/short.txt'
	out='results.csv'
	#TODO(tom) This isn't working. I'll fix it later.
	probs=ngram.probabilities(ngram.good_turing(ngram.ngram(nmax,filters.unk(filters.shakespeare(train)))))
	sentence_generation(train,out,nmax,reps,probs)
