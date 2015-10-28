def memoizedcutrod(p,n):
	r=[]
	for x in xrange(0,n):
		r.append(-9999)
	return memoizedcutrodaux(p,n,r)

def memoizedcutrodaux(p,n,r):
	q=r[n-1]
	if r[n-1]>=0:
		return r[n]
	if n==0:
		q=0
	elif q==-9999:
		for x in xrange(1,n):
			q=max(q,p[x-1]+memoizedcutrodaux(p,n-x,r))
	r[n-1]=q
	return q

def max(a,b):	
	if a>=b:
		return a
	else:
		return b  

def cutrod(p,n):
	if n==1:
		return p[0]
	q=-99999
	for x in xrange(1,n):
		q=max(q,p[x]+cutrod(p,n-x))
	return q

if __name__ == "__main__":
	p = [1,5,8,9,10,17,17,20,24,30]
	print cutrod(p,2)
	#print memoizedcutrod(p,3)	