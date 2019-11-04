'''
LeetCode 226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree

Hi, here's your problem today. This problem was recently asked by Twitter:

You are given the root of a binary tree. Invert the binary tree in place.
That is, all left children should become right children, and all right children should become left children.

Example:

    a
   / \
  b   c
 / \  /
d   e f

The inverted version of this tree is as follows:

  a
 / \
 c  b
 \  / \
  f e  d
'''
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    def preorder(self, thisLevel=None):
        print(self.val, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

class SolutionRecursion:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            node.left, node.right = node.right,node.left
            for children in (node.left, node.right):
                if children:
                    stack.append(children)
        return root

root = TreeNode('a') 
root.left = TreeNode('b') 
root.right = TreeNode('c') 
root.left.left = TreeNode('d') 
root.left.right = TreeNode('e') 
root.right.left = TreeNode('f') 

root.preorder()
#a b d e c f 
print("")
Solution().invertTree(root)
root.preorder()
#a c f b e d
