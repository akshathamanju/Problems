# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        tmp = ListNode(0)
        s = 0
        while s1 or s2:
            if s1:
                s += s1.pop()
            if s2:
                s += s2.pop()
            tmp.val = s % 10 #remainder
            head = ListNode(s // 10)
            head.next = tmp
            tmp = head
            s //= 10 #carry
        return tmp if tmp.val else tmp.next
