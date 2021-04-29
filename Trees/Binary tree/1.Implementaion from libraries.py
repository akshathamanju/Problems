
from binarytree import tree
from binarytree import Node
from binarytree import build
from binarytree import Node

root = Node(1)                  # index: 0, value: 1
root.left = Node(2)             # index: 1, value: 2
root.right = Node(3)            # index: 2, value: 3
root.left.right = Node(4)       # index: 4, value: 4
root.left.right.left = Node(5)  # index: 9, value: 5

print(root)
#
#      ____1
#     /     \
#    2__     3
#       \
#        4
#       /
#      5
#
root.pprint(index=True)
#
#       _________0-1_
#      /             \
#    1-2_____        2-3
#            \
#           _4-4
#          /
#        9-5
#
print(root[9])
# Node(5)

# Replace the node/subtree at index 4
root[4] = Node(6, left=Node(7), right=Node(8))
root.pprint(index=True)
#
#       ______________0-1_
#      /                  \
#    1-2_____             2-3
#            \
#           _4-6_
#          /     \
#        9-7     10-8
#

# Delete the node/subtree at index 1
del root[1]
root.pprint(index=True)
#
#    0-1_
#        \
#        2-3

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(root)
#
#        __1
#       /   \
#      2     3
#     / \
#    4   5
#
print(root.inorder)
# [Node(4), Node(2), Node(5), Node(1), Node(3)]

print(root.preorder)
# [Node(1), Node(2), Node(4), Node(5), Node(3)]

print(root.postorder)
# [Node(4), Node(5), Node(2), Node(3), Node(1)]

print(root.levelorder)
# [Node(1), Node(2), Node(3), Node(4), Node(5)]

print(list(root)) # Equivalent to root.levelorder
# [Node(1), Node(2), Node(3), Node(4), Node(5)]

values = [7, 3, 2, 6, 9, None, 1, 5, 8]
root = build(values)
print(root)

# Go back to list representation
print(root.values)
# [7, 3, 2, 6, 9, None, 1, 5, 8]