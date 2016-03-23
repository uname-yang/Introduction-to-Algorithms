from Queue import Queue
def josephus(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in xrange(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

if __name__ == '__main__':
    print(josephus(["Bill", "David", "Kent", "Jane", "Susan", "Brad"], 5))