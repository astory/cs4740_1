# These filters process datasets as file names and return a list of words, as
# well as start-of-sentence symbols.

import re
import string

SOS = '#'
EOS = '.'
UNK = '<UNK>'

eos = ['.', '?', '!']
valid_line_regex_shakespeare = re.compile('[a-z]')
valid_line_regex_war_and_peace = re.compile('[a-z"]')
valid_line_regex =valid_line_regex_war_and_peace
whitespace = re.compile('\s+')

def unk(words):
	#Add unknown tokens to the first occurance of each word
	#in the list of word tokens words.
	unks=[]
	for i in range(0,len(words)-1):
		if words[i] not in unks:
			unks.append(words[i])
			words[i]=UNK
	return words

def strip_punct(word):
	if word == '' or None:
		l = []
	elif word[-1] in eos :
		#end of sentence punctuation
		l = strip_punct(word[0:-1])
		l.append(word[-1])
		l.append(SOS)
	elif word[-1] in string.punctuation:
		#end-of-word mid-sentence punctuation
		l = strip_punct(word[0:-1])
		l.append(word[-1])
	elif word[0] in string.punctuation:
		#beginning-of-word mid-sentence punctuation
		l = [word[0]]
		l.extend(strip_punct(word[1:]))
	else:
		l = [word]
	return l

def shakespeare(filehandle):
	words = [SOS]
	f = filehandle
	for line in f:
		# if the line is empty, or is just something like "SECOND LORD", the
		# sentence is over, and we should add a new one.
		if valid_line_regex.search(line):
			line_words = whitespace.split(line)
			for word in line_words:
				words.extend(strip_punct(word))
		else:
			if not words[-1] == SOS:
				words.append(SOS)
	return words

#Try unk(shakespeare(filename))
