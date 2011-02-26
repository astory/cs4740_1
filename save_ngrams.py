#Save unigrams to a file.
#Then create n>1 n-grams and save those to a file.
#Ooops you already wrote a better version of this
import filters

TRAIN='Shakespeare/Train.txt'
UNI='Shakespeare/unigrams.txt'
BI='Shakespeare/bigrams.txt'
TRI='Shakespeare/trigrams.txt'

uni=filters.shakespeare(TRAIN)

#Unigrams
g=open(UNI,'w')
for i in range(0,len(uni)-1):
	g.write(uni[i]+'\n')
g.close()


n=3
g=open(TRI,'w')
for i in range(n,len(uni)):
	g.write(uni[i:i+n+1]+'\n')
g.close()
