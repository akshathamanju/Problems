'''
take the small pointer, compare the l1 and l2,
if l1 <= l2, pont small as l1 else l2,
In the same way move small,l1, l2 untill l1, l2 becomes empty

Time : O(n)
space: O(1)
'''
class Solution:
    def mergeTwoLists(self, l1, l2):

        if not l1:
            return l2
        if not l2:
            return l1

        small = newhead = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                small.next = l1
                l1 = l1.next
            else:
                small.next = l2
                l2 = l2.next
            small = small.next
        if not l1:
            small.next = l2
        if not l2:
            small.next = l1
        return newhead.next