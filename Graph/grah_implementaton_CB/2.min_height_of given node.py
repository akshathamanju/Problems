def min_height(root, target):
    queue = [(root, 0)] # 0 is the starting height
    while queue:
        if node is not None:
            node, height = queue.dequeue()
            # return immediately since BFS finds the shortest path first
            if node.value == target:
                return height
            queue.enqueue((node.left, height + 1))
            queue.enqueue((node.right, height + 1))