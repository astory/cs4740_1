# These filters process datasets as file names and return a list of words, as
# well as start-of-sentence symbols.

import re

SOS = '#'
EOS = '.'

valid_line_regex = re.compile('[a-z]')
whitespace = re.compile('\s+')

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
				elif word[-1] == EOS :
					word = word[0:-1]
					words.append(word)
					words.append(SOS)
				else:
					words.append(word)
		else:
			if not words[-1] == SOS:
				words.append(SOS)
	return words
