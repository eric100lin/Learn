class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def isSymmetricSubTree(left,right):
    if left is None and right is None:
        return True
    if left is not None and right is not None:
        return left.data == right.data and \
               isSymmetricSubTree(left.left, right.right) and \
               isSymmetricSubTree(left.right, right.left)
    return False

def isSymmetric(head):
    if head is not None:
       return isSymmetricSubTree(head.left, head.right)
    return False

def isBSTSubTree(left,right,parentData):
    if left is not None:
        if left.data>parentData or \
           not isBSTSubTree(left.left, left.right, left.data):
            return False
    if right is not None:
        if right.data<parentData or \
           not isBSTSubTree(right.left, right.right, right.data):
            return False
    return True

def isBST(head):
    if head is not None:
       return isBSTSubTree(head.left, head.right, head.data)
    return True #empty tree must BST

if __name__ == "__main__":
    tree1 = Node(8)
    tree1.left = Node(3)
    tree1.right = Node(10)
    
    tree1.left.left = Node(1)
    tree1.left.right = Node(6)
    tree1.left.right.left = Node(4)
    tree1.left.right.right = Node(7)
    
    tree1.right.right = Node(14)
    tree1.right.right.left = Node(13)
    print('isSymmetric: {}'.format(isSymmetric(tree1)))
    print('isBST: {}'.format(isBST(tree1)))
    
    tree2 = Node(314)
    tree2.left = Node(6)
    tree2.right = Node(6)
    tree2.left.right = Node(2)
    tree2.left.right.right = Node(3)
    tree2.right.left = Node(2)
    tree2.right.left.left = Node(3)
    print('isSymmetric: {}'.format(isSymmetric(tree2)))
    print('isBST: {}'.format(isBST(tree2)))