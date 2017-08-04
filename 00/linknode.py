class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

if __name__ == '__main__':
    L = Node("A",Node("B",Node("C")))
    print L.next.next.value
