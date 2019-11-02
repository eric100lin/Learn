from collections import deque

class Node:
    def __init__(self, v):
        self.value=v
        self.left=None
        self.right=None
    # level-by-level pretty-printer
    def __str__(self):
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value) + ' '
            nodes.append(node.left)
            nodes.append(node.right)
        return answer

def binarySearch(root, v):
    if root:
        if v<root.value:
            return binarySearch(root.left, v)
        elif v>root.value:
            return binarySearch(root.right, v)
        else:
            return True
    return False

def binarySearchInterative(root, v):
    curr = root
    while curr:
        if v<curr.value:
            curr = curr.left
        elif v>curr.value:
            curr = curr.right
        else:
            return True
    return False

# 2 5 30 40 60 65 70 80
root = Node(30)
root.left = Node(5)
root.right = Node(40)

root.left.left = Node(2)

root.right.right = Node(60)
root.right.right.right = Node(70)

root.right.right.right.left = Node(65)
root.right.right.right.right = Node(80)

print(root)

#print(binarySearch(root, 65))
print(binarySearchInterative(root, 65))