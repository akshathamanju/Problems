from collections import Deque


class GraphNode:
    # returns the node's neighbors
    # the implementation depends on graph stucture
    def get_neighbors(self):
        pass


# source, target are GraphNodes
# returns True if there exists a path between source and target.
def bfs(graph_traversal_method, source, target):
    visited_nodes = set()  # set of visited nodes so we don't revisit nodes we have already seen

    # Use a Queue since BFS. Here we use a doublyended Queue
    nodes_to_visit = Deque()

    # start from the source Node
    nodes_to_visit.append(source)

    while nodes_to_visit.isNotEmpty():
        # gets next Node from nodes_to_visit and removes from list
        current_node = nodes_to_visit.popleft()
        if current_node is target:
            return True
        visited_nodes.add(current_node)  # mark current_node as visited
        # add current_node's neighbors to visit if they haven't already
        for neighbor in current_node.get_neighbors():
            if neighbor not in visited_nodes:
                nodes_to_visit.add(neighbor)

    # if we search all the neighbors and do not find the target return False
    return False