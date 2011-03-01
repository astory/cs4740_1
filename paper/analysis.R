get_results=function(file) {
	read.csv(
		file,sep='|',header=T,quote='&',
		colClasses=c('integer','logical','numeric','numeric','character')
		)
}

mycols=c('#00000060','#FFFF0060')

results.shakespeare=get_results('../Shakespeare results.csv')
results.tolstoy=get_results('../War and Peace results.csv')

#foo=results.tolstoy
#par(mfrow=c(1,2));for (i in c(0,1)){plot((perplexity)~n,data=subset(foo,use.fractions==i),main=paste('use fractions =',i))}

pp_gen.plot=function(foo,corpusname){
	foo.ag=aggregate(foo$perplexity,list(use.fractions=foo$use.fractions,n=foo$n),mean)
	plot(perplexity~n,data=foo,type='n',axes=F,
		main=paste('Perplexity of generated sentences:',corpusname),
		xlab='n-gram length',
		ylab='Perplexity'
	)
	legend('topright',
		c('Arbitrary precision arithmetic','Log probability'),
		pch=21,
		col=mycols[c(1,2)],
		title='Probability computation method'
	)
	axis(1,at=1:max(foo$n))
	axis(2)
	for (i in c(0,1)){
		points(perplexity~n,data=subset(foo,use.fractions==i),
			pch=21,
			#col=NA,bg=1+i
			col=mycols[1+i]
		)
		lines(x~n,data=subset(foo.ag,use.fractions==i),col=mycols[1+i])
	}
}
