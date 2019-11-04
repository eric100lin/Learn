'''
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, 
determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
*The left subtree of a node contains only 
 nodes with keys less than the node's key.
*The right subtree of a node contains only 
 nodes with keys greater than the node's key.
*Both the left and right subtrees must also 
 be binary search trees.

Hi, here's your problem today. This problem was recently asked by Facebook:
You are given the root of a binary search tree. 
Return true if it is a valid binary search tree, and false otherwise. 
Recall that a binary search tree has the property that 
all values in the left subtree are less than the root, 
and all values in the right subtree are greater than the root.
'''
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Time complexity : O(N) since we visit each node exactly once.
#Space complexity: O(N) since we keep up to the entire tree.
class Solution:
    def isValidBST(self, root: TreeNode, min=None, max=None) -> bool:
        if root:
            if min is not None and root.val<=min:
                return False
            if max is not None and root.val>=max:
                return False
            lValid = self.isValidBST(root.left, min, root.val)
            rValid = self.isValidBST(root.right, root.val, max)
            return lValid and rValid
        #empty tree is valid BST!!
        return True

import unittest

class TestValidBST(unittest.TestCase):

    def testExample1(self):
        #    5
        #   / \
        #  3   7
        # / \ /
        #1  4 6
        a = TreeNode(5)
        a.left = TreeNode(3)
        a.right = TreeNode(7)
        a.left.left = TreeNode(1)
        a.left.right = TreeNode(4)
        a.right.left = TreeNode(6)
        self.assertEqual(Solution().isValidBST(a), True)

    def testExample2(self):
        #   2
        #  / \
        # 1   3
        a = TreeNode(2)
        a.left = TreeNode(1)
        a.right = TreeNode(3)
        self.assertEqual(Solution().isValidBST(a), True)

    def testExample3(self):
        #    5
        #   / \
        #  1   4
        #     / \
        #    3   6
        a = TreeNode(5)
        a.left = TreeNode(1)
        a.right = TreeNode(4)
        a.right.left = TreeNode(3)
        a.right.right = TreeNode(6)
        self.assertEqual(Solution().isValidBST(a), False)

if __name__ == "__main__":
    unittest.main()
