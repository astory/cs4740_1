#!/usr/bin/env python
import ngram
import filters
import csv
import random

ngram.good_turing =lambda x:x

def trial(train,n,p='ap'):
	"""n is n-gram size. p is whether it's log, arbitrary precision or float"""
	#Start timer
	probs=ngram.probabilities(ngram.good_turing(ngram.ngram(n,filters.unk(filters.shakespeare(train)))))
	sentence=ngram.make_sentence(probs)
	pp=ngram.perplexity(probs,sentence)
	#End timer
	time=42
	return [n,p,pp,time,sentence]

def sentence_generation(train,filename,nmax,reps):
	out=csv.writer(open(filename, 'wb'), delimiter='|', quotechar='&', quoting=csv.QUOTE_NONE)
	for i in range(0,nmax*reps):
		n=random.randint(1,nmax)
		out.writerow(trial(train,n))

def main():
	sentence_generation('Shakespeare/Train.txt','hi.csv',3,30)
