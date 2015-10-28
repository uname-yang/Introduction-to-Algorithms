def left(i):
	return 2*i
def right(i):
	return 2*i+1
def parent(i):
	return i/2
def maxheapify(_array,size,i): 
	l=left(i)
	r=right(i)
	largest=i
	if l<=size and _array[l-1]>_array[i-1]:
		largest=l
	else:
		largest=i
	if r<=size and _array[r-1]>_array[largest-1]:
		largest=r
	if largest!=i:
		temp=_array[i-1]
		_array[i-1]=_array[largest-1]
		_array[largest-1]=temp
		maxheapify(_array,size,largest)
def buildmaxheap(_array):
	size=len(_array)
	for x in xrange(size,0,-1):
		maxheapify(_array,size,x)
def heapsort(_array):
	buildmaxheap(_array)
	size=len(_array)
	for x in xrange(len(_array),1,-1):
		temp=_array[0]
		_array[0]=_array[x-1]
		_array[x-1]=temp
		size=size-1
		maxheapify(_array,size,1)


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
	data = [4,1,3,2,16,9,10,14,8,7]
	print "--- input ---"
	print_data(data)
	buildmaxheap(data)
	print '--- max heap ---'
	print_data(data)
	heapsort(data)
	print '--- heap sort ---'
	print_data(data)
			
