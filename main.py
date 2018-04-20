import networkx as nx
import csv
import matplotlib.pyplot as plt
import pants as pants
import math as math
routes = []

#opened_csv = 'VOIES_NM.csv'
opened_csv = 'small.csv'

G=nx.Graph()


def getBpBi(row):
    if (row[10] != ''):
        return row[10]
    elif (row[11] != ''):
        return row[11]


def ifImpasse(row, num):
    if (row[num] == 'Impasse'):
        return 'impasse-' + row[5]
    elif(row[num] != ''):
        return row[num]
    else:
        return 'impasse-'+ row[5]


with open(opened_csv, 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)
    for row in reader:
        if(row[4] == "NANTES" and (row[10] != '' or row[10] != '')):
            G.add_edge(ifImpasse(row, 6), ifImpasse(row, 7),weight=int(getBpBi(row)), name=row[1])


pos=nx.spring_layout(G) # positions for all nodes

nx.draw(G,pos)
# specifiy edge labels explicitly
edge_labels=dict([((u,v,),d['name'])
             for u,v,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display

nodes = []
nodes.append(nx.shortest_path_length(G, "NANTES Quai de la Fosse", "NANTES Rue Flandres Dunkerque 40", "weight"))
nodes.append(nx.shortest_path_length(G, "NANTES Quai de la Fosse", "NANTES Rue de la Brasserie", "weight"))

def euclidean(a, b):
    return math.sqrt(pow(a, 2) + pow(b, 2))

world = pants.World(nodes, euclidean)
solver = pants.Solver()
solution = solver.solve(world)

print(nodes)
print(solution.path)


