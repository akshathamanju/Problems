'''
Graph creation and various operations using python

1. Creation of graph using dictionaries
2. generating edges
3. Finding a path between 2 vertex/nodes
4. Finding the shortest path between 2 nodes
5. Determine cycles in the graph
6. Find isolated nodes
7. Add an edge
8. Find degree of vertex
9. Find degree of vertex
10. Find if the graph is connected or not

'''
#2. generating edges
def generate_edges(graph):
    edges = []
    for nodes in graph:
        for neighbour in graph[nodes]:
            edges.append((nodes, neighbour))
    return (edges)
#3. Finding a path between 2 vertex/nodes
def find_path_to_vertices(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path_to_vertices(graph, node, end, path)
            if newpath:
                return newpath
    return None
#4. Finding the shortest path between 2 nodes
def shortest_path_between_two_vertices(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest_path = None
    for node in graph[start]:
        if node not in path:
            newpath = find_path_to_vertices(graph, node, end, path)
            if newpath:
                if not shortest_path or len(shortest_path) > len(newpath):
                    shortest_path = newpath
    return shortest_path

#5. Determine cycles in the graph
def find_cycle_single_node(graph, start):
    for node in graph[start]:
        #if adjacent node is equal to start then there exists a cycle
        if node == start:
            return 1
    return 0
def find_all_paths(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    found_paths = []
    for node in graph[start]:
        if node not in path:
            newpath_find  = find_path_to_vertices(graph, node, end, path)
            for newpaths in newpath_find:
                found_paths.append(newpaths)
    return found_paths
#6. Find isolated nodes
def find_isolated_node(graph, start):
    isolated_node = []
    for node in graph:
        if not graph[node]:
            isolated_node.append(node)
    return isolated_node
#7. Add an edge
def add_an_edge(graph, edge):
    #
    edge = set(edge)
    (node1, node2) = tuple(edge)
    if node1  in graph:
        graph[node1].append(node2)
    else:
        graph[node1] = node2
    return graph
#8. Find degree of vertex
#degree means nmber of outgoing edges

def find_degree_of_vertex(graph, node):
    #number of neighbours will be equal to the number of degrees
    neighbours_present = []
    degree = 0
    for neighbour in graph[node]:
        neighbours_present.append(neighbour)
        degree = degree + 1
    return degree

#10. Find if the graph is connected or not
def find_graph_connected(graph, visited_node = None, start = None):
    if visited_node == None:
        visited_node = set()

    nodes = list(graph.keys())
    if not start:
        start = nodes[0]
    visited_node.add(start)
    if len(visited_node) < len(nodes):
        for other_nodes in graph[start]:
            if other_nodes not in visited_node:
                if find_graph_connected(graph, visited_node, other_nodes):
                    return True
    else:
        return True
    return False

#1. Creation of graph using dictionaries
if __name__ == '__main__':
    graph = {
        'A' : ['A', 'B', 'C'],
        'B' : ['C' ,'D'],
        'C' : ['D'],
        'D' : ['C'],
        'E' : ['F'],
        'F' : ['C'],
        'G' : [],
        'P' : []
        }
    print(graph['A'])
    print("The nodes/vertices of the graph: ",graph.keys(), "/n the edges of the graph: for key in keys(0) are {1}".format(graph.keys(), graph.values()))

    print("2. generated edges are :", generate_edges(graph))
    print("3. Finding a  path between 2 vertex/nodes :", find_path_to_vertices(graph, 'A', 'D', path = []))
    print("4. Finding the shortest path between 2 nodes: ",shortest_path_between_two_vertices(graph, 'A','D',path = []))
    print("5. Determine cycles in the graph : ")
    cycle_exists = find_cycle_single_node(graph, 'A')
    if cycle_exists:
        print("Cycle Present")
    else:
        print("No cycle Present")
    print("find all paths : ", find_all_paths(graph, 'A', 'D', path=[]))
    print("6. Find isolated nodes : ", find_isolated_node(graph, 'A'))
    print("7.add edge : ", add_an_edge(graph, {'A', 'E'}))
    degree_of_node = find_degree_of_vertex(graph, 'A')
    print("8. degree of vertex", degree_of_node)
    print("10. Find if the graph is connected or not : ")
    connection_present  = find_graph_connected(graph, visited_node = None, start = None)
    if connection_present:
        print("Graph is connected ")
    else:
        print("Graph is not connected ")