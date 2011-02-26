# These filters process datasets as file names and return a list of words, as
# well as start-of-sentence symbols.

import re
import string

SOS = '#'
EOS = '.'

eos = ['.', '?', '!']
valid_line_regex = re.compile('[a-z]')
whitespace = re.compile('\s+')
#Add spaces before or after punctuation
#??? How do you do
#echo 'euthasonethu, ousnthoaeu "asoehushanotheus soe '| sed  -e 's/\([a-z]\)\([,"]\)/\1\ \2/' -e 's/\([,"]\)\([a-z]\)/\1\ \2/'
#in python?
punct_begin=re.sub('[%s][a-z]' % re.escape(string.punctuation), '', s)
punct_end=re.sub('[a-z][%s]' % re.escape(string.punctuation), '', s)
#Running both of these in series will sep ' a ' rate punctuation in the mid'dle of words

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
					word = word[0:-1]
					words.append(word)
					words.append(SOS)
				else:
					words.append(word)
		else:
			if not words[-1] == SOS:
				words.append(SOS)
	return words
