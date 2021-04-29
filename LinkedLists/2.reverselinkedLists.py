'''
Problem Statement
Given the head of a Singly LinkedList, reverse the LinkedList.
Write a function to return the new head of the reversed LinkedList.
'''

#mycode
from __future__ import print_function
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()

def reverseLinkedList(head):
    cur = head
    prev = None
    nxt = None
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    head = prev
    return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverseLinkedList(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
'''
Time complexity 
The time complexity of our algorithm will be O(N) where ‘N’ is the total number of nodes in the LinkedList.
Space complexity 
We only used constant space, therefore, the space complexity of our algorithm is O(1).
'''