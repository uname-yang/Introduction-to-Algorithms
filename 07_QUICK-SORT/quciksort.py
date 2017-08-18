def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)


def partition(array, p, r):
    x = array[r]
    j = p

    for i in xrange(p, r):
        if array[i] <= x:
            ij = array[i]
            array[i] = array[j]
            array[j] = ij
            j = j + 1
    jr = array[j]
    array[j] = array[r]
    array[r] = jr
    return j


def print_data(data, has_line=False):
    if has_line:
        print "-----------------------------"
    for i in range(len(data)):
        print str(data[i]),
        if i != len(data) - 1:
            print ",",
    print ""


if __name__ == "__main__":
    #data = [-2, -8, -7, -10, -3,-78, -5, -6, -4, -6]
    data = [-2, 8, -7, 10, 3, 78, -5, 6, -4, 6, 9, -90]  # bug
    print_data(data, True)
    quicksort(data, 0, len(data) - 1)
    print_data(data, True)
