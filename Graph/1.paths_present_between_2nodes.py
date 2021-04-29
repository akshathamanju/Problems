from collections import deque
from buildAdjList import buildAdjList
from buildAdjList import prettyPrint

# time O(N*N)
#space O(N) -> incase queue has all the elemnts
def BFS(adj_list, source, target):

    queue= deque()
    queue.append(source)
    seen = set(source)
    #time O(N)
    while queue:
        cur = queue.pop()
        if cur == target:
            return True
        #time : O(N)
        for neighbor in adj_list(cur):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return False

'''
DFS approach
start at hermia 
end at Oberon 
return False as there is no connection
'''
#is there a path from this node to this node
def DFS(adj_list, source, target):
    pass

if __name__ == '__main__':
    love_connections = [("Lysander", "Helena"), ("Hermia", "Lusander"),
                        ("Demetrius", "Hermia"), ("Helena","demetrius"),
    ("Titania","Oberon"),("Oberon", "TItania"),("Puck", "Puck"), ("Lysander", "Puck")]

    #directed adjacency list
    adj_list = buildAdjList(love_connections)
    graph_repr = prettyPrint(love_connections)
    BFS(adj_list, "Lysander", "Helena" )



