import filters

TRAIN='Shakespeare/Train.txt'
UNI='Shakespeare/unigrams.txt'
BI=
TRI=

uni=filters.shakespeare(TRAIN)

g=open(UNI,'w')
for i in range(0,len(uni)-1):
	g.write(uni[i]+'\n')

g.close()
