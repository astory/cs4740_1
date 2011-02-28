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
	for i in range(0,reps):
		for n in range(1,nmax+1):
			try:
				ngram.set_fractions(True)
				out.writerow(trial(train,n,True,probs))
				ngram.set_fractions(False)
				out.writerow(trial(train,n,False,probs))
			except(AttributeError):
				pass

def run(train,nmax,out):
	reps=30
	#train='Shakespeare/short.txt'
	#TODO(tom) This isn't working. I'll fix it later.
	probs=ngram.probabilities(ngram.good_turing(ngram.ngram(nmax,filters.unk(filters.shakespeare(train)))))
	sentence_generation(train,out,nmax,reps,probs)

def main():
	ngram.set_fractions(True)
	nmax=5
	run('War and Peace/Train.txt',nmax,'War and Peace results.csv')
	run('Shakespeare/Train.txt',nmax,'Shakespeare results.csv')

if __name__ == '__main__':
	main()
