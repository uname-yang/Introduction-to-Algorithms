def countingsort(A,k):# A<-[0,k]
	C=[]
	B=[]
	for x in xrange(0,k):
		C.append(0)
	for x in xrange(0,len(A)):
		B.append(0)
	for x in xrange(0,len(A)):
		C[A[x]]=C[A[x]]+1
	print_data(C,True)
	for x in xrange(1,k-1):
		C[x]=C[x]+C[x-1]
	print_data(C,True)
	for x in xrange(len(A),0,-1):
		B[C[A[x-1]]-1]=A[x-1]
		C[A[x-1]]=C[A[x-1]]-1
	return B

def print_data(data, has_line = False):
	if has_line:
		print "-----------------------------"
	for i in range(len(data)):
		print str(data[i]),
		if i != len(data) - 1:
			print ",",
	print ""

if __name__ == "__main__":
	#data = [-2, -8, -7, -10, -3,-78, -5, -6, -4, -6]
	data = [2, 8, 33, 10, 3,78, 5, 6, 4, 6,9,90]
	print_data(data,True)
	data2=countingsort(data,98)
	print_data(data2,True)
			
