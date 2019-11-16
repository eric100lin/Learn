'''
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, 
return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
from typing import *
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if root:
            q = collections.deque()
            q.append((root, 0))
            while q:
                current, level = q.popleft()
                for child in (current.left, current.right):
                    if child:
                        q.append((child, level+1))
                # Elegant! Use index >= (length of array) to check
                if level >= len(ans):
                    ans.append([current.val])
                else:
                    ans[level].append(current.val)
        return ans

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrder(root))
# [[3], [9, 20], [15, 7]]
