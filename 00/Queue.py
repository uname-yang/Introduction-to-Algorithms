class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)
if __name__ == '__main__':
	s = Queue()
	for i in xrange(3):
		s.enqueue(i)
	print s.items,s.dequeue,s.items