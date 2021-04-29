def grid_bfs(grid):
    N = len(grid)
    visited = set()
    if ally_color == “ “:
        return True
    queue = Queue()
    queue.enqueue((0,0))
    directions = [(-1,0), (1,0), (0,1), (0, -1)]
    while queue:
        i,j = queue.dequeue()
        visited.add((i,j))
        # add logic to do something with i,j
        for x,y in directions:
            # check if it’s in visited
            new_i, new_j = i + x, j + y
            if (new_i, new_j) not in visited:
                # Check that it’s in bounds
                if 0 <= new_i < N and 0 <= new_j < N:
                    # Enqueue or add other checks if necessary.
                    queue.enqueue((new_i, new_j))