'''
250. Count Univalue Subtrees
https://leetcode.com/problems/count-univalue-subtrees/
https://leetcode.com/articles/count-univalue-subtrees/
https://www.lintcode.com/en/old/problem/count-univalue-subtrees/

Hi, here's your problem today. This problem was recently asked by Microsoft:

A unival tree is a tree where all the nodes have the same value. Given a binary tree, return the number of unival subtrees in the tree.

For example, the following tree should return 5:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

The 5 trees are:
- The three single '1' leaf nodes. (+3)
- The single '0' leaf node. (+1)
- The [1, 1, 1] tree at the bottom. (+1)
'''
from typing import *

#Definition of Node:
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def isUnival(self, node, unival=None):
        if node:
            if unival is not None and node.val!=unival:
                return False
            l = self.isUnival(node.left, node.val)
            r = self.isUnival(node.right, node.val)
            return l and r
        return True
    
    """
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """
    def countUnivalSubtrees(self, root):
        count = 0
        if root:
            import collections
            q = collections.deque()
            q.append(root)
            while q:
                node = q.popleft()
                if self.isUnival(node):
                    count += 1
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return count

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(Solution().countUnivalSubtrees(a))
# 5