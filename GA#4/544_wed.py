
n = 6
m = 5
roads = [(0,3) , (1,3) , (0,2) , (2,5) , (4,5)]

#def deleteDuplicates():
    
def produce2CNF(roads):
    crossRoads = []
    for i in range(m):
        for j in range(i+1,m):
            if roads[i][0] < roads[i][1]:
                temp_i = roads[i]
            else:
                temp_i[0] = roads[i][1]
                temp_i[1] = roads[i][0]
            if roads[j][0] < roads[j][1]:
                temp_j = roads[j]
            else:
                temp_j[0] = roads[j][1]
                temp_j[1] = roads[j][0]
            if (temp_i[0] < temp_j[0] and temp_j[0] < temp_i[1] and temp_i[1] < temp_j[1]) or (temp_j[0] < temp_i[0] and temp_i[0] < temp_j[1] and temp_j[1] < temp_i[1]):
                crossRoads.append((i,j+m))
                crossRoads.append((i+m,j))
    return crossRoads
    
def implicationGraphTransformation(cnf2):
    graph = [[] for i in range(2*m)]
    
    while (len(cnf2) > 0):
        temp = cnf2.pop()
        
        if temp[0] > m-1: 
            graph[temp[0]-m].append(temp[1])
            
        else:
            graph[temp[0]+m].append(temp[1])
            
        if temp[1] > m-1:
            graph[temp[1]-m].append(temp[0])
            
        else:
            graph[temp[1]+m].append(temp[0])
                                    
    return graph 
   

def findStronglyConnectedComponents(graph):
    count = 0
    stronglyConnectedComponents = [None]*2*m
    for node in graph:
        if len(node) > 0:
            temp = node.pop()
            
    return null

def checkStronglyConnectedComponents(stronglyConnectedComponents):
    if cmp(stronglyConnectedComponents[0], stronglyConnectedComponents[10]) == 0:
        return false
    return true


cnf2 = produce2CNF(roads)
print(cnf2)
graph = implicationGraphTransformation(cnf2)
print(graph)
#stronglyConnectedComponents = findStronglyConnectedComponents(graph)
#answer = checkStronglyConnectComponents(temp)
