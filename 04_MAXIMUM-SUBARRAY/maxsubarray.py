def findmaxcrossingsubarray(_array,low,mid,high):
	leftsum=-999999999999
	sum=0
	maxleft=low
	for x in xrange(mid,low-1,-1):
		sum=sum+_array[x-1]
		if sum>leftsum:
			leftsum=sum
			maxleft=x
	rightsum=-99999999999
	sum=0
	maxright=mid+1
	for x in xrange(mid+1,high+1):
		sum=sum+_array[x-1]
		if sum>rightsum:
			rightsum=sum
			maxright=x
	return(maxleft,maxright,leftsum+rightsum)

def findmaxsubarray(_array,low,high):
	if high==low:
		return (low,high,_array[low-1])#only on element
	else:
		mid=(low+high)/2
		(leftlow,lefthigh,leftsum)=findmaxsubarray(_array,low,mid)
		(rightlow,righthigh,rightsum)=findmaxsubarray(_array,mid+1,high)
		(crosslow,crosshigh,crosssum)=findmaxcrossingsubarray(_array,low,mid,high)
		if(leftsum>=rightsum and leftsum>=crosssum):
			return(leftlow,lefthigh,leftsum)
		elif(rightsum>=leftsum and rightsum>=crosssum):
			return (rightlow,righthigh,rightsum)
		else:
			return(crosslow,crosshigh,crosssum)

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
	data = [-2, 8, -7, 10, 3,78, -5, 6, -4, 6,9,-90]#bug
	print "--- input ---"
	print_data(data)
	(low,high,_sum)=findmaxsubarray(data,1,len(data))
	print "--- maximum subarray ---"
	subdata=[]
	for x in xrange(low,high+1):
		subdata.append(data[x-1])
	print_data(subdata)
	print '--- max sum ---'
	print _sum
			
