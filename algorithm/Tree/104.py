'''
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Hi, here's your problem today. 
This problem was recently asked by Google:
You are given the root of a binary tree.
Return the deepest node (the furthest node from the root).

Example:
    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.
'''
from typing import *
import collections

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        maxdepth = 0
        if root:
            q = collections.deque()
            q.append((root, 1))
            while q:
                (node, depth) = q.popleft()
                maxdepth = max(maxdepth, depth)
                for children in (node.left, node.right):
                    if children:
                        q.append((children, depth+1))
        return maxdepth

def deepest(node):
    if not node:
        return None
    q = collections.deque()
    q.append((node, 1))
    maxdepth = 1
    depestNode = node
    while q:
        (n,depth) = q.popleft()
        for children in (n.left, n.right):
            if children is not None:
                q.append((children, depth+1))
        if depth > maxdepth:
            maxdepth = depth
            depestNode = n
    return depestNode

root = TreeNode('a')
root.left = TreeNode('b')
root.left.left = TreeNode('d')
root.right = TreeNode('c')

print(deepest(root))
# (d, 3)
print(Solution().maxDepth(root))
#3