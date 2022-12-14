import linecache
import networkx as nx
import matplotlib.pyplot as plt
import prim as p

G = nx.Graph()
A=nx.Graph()

for y in p.lst_adj:
    if y[0]==y[1]:
        pass
    else:
        A.add_edge(p.dicionario[y[0]],p.dicionario[y[1]])

nx.draw_networkx(A,pos=nx.spring_layout(A),with_labels=True)  
plt.show()


for x in p.arvore_geradora:
    G.add_edge(p.dicionario[int(x[0])],p.dicionario[int(x[1])])

nx.draw_networkx(G,pos=nx.spring_layout(G),with_labels=True)
plt.show()

