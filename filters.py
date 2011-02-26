# These filters process datasets as file names and return a list of words, as
# well as start-of-sentence symbols.

import re
import string

SOS = '#'
EOS = '.'

eos = ['.', '?', '!']
valid_line_regex = re.compile('[a-z]')
whitespace = re.compile('\s+')

def unk(words):
	#Add unknown tokens to the first occurance of each word
	#in the list of word tokens words.
	unks=[]
	for i in range(0,len(words)-1):
		if words[i] not in unks:
			unks.append(words[i])
			words[i]='<UNK>'
	return words

def shakespeare(filename):
	"""Processes input assuming it is shakespeare-like"""
	words = [SOS]
	f = open(filename)
	for line in f:
		# if the line is empty, or is just something like "SECOND LORD", the
		# sentence is over, and we should add a new one.
		if valid_line_regex.search(line):
			line_words = whitespace.split(line)
			for word in line_words:
				if word == '':
					pass
				elif word[-1] in eos :
					#end of sentence punctuation
					words.append(word[0:-1]) #word
					words.append(word[-1]) #eos punctuation
					words.append(SOS) #sos marker
				elif word[-1] in string.punctuation:
					#end-of-word mid-sentence punctuation
					words.append(word[0:-1]) #word
					words.append(word[-1]) #punctuation
				elif word[0] in string.punctuation:
					#beginning-of-word mid-sentence punctuation
					words.append(word[-1]) #punctuation
					words.append(word[0:-1]) #word
				#This currently does not handle middle-of-word punctuation like someone else's program would.
				else:
					words.append(word)
		else:
			if not words[-1] == SOS:
				words.append(SOS)
	return words

#Try unk(shakespeare(filename))
