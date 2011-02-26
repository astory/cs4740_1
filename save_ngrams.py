#Save unigrams to a file.
#Then create n>1 n-grams and save those to a file.
import filters

TRAIN='Shakespeare/Train.txt'
UNI='Shakespeare/unigrams.txt'
BI='Shakespeare/bigrams.txt'
TRI='Shakespeare/trigrams.txt'

uni=filters.shakespeare(TRAIN)

g=open(UNI,'w')
for i in range(0,len(uni)-1):
	g.write(uni[i]+'\n')
g.close()

