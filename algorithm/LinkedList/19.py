'''
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list

Hi, here's your problem today. This problem was recently asked by AirBNB:

You are given a singly linked list and an integer k. 
Return the linked list, removing the k-th last element from the list.

Try to do it in a single pass and using constant space.
'''
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        current_node = self
        result = []
        while current_node:
          result.append(current_node.val)
          current_node = current_node.next
        return str(result)

class Solution:
    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        root = Node(-1, head)
        first, second = root, root
        for i in range(n+1):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return root.next

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = Solution().removeNthFromEnd(head, 3)
print(head)
# [1, 2, 4, 5]