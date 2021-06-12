""" create a sample graph as a dictionary
    Where the key is a node
    and values are next nodes"""

graph = { 'a' : ['b', 'c'],
          'b' : ['d', 'e'],
          'c' : ['f'],
          'd' : [],
          'e' : ['f','g'],
          'f' : [],
          'g' : ['a']
}

visited = [] # a list of all visited nodes
queue = []   # a temporary list 

def BFS (visited, graph, s_node ):
    visited.append(s_node) # s_node is the point where we start our visit
    queue.append(s_node)

    while queue: 
        s= queue.pop(0)
        print (s, end =' ')

        for next in graph[s]: #visit neighbours of graph[s]
            
            if next not in visited:
                visited.append(next) # if not visited, visit it
                queue.append (next)  # and added to the queue to visit its neighbours

print('BFS')
BFS(visited, graph, 'a') 
print()

