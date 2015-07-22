def merge(_array,p,q,r):
	n1=q-p+1
	n2=r-q
	L=[]
	R=[]
	for x in xrange(0,n1):
		L.append(_array[p+x-1])
	for x in xrange(0,n2):
		R.append(_array[q+x])
	L.append(999999999999999)
	R.append(999999999999999)

	i=0
	j=0
	for x in xrange(p-1,r):
		if L[i]<=R[j]:
			_array[x]=L[i]
			i=i+1
		else:
			_array[x]=R[j]
			j=j+1

def mergesort(_array,p,r):
	if p<r:
		q=(p+r)/2
		mergesort(_array,p,q)
		mergesort(_array,q+1,r)
		merge(_array,p,q,r)

def print_data(data, has_line = False):
	if has_line:
		print "-----------------------------"

	for i in range(len(data)):
		print str(data[i]),
		if i != len(data) - 1:
			print ",",
	print ""

if __name__ == "__main__":
	data = [2, 89, 6, 7, 1, 99, 5, 6,898,6,3789,80,99]
	print "--- before ---"
	print_data(data)
	#merge(data,1,4,8)
	#print_data(data)
	mergesort(data,1,len(data))
	print "--- after ---"
	print_data(data)
			
