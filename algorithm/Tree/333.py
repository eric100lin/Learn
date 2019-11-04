'''
333. Largest BST Subtree
https://leetcode.com/problems/largest-bst-subtree/

Hi, here's your problem today. 
This problem was recently asked by Twitter:

You are given the root of a binary tree. 
Find and return the largest subtree of that tree, 
which is a valid binary search tree.

Input: 
      5
    /  \
   2    4
 /  \
1    3

Output: 2 1 3 
The following subtree is the maximum size BST subtree 
   2  
 /  \
1    3


Input: 
       50
     /    \
  30       60
 /  \     /  \ 
5   20   45    70
              /  \
            65    80
Output: 60 45 70 65 80
The following subtree is the maximum size BST subtree 
      60
     /  \ 
   45    70
        /  \
      65    80
'''
from typing import *

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += ' ' + str(self.left)
        if self.right:
            answer += ' ' + str(self.right)
        return answer


def isValidBST(node, min=None, max=None):
    if node:
        if min is not None and node.key <= min:
            return False, 0
        if max is not None and node.key >= max:
            return False, 0
        left, leftCnt = isValidBST(node.left, min, node.key)
        right, rightCnt = isValidBST(node.right, node.key, max)
        return left and right, leftCnt + rightCnt + 1
    return True, 0

def largest_bst_subtree(root):
    ret = None
    if root:
        res = 0
        import collections
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            is_valid, cnt = isValidBST(node)
            if is_valid and cnt > res:
                res = cnt
                ret = node
            for children in (node.left, node.right):
                if children:
                    q.append(children)
    return ret


import unittest


class TestBST(unittest.TestCase):

    def testExample(self):
        #     5
        #    / \
        #   6   7
        #  /   / \
        # 2   4   9
        node = TreeNode(5)
        node.left = TreeNode(6)
        node.right = TreeNode(7)
        node.left.left = TreeNode(2)
        node.right.left = TreeNode(4)
        node.right.right = TreeNode(9)
        self.assertEqual("7 4 9", str(largest_bst_subtree(node)))

    def testExample2(self):
        #      5
        #    /  \
        #   2    4
        # /  \
        # 1    3
        node = TreeNode(5)
        node.left = TreeNode(2)
        node.right = TreeNode(4)
        node.left.left = TreeNode(1)
        node.left.right = TreeNode(3)
        self.assertEqual("2 1 3", str(largest_bst_subtree(node)))

    def testExample3(self):
        #       50
        #     /    \
        #  30       60
        # /  \     /  \ 
        # 5   20   45    70
        #              /  \
        #            65    80
        node = TreeNode(50)
        node.left = TreeNode(30)
        node.right = TreeNode(60)
        node.left.left = TreeNode(5)
        node.left.right = TreeNode(20)
        node.right.left = TreeNode(45)
        node.right.right = TreeNode(70)
        node.right.right.left = TreeNode(65)
        node.right.right.right = TreeNode(80)
        self.assertEqual("60 45 70 65 80", str(largest_bst_subtree(node)))

    def testExample4(self):
        #       10
        #     /    \
        #   5       15
        # /  \     /  \
        # 1   8   6    7
        node = TreeNode(10)
        node.left = TreeNode(5)
        node.right = TreeNode(15)
        node.left.left = TreeNode(1)
        node.left.right = TreeNode(8)
        node.right.left = TreeNode(6)
        node.right.right = TreeNode(7)
        self.assertEqual("5 1 8", str(largest_bst_subtree(node)))


if __name__ == "__main__":
    unittest.main()
