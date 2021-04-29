"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


#Use of dictionary for O(1) lookup
#clone only the values of link list(set the next and random as None)
#copy the random and next only if they exist(i.e. Not None)
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return head
        # Use of dictionary for O(1) lookup
        d = {}
        curr = head
        # clone only the values of link list(set the next and random as None)
        while curr:
            d[curr] = Node(curr.val, None, None)
            curr = curr.next
        curr = head
        # copy the random and next only if they exist(i.e. Not None)
        while curr:
            if curr.next:
                d[curr].next = d[curr.next]
            if curr.random:
                d[curr].random = d[curr.random]
            curr = curr.next
        return d[head]