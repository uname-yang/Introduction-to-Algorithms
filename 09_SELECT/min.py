def minium(A):
	min=A[0]
	for x in xrange(1,len(A)-1):
		if min >A[x]:
			min=A[x]
	return min  
		

