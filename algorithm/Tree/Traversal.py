class Node:
    def __init__(self, v):
        self.value=v
        self.left=None
        self.right=None
    def preorder(self):
        print(self.value,end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
    def preorder_interative(self):
        stack = [ self ]
        while stack:
            node = stack.pop()
            print(node.value,end=' ')
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.value,end=' ')
        if self.right is not None:
            self.right.inorder()
    def inorder_interative(self):
        stack = []
        curr = self
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                print(curr.value, end=' ')
                curr = curr.right
            else:
                break
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.value,end=' ')
    def postorder_interative(self):
        s1 = [ self ]
        s2 = []
        while s1:
            node = s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        while s2:
            print(s2.pop().value,end=' ')
    def levelorder(self):
        import queue
        q = queue.Queue()
        curr = self
        while True:
            print(curr.value, end=' ')
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)
            if q.empty():
                break
            curr = q.get()

def copy(root):
    if root:
        newNode = Node(root.value)
        newNode.left = copy(root.left)
        newNode.right = copy(root.right)
        return newNode
    return None

def equal(t1,t2):
    if t1 is None and t2 is None:
        return True
    return t1 and t2 and \
        t1.value==t2.value and \
        equal(t1.left,t2.left) and \
        equal(t1.right,t2.right)

# A/B*C*D+E
root = Node('+')
root.left = Node('*')
root.right = Node('E')

root.left.left = Node('*')
root.left.right = Node('D')

root.left.left.left = Node('/')
root.left.left.right = Node('C')

root.left.left.left.left = Node('A')
root.left.left.left.right = Node('B')

oldRoot = root
root = copy(oldRoot)
print('Compare: {}'.format(equal(oldRoot,root)))

print('Preorder:')
root.preorder()
print()
root.preorder_interative()
print()

print('Inorder:')
root.inorder()
print()
root.inorder_interative()
print()

print('Postorder:')
root.postorder()
print()
root.postorder_interative()
print()

print('Levelorder:')
root.levelorder()
print()
