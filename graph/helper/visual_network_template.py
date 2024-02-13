import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = ["A", "B", "C", "D", "E", "F", "G"]
G.add_nodes_from(nodes)

edges = [
    ("A", "B"), ("A", "C"), ("A", "D"),
    ("C", "G"),
    ("D", "E"), ("D", "G"),
    ("E", "F"), ("A", "F"), ("A", "E")
]

G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

plt.axis("off")
plt.show()


