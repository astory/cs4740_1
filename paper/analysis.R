get_results=function(file) {read.csv(file,sep='|',colClasses=c('integer','logical','numeric','numeric','character'))}

#results.shakespeare=get_results('Shakespeare results.csv')
results.tolstoy=get_results('War and Peace results.csv')

foo=results.tolstoy
par(mfrow=c(1,2));for (i in c(0,1)){plot((perplexity)~n,data=subset(foo,use.fractions==i),main=paste('use fractions =',i))}
