#!/usr/bin/env python
import ngram
import filters
import csv
import random

ngram.good_turing =lambda x:x

def trial(train,n,probs,p='ap'):
	"""n is n-gram size. p is whether it's log, arbitrary precision or float"""
	#Start timer
	#import code
	#code.interact(local=locals())
	sentence=ngram.make_sentence(probs[0:(n+1)])
	pp=ngram.perplexity(probs[0:(n+1)],sentence)
	#End timer
	time=42
	return [n,p,pp,time,sentence]

def sentence_generation(train,filename,nmax,reps,probs):
	out=csv.writer(open(filename, 'wb'), delimiter='|', quotechar='&', quoting=csv.QUOTE_NONE)
	for i in range(0,nmax*reps):
		n=random.randint(1,nmax)
		out.writerow(trial(train,n,probs))

def main():
	nmax=3
	reps=3
	train='Shakespeare/short.txt'
	out='results.csv'
	#TODO(tom) This isn't working. I'll fix it later.
	probs=ngram.probabilities(ngram.good_turing(ngram.ngram(nmax,filters.unk(filters.shakespeare(train)))))
	sentence_generation(train,out,nmax,reps,probs)
