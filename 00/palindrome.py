# -*- coding: utf-8 -*-
from Deque import Deque
def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        ##chardeque.addRear(ch)
        chardeque.addFront(ch)

    while chardeque.size() > 1:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            return False

    return True

if __name__ == '__main__':
    str1 = 'able was i ere i saw elba'
    print('"%s" is%s palindrome' % (str1, '' if palchecker(str1) else ' not'))