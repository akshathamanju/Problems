'''
take 2 pointers to a, b to headA, headB respectively
for each iteration check whether a and b are pointing to the same node,
if so return the value.
supppose the traversal of one list reached end then point the pointer to the other list and continue the comparision

Time: O(N+M)
space: O(1)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):

        if not headA or not headB:
            return None

        a = headA
        b = headB

        while a != b:
            if not a:
                a = headB
            else:
                a = a.next
            if not b:
                b = headA
            else:
                b = b.next
        return b


