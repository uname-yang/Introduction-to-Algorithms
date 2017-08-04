class Tree:
    def __init__(self,left,right):
        self.left=left
        self.right=right

if __name__ == '__main__':
    T = Tree(Tree("A","B"),Tree("C","D"))
    print(T.right.left)
