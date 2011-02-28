#!/bin/bash
#TRAIN='Train.txt'
#TEST='Test.txt'
TRAIN='shorter.txt'
TEST='short.txt'
echo 'corpus, n-gram length, smoothing, prob, perplexity,sentence'
for n in 1 #2 #3 4 5 6
	do for corpus in 'Shakespeare' #'War and Peace'
		#Header for csv file
		do echo corpus ', ' $n ', ' 'on'  ', ' 'log' ', ' `./ngram.py -n $n -t $corpus/$TRAIN -sl -p $corpus/$TEST|grep '^Perplexity:'|cut -d ' ' -f 2` ', ' `./ngram.py -n $n -t $corpus/$TRAIN -slm|tail -n 1`
		
		echo    corpus ', ' $n ', ' 'off' ', ' 'log' ', ' `./ngram.py -n $n -t $corpus/$TRAIN  -l -p $corpus/$TEST|grep '^Perplexity:'|cut -d ' ' -f 2` ', ' `./ngram.py -n $n -t $corpus/$TRAIN  -lm|tail -n 1`
		
		echo    corpus ', ' $n ', ' 'on'  ', ' 'ap'  ', ' `./ngram.py -n $n -t $corpus/$TRAIN  -s -p $corpus/$TEST|grep '^Perplexity:'|cut -d ' ' -f 2` ', ' `./ngram.py -n $n -t $corpus/$TRAIN  -sm|tail -n 1`
		
		echo    corpus ', ' $n ', ' 'off' ', ' 'ap'  ', ' `./ngram.py -n $n -t $corpus/$TRAIN     -p $corpus/$TEST|grep '^Perplexity:'|cut -d ' ' -f 2` ', ' `./ngram.py -n $n -t $corpus/$TRAIN   -m|tail -n 1`
	done
done
