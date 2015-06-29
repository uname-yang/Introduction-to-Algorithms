
def insertsort(data):
	for j in range(1,len(data)):
		key=data[j]
		i=j-1
		while i>=0 and data[i]>key:
			data[i+1]=data[i]
			i=i-1
		data[i+1]=key
	#return data

def print_data(data, has_line = False):
	if has_line:
		print "-----------------------------"

	for i in range(len(data)):
		print str(data[i]),
		if i != len(data) - 1:
			print ",",
	print ""

if __name__ == "__main__":
	data = [2, 8, 7, 1, 3, 5, 6, 4]
	print "--- before ---"
	print_data(data)
	insertsort(data)
	print "--- after ---"
	print_data(data)
			
