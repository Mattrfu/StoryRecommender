import re
import networkx as nx
all_data = []

with open("SortedSim") as sim:
    for line in sim:
        data = (re.sub("\(|\)|\n", "", line))
        all_data.append(data.split(", "))

def getPeeps(points):
    toReturn = []
    for [a, b] in points:
        if a not in toReturn:
            toReturn.append(a)
        if b not in toReturn:
            toReturn.append(b)
    return toReturn

def get_starting_graph(data):
    points = data[0]
    no_linked_lists = []
    for n in data[1:]:
        peeps = getPeeps(points)
        if (n[0] in peeps) ^ (n[1] in peeps):
            points.append(n)
        if (n[0] not in peeps) and (n[1] not in peeps):
            no_linked_lists.append(n)

    added = True
    while added:
        added = False
        for n in no_linked_lists:
            peeps = getPeeps(points)
            if (n[0] in peeps) ^ (n[1] in peeps):
                points.append(n)
                no_linked_lists.remove(n)
                added = True
            elif (n[0] in peeps) and (n[1] in peeps):
                no_linked_lists.remove(n)
    return points

def grow(data):
    edges = list()
    index = 0
    for n in data:
        peeps = getPeeps(edges)
        if n[0] not in peeps and n[1] not in peeps:
            edges.append(n)
        elif (n[0] in peeps) ^ (n[1] in peeps):
            edges.append(n)
        index+=1
        if(index%1000==0):
            print(index)
    return edges

edges = []
data = []
with open("Graph") as graph:
    for line in graph:
        data = line.split("], [")
for entry in data:
    item = entry.split(", ")
    edges.append([item[0],item[1],int(item[2])])
print(edges)
graph = nx.Graph()
graph.add_weighted_edges_from(edges)
nx.write_graphml(graph, "min_span_no_ask.graphml")