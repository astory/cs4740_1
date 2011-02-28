#!/usr/bin/env python
import ngram
import filters
import csv
import random

ngram.good_turing =lambda x:x

def trial(train,n,p,probs):
	"""n is n-gram size. p is whether it's log or arbitrary precision"""
	ngram.set_fractions(p)
	sentence=ngram.make_sentence(probs[0:(n+1)])
	pp=ngram.perplexity(probs[0:(n+1)],sentence)
	time='NA'
	return [n,p,pp,time,' '.join(sentence)]

def sentence_generation(train,filename,nmax,reps,probs_ap,probs_log):
	#Open results file
	out_fh = open(filename, 'wb')
	out=csv.writer(out_fh, delimiter='|', quotechar='&', quoting=csv.QUOTE_NONE)
	out.writerow(['n','use fractions','perplexity','time','sentence'])
	
	#Write perplexities and other output
	for i in range(0,reps):
		for n in range(1,nmax+1):
			try:
				out.writerow(trial(train,n,True,probs_ap))
				out.writerow(trial(train,n,False,probs_log))
				out_fh.flush()
			except(AttributeError):
				pass

def run(train,nmax,reps,out):
	#Get probabilities
	fh = open(train)
	ngram.set_fractions(True)
	probs_ap=ngram.probabilities(ngram.good_turing(ngram.ngram(nmax,filters.unk(filters.shakespeare(fh)))))
	
	fh = open(train)
	ngram.set_fractions(False)
	probs_log=ngram.probabilities(ngram.good_turing(ngram.ngram(nmax,filters.unk(filters.shakespeare(fh)))))
	
	sentence_generation(train,out,nmax,reps,probs_ap,probs_log)

def main():
	nmax=2
	reps=2
	run('War and Peace/short.txt',nmax,reps,'War and Peace results.csv')
	#nmax=5
	#run('War and Peace/Train.txt',nmax,'War and Peace results.csv')
	#run('Shakespeare/Train.txt',nmax,'Shakespeare results.csv')

if __name__ == '__main__':
	main()
