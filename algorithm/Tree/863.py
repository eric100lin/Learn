'''
863. All Nodes Distance K in Binary Tree
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

We are given a binary tree (with root node root),
a target node, and an integer value K.
Return a list of the values of all nodes that 
have a distance K from the target node.  
The answer can be returned in any order.

Input: 
 root(TreeNodes) = [3,5,1,6,2,0,8,null,null,7,4], 
 target(TreeNodes) = 5, K(int) = 2
Output: [7,4,1]
Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above 
are just serializations of these objects.

Explanation: 
The nodes that are a distance 2 from 
the target node (with value 5)
have values 7, 4, and 1.

#     3
#    /  \
#   5    1
#  / \  / \
#  6 2  0 8
#   / \
#   7 4

Note:
The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
'''
# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def addParentField(self, node, parent=None):
        if node:
            node.parent = parent
            self.addParentField(node.left, node)
            self.addParentField(node.right, node)

    def distanceK(self, root, target, K):
        """
        :type root: Node
        :type target: Node
        :type K: int
        :rtype: List[int]
        """
        result = []
        self.addParentField(root)
        if root and target:
            q  = collections.deque()
            q.append((target, 0))
            seen = { target }
            while q:
                node, d = q.popleft()
                if d==K:
                    result.append(node.val)
                else:
                    for nei in (node.left, node.right, node.parent):
                        if nei and nei not in seen:
                            q.append((nei, d+1))
                            seen.add(nei)
        return result

    def valuesAtHeight(self, root, height):
        result = []
        if root:
            q = collections.deque()
            q.append((root, 1))
            while q:
                node, h = q.popleft()
                if h==height:
                    result.append(node.val)
                else:
                    for child in (node.left, node.right):
                        if child:
                            q.append((child, h+1))
        return result

import unittest

class TestDistanceK(unittest.TestCase):

    def testExample1(self):
        #[3,5,1,6,2,0,8,null,null,7,4]
        #Target=5
        #K=2
        #      3
        #     / \
        #   5    1
        #  / \   / \
        # 6   2  0  8
        #    / \
        #   7   4
        a = Node(3)
        a.left = Node(5)
        a.right = Node(1)
        a.left.left = Node(6)
        a.left.right = Node(2)
        a.right.left = Node(0)
        a.right.right = Node(8)
        a.left.right.left = Node(7)
        a.left.right.right = Node(4)
        self.assertEqual(set(Solution().distanceK(a, a.left, 2)), set([7, 4, 1]))

    def testExample2(self):
        #[0,2,1,null,null,3]
        #Target=3
        #K=3
        #      0
        #     / \
        #   2    1
        #       /
        #      3 
        a = Node(0)
        a.left = Node(2)
        a.right = Node(1)
        a.right.left = Node(3)
        self.assertEqual(set(Solution().distanceK(a, a.right.left, 3)), set([2]))

class TestValuesAtHeight(unittest.TestCase):

    def testExample1(self):
        #     1
        #    / \
        #   2   3
        #  / \   \
        # 4   5   7
        a = Node(1)
        a.left = Node(2)
        a.right = Node(3)
        a.left.left = Node(4)
        a.left.right = Node(5)
        a.right.right = Node(7)
        self.assertEqual(Solution().valuesAtHeight(a, 3), [4, 5, 7])
        self.assertEqual(Solution().valuesAtHeight(a, 2), [2, 3])
        self.assertEqual(Solution().valuesAtHeight(a, 1), [1])
        self.assertEqual(Solution().valuesAtHeight(a, 0), [])

if __name__ == "__main__":
    unittest.main()