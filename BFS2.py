import json

with open('graph2.json') as file:
    graph = json.load(file)

path = []
for i in graph:
    #print (graph[i])
    for j in graph[i]:
        #print ('j is: ' , j)
        if j not in path:
            path.append(j)
            
print (path)

#print(json.dumps(sum_result, indent =4)

with open("path.json","w") as write_file:
    json.dump(path, write_file, indent =4)