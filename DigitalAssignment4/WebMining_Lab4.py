# importing libraries 
import networkx as nx 
import matplotlib.pyplot as plt 
G = nx.DiGraph()
G.add_edge('Imperial Spice', 'Indian Grill') 
G.add_edge('Imperial Spice', 'King of Spices')
G.add_edge('Imperial Spice', 'Shahi Darbar') 
G.add_edge('Shahi Darbar', 'Imperial Spice') 
G.add_edge('Indian Grill', 'Mughlai Darbar') 
G.add_edge('Mughlai Darbar', 'Indian Grill') 
G.add_edge('Shahi Darbar', 'Cardamom') 
G.add_edge('Mughlai Darbar', 'Cardamom')

nx.draw_planar(G, with_labels = True) 
plt.savefig("graph.png")

c = {} 
for n in G.nodes: 
    c[n] = G.out_degree(n) 
print("Out degree of each node :", c) 
# create index of inbound links of every node 
inedge = {} 
for n in G.nodes: 
    inedge[n] = [] 
    for edge in G.in_edges: 
        if edge[1] == n: 
            inedge[n].append(edge[0]) 
            print("Inbound links of each node :",inedge)
pr = {}
for n in G.nodes:
    pr[n]=1
print(pr)
# set damping factor and number of iterations
df = 0.8
max_iter = 10
# stop after 10 iterations
while max_iter>0:
    new_pr = {}
    for n in G.nodes:
        influence = 0
        for edge in inedge[n]:
            influence += pr[edge]/c[edge]
        new_pr[n] = (1-df) + (df*influence)
        # round up the value
        new_pr[n] = round(new_pr[n], 2)
pr = new_pr
print(pr)
max_iter -= 1