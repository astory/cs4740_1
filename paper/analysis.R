get_results=function(file) {
	read.csv(
		file,sep='|',header=T,quote='&',
		colClasses=c('integer','logical','numeric','numeric','character')
		)
}

mycols=rev(c('#00000060','#FF000060'))

results.shakespeare=get_results('shakespeare.csv')
results.tolstoy=get_results('war_and_peace.csv')

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
		col=c(2,1),
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

test.plot=function(){
	par(mfrow=c(2,1))
	test=read.csv('test_pp.csv')
	plot(perplexity~n.gram_length,data=subset(test,corpus=='Shakespeare'),type='n',
	xlab='n-gram length',ylab='Perplexity',main='Perplexity of the Shakespeare test corpus'
	)
	points(perplexity~n.gram_length,data=subset(test,prob=='ap'&smoothing=='on'&corpus=='Shakespeare'),type='l')
	points(perplexity~n.gram_length,data=subset(test,prob=='ap'&smoothing=='off'&corpus=='Shakespeare'),type='l',col=2)
	#points(perplexity~n.gram_length,data=subset(test,prob=='log'&smoothing=='off'&corpus=='Shakespeare'),type='l')
	legend('topright',
			c('Smoothing on','Smoothing off'),
			lty=1,
			col=c(1,2)
		)

	plot(perplexity~n.gram_length,data=subset(test,corpus=='War_and_Peace'),type='n',
	xlab='n-gram length',ylab='Perplexity',main='Perplexity of the War and Peace test corpus'
	)
	points(perplexity~n.gram_length,data=subset(test,prob=='ap'&smoothing=='on'&corpus=='War_and_Peace'),type='l')
	points(perplexity~n.gram_length,data=subset(test,prob=='ap'&smoothing=='off'&corpus=='War_and_Peace'),type='l',col=2)
	legend('topright',
			c('Smoothing on','Smoothing off'),
			lty=1,
			col=c(1,2)
		)
}		
