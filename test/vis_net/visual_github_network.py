import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



def create_graph(main_account, followers, following):
    G = nx.Graph()

    # Initially add the main account with a temporary color
    G.add_node(main_account, color="temp")

    # Track mutual relationships
    mutuals = set(followers) & set(following)

    # Add followers
    for follower in followers:
        color = 'purple' if follower in mutuals else 'lightblue'
        G.add_node(follower, color=color)
        G.add_edge(main_account, follower)

    # Add following
    for following_ in following:
        color = 'purple' if following_ in mutuals else 'red'
        # Check if the node exists to possibly update the color to purple
        if following_ in G.nodes():
            G.nodes[following_]['color'] = color
        else:
            G.add_node(following_, color=color)
        G.add_edge(main_account, following_)

    # Update the main account color last to ensure it's accurate
    # If the main account has mutual relationships, set it to purple
    if main_account in mutuals:
        G.nodes[main_account]['color'] = 'purple'
    else:
        G.nodes[main_account]['color'] = 'lightgreen'

    return G



def combine_graphs(graphs):
    combined_graph = nx.Graph()
    for graph in graphs:
        combined_graph = nx.compose(combined_graph, graph)
    return combined_graph


def draw_graph(graph):
    pos = nx. spring_layout(graph, seed=42)
    
    node_colors = [graph.nodes[node]['color'] for node in graph.nodes()]
    
    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color=node_colors)
    nx.draw_networkx_edges(graph, pos, width=1, alpha=0.6, edge_color="black")
    nx.draw_networkx_labels(graph, pos, font_size=10)
    
    color_legend = [
        mpatches.Patch(color='lightgreen', label='Main Account'),
        mpatches.Patch(color='lightblue', label='Followers'),
        mpatches.Patch(color='red', label='Following'),
        mpatches.Patch(color='purple', label='Both Followers and Following')
    ]
    plt.legend(handles=color_legend, loc='upper left')

    plt.axis("off")
    plt.show()


