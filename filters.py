# These filters process datasets as file names and return a list of words, as
# well as start-of-sentence symbols.

import re
import string

SOS = '#'
EOS = '.'

eos = ['.', '?', '!']
valid_line_regex = re.compile('[a-z]')
whitespace = re.compile('\s+')

def unk(word,words):
	#I don't know why this isn't working
	#if word not in words:
	#	word='<UNK>'
	return word

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
					words.append(unk(word[0:-1],words)) #word
					words.append(word[-1]) #eos punctuation
					words.append(SOS) #sos marker
				elif word[-1] in string.punctuation:
					#end-of-word mid-sentence punctuation
					words.append(unk(word[0:-1],words)) #word
					words.append(word[-1]) #punctuation
				elif word[0] in string.punctuation:
					#beginning-of-word mid-sentence punctuation
					words.append(word[-1]) #punctuation
					words.append(unk(word[0:-1],words)) #word
				else:
					words.append(unk(word,words))
		else:
			if not words[-1] == SOS:
				words.append(SOS)
	return words
