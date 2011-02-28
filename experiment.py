#!/usr/bin/env python
import ngram
import filters
import csv
import random

ngram.good_turing =lambda x:x

def trial(train,n,p,probs):
	"""n is n-gram size. p is whether it's log or arbitrary precision"""
	ngram.set_fractions(randint(0,1))
	sentence=ngram.make_sentence(probs[0:(n+1)])
	pp=ngram.perplexity(probs[0:(n+1)],sentence)
	time='NA'
	return [n,p,pp,time,' '.join(sentence)]

def sentence_generation(train,filename,nmax,reps,probs):
	out_fh = open(filename, 'wb')
	out=csv.writer(out_fh, delimiter='|', quotechar='&', quoting=csv.QUOTE_NONE)
	out.writerow(['n','use fractions','perplexity','time','sentence'])
	for i in range(0,reps):
		for n in range(1,nmax+1):
			try:
				#ngram.set_fractions(True)
				#out.writerow(trial(train,n,True,probs))
				#ngram.set_fractions(False)
				out.writerow(trial(train,n,False,probs))
				out_fh.flush()
			except(AttributeError):
				pass

def run(train,nmax,out):
	reps=2
	#train='Shakespeare/short.txt'
	#TODO(tom) This isn't working. I'll fix it later.
	fh = open(train)
	probs=ngram.probabilities(ngram.good_turing(ngram.ngram(nmax,filters.unk(filters.shakespeare(fh)))))
	sentence_generation(train,out,nmax,reps,probs)

def main():
	ngram.set_fractions(True)
	nmax=5
	run('War and Peace/Train.txt',nmax,'War and Peace results.csv')
	run('Shakespeare/Train.txt',nmax,'Shakespeare results.csv')

if __name__ == '__main__':
	main()
