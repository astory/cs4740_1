#!/usr/bin/env python
from random import normalvariate #Just for generating numbers for testing functions
from math import log,e

#Assume we already have the counts in some file and that this function gets them
def C(ngram):
	#Return the count of a particular n-gram somehow
	return normalvariate(0.25,0.05)

#Get the probability of a particular series of words with MLE
def p(wordlist,N):
	#n is the length of wordlist
	n=len(wordlist)-1 #Check here if we get off-by-one problems
	#Accessing indexes with python is surprisingly annoying to me.
	#When you use ranges, the higher number is a strict boundary.
	log_p=0
	print 'This is wrong. Fix it.'
	for i in range(1,n+1,N):
		#The log_p value should be negative
		log_p=log(C(wordlist[n-i*N+1:n-(i-1)*N])/C(wordlist[n-i*N:n-(i-1)*N]))+log_p
		print e**log_p
	return log_p
