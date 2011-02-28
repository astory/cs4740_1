#!/bin/bash
for n in 1 2 3 4 5 6
	do for corpus in 'Shakespeare' 'War and Peace'
		#Header for csv file
		do echo 'corpus, n-gram length, smoothing, prob, perplexity'
		echo corpus ', ' $n ', ' 'on'  ', ' 'log' ', ' `./ngram.py -n $n -t $corpus/Train.txt -p $corpus/Test.txt -sl|grep 'Perplexity:'|cut -d ' ' -f 2`
		echo corpus ', ' $n ', ' 'off' ', ' 'log' ', ' `./ngram.py -n $n -t $corpus/Train.txt -p $corpus/Test.txt  -l|grep 'Perplexity:'|cut -d ' ' -f 2`
		echo corpus ', ' $n ', ' 'on'  ', ' 'ap'  ', ' `./ngram.py -n $n -t $corpus/Train.txt -p $corpus/Test.txt -s |grep 'Perplexity:'|cut -d ' ' -f 2`
		echo corpus ', ' $n ', ' 'off' ', ' 'ap'  ', ' `./ngram.py -n $n -t $corpus/Train.txt -p $corpus/Test.txt    |grep 'Perplexity:'|cut -d ' ' -f 2`
	done
done
