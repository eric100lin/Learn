'''
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Hi, here's your problem today. 
This problem was recently asked by Microsoft:
You are given the preorder and inorder traversals 
of a binary tree in the form of arrays. 
Write a function that reconstructs the 
tree represented by these traversals.

Example:
Preorder: [a, b, d, e, c, f, g]
Inorder:  [d, b, e, a, f, c, g]

The tree that should be constructed from these traversals is:
    a
   / \
  b   c
 / \ / \
d  e f  g
'''
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def traversal(self):
        if self.left is not None:
            self.left.traversal()
        if self.right is not None:
            self.right.traversal()
        print(self.val, end=' ')

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder or len(preorder)!=len(inorder):
            return None
        root = TreeNode(preorder[0])
        rootIdxInorder = inorder.index(preorder[0])
        root.left  = self.buildTree(preorder[1:rootIdxInorder+1], inorder[:rootIdxInorder])
        root.right = self.buildTree(preorder[rootIdxInorder+1:],  inorder[rootIdxInorder+1:])
        return root

preorder = [3,9,20,15,7]
inorder =  [9,3,15,20,7]
root = Solution().buildTree(preorder, inorder)
root.traversal()
print()