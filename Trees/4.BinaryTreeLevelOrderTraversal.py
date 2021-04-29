# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
use queue for storing the elements
for each element in the queue check whether thay have children

Time: O(n)
space: O(n)
'''
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def levelOrder(self, root: TreeNode) -> List[List[int]]:

            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """

            if not root:
                return []
            result = []
            queue = deque()
            queue.append(root)

            while len(queue) > 0:
                queue_len = len(queue)
                level = []
                for i in range(queue_len):
                    node = queue.popleft()  # removes the 1st element of the queue
                    level.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(level)
            return result
