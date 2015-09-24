class Node:
    def __init__(self, initdata):
        self.__data = initdata
        self.__next = None

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, newnext):
        self.__next = newnext

class SinCycLinkedlist:
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(self.head)

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)

    def remove(self, item):
        prev = self.head
        while prev.getNext() != self.head:
            cur = prev.getNext()
            if cur.getData() == item:
                prev.setNext(cur.getNext())
            prev = prev.getNext()

    def search(self, item):
        cur = self.head.getNext()
        while cur != self.head:
            if cur.getData() == item:
                return True
            cur = cur.getNext()

        return False

    def empty(self):
        return self.head.getNext() == self.head

    def size(self):
        count = 0
        cur = self.head.getNext()
        while cur != self.head:
            count += 1
            cur = cur.getNext()

        return count

if __name__ == '__main__':
    s = SinCycLinkedlist()
    print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))

    s.add(19)
    s.add(86)
    print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))

    print('86 is%s in s' % ('' if s.search(86) else ' not',))
    print('4 is%s in s' % ('' if s.search(4) else ' not',))
    print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))

    s.remove(19)
    print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))