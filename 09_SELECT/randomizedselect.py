def select(array, p, r, i):
    if p == r:
        return array[p]
    q = partition(array, p, r)
    k = q - p + 1
    if i == k:
        return array[q]
    elif i < k:
        return select(array, p, q - 1, i)
    else:
        return select(array, q + 1, r, i - k)


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
    d = select(data, 1, 5, 3)
    print d
