#!/bin/bash
for n in 1 2 3 4 5 6
	do for corpus in 'Shakespeare' 'War and Peace'
		#Header for csv file
		do echo 'corpus, n-gram length, smoothing, prob, perplexity,sentence'
		echo corpus ', ' $n ', ' 'on'  ', ' 'log' ', ' \
		#Perplexity
		`./ngram.py -n $n -t $corpus/Train.txt -sl -p $corpus/Test.txt|grep 'Perplexity:'|cut -d ' ' -f 2` ', ' \
		#Sentence
		`./ngram.py -n $n -t $corpus/Train.txt -sl|tail -n 1`
		
		echo corpus ', ' $n ', ' 'off' ', ' 'log' ', ' \
		#Perplexity
		`./ngram.py -n $n -t $corpus/Train.txt  -l -p $corpus/Test.txt|grep 'Perplexity:'|cut -d ' ' -f 2` ', ' \
		#Sentence
		`./ngram.py -n $n -t $corpus/Train.txt  -l|tail -n 1`
		
		echo corpus ', ' $n ', ' 'on'  ', ' 'ap'  ', ' \
		#Perplexity
		`./ngram.py -n $n -t $corpus/Train.txt  -s -p $corpus/Test.txt|grep 'Perplexity:'|cut -d ' ' -f 2` ', ' \
		#Sentence
		`./ngram.py -n $n -t $corpus/Train.txt  -s|tail -n 1`
		
		echo corpus ', ' $n ', ' 'off' ', ' 'ap'  ', ' \
		#Perplexity
		`./ngram.py -n $n -t $corpus/Train.txt     -p $corpus/Test.txt|grep 'Perplexity:'|cut -d ' ' -f 2` ', ' \
		#Sentence
		`./ngram.py -n $n -t $corpus/Train.txt    |tail -n 1`
	done
done
