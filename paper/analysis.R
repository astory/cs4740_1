get_results=function(file) {
	read.csv(
		file,sep='|',header=T,quote='&',
		colClasses=c('integer','logical','numeric','numeric','character')
		)
}

results.shakespeare=get_results('../Shakespeare results.csv')
results.tolstoy=get_results('../War and Peace results.csv')

#foo=results.tolstoy
#par(mfrow=c(1,2));for (i in c(0,1)){plot((perplexity)~n,data=subset(foo,use.fractions==i),main=paste('use fractions =',i))}

pp_gen.plot=function(foo){
	foo.ag=aggregate(foo$perplexity,list(use.fractions=foo$use.fractions,n=foo$n),mean)
	plot(perplexity~n,data=foo,type='n',axes=F,
		main='Perplexity of generated sentences as a function of n-gram length and probability computation method',
		xlab='n-gram length',
		ylab='Perplexity'
	)
	axis(1,at=1:max(foo$n))
	axis(2)
	for (i in c(0,1)){
		points(perplexity~n,data=subset(foo,use.fractions==i),pch=21,col=NA,bg=1+i)
		lines(x~n,data=subset(foo.ag,use.fractions==i),col=1+i)
	}
}
