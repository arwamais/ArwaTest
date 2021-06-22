import json
# this little code opens a json file called twonum.json
# adds the two numbers inside it 
# and outputs the results to a json file called result.jsom

with open('twonum.json') as file:
    values = json.load(file)

sum = 0
for i in values:
    sum += float(values[i]) 

#print (sum)

sum_result ={"sum": sum}
#print(json.dumps(sum_result, indent = 4))

with open("result.json","w") as write_file:
    json.dump(sum_result, write_file, indent =4)