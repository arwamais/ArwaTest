import json

with open('directedgraph.json') as file:
    graph = json.load(file)

#print (graph)
first = int(graph['from'])
last = int(graph['to'])
path = []
path.append(first)
found_last = False 

my_graph = graph['directed_graph']
for i in my_graph:
    
    #print (my_graph[i])
    for j in my_graph[i]:
        #print ('j is: ' , j)
        if j not in path and not found_last:
            path.append(j)
            if j == last:
                found_last = True
            
print (path)

#print(json.dumps(sum_result, indent =4)

with open("path.json","w") as write_file:
    json.dump(path, write_file, indent =4)