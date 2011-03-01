#!/usr/bin/env/python
import filters
import ngram

train = open('Shakespeare/Train.txt')
test = open('Shakespeare/Test.txt')

ngram.set_fractions(True)
train_words = filters.unk(filters.shakespeare(train))
ngrams = ngram.ngram(3, train_words)
probs = ngram.probabilities(ngrams)
test_words = filters.shakespeare(test)

def test(use_fractions):
	ngram.set_fractions(use_fractions)
	print ngram.perplexity(probs, test_words)

if __name__=='__main__':
	print "testing now"
	from timeit import Timer
	t = Timer("test(True)", "from __main__ import test")
	#u = Timer("test(False)", "from __main__ import test")
	print "fractions on: %s" % t.timeit(number=10)
	#print "fractions off: %s" % u.timeit(number=10)
