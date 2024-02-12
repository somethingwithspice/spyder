from vis_net.visual_github_network import *
import requests

user = "jmcapra"
base_url = "https://api.github.com/users/"
url = base_url + user
check = ["followers", "following"]



def get_users(main_account, type_):

    users = []
    
    req = requests.get(base_url + f"{main_account}/{type_}")
    result = req.json()
    
    for x in result:
        users.append(x['login'])
    
    return users


graph_skeleton = []

for x in get_users(user, "following"):
    graph_skeleton.append([x, get_users(x, "following")])

graphs = []
for x in graph_skeleton:
    graphs.append(create_graph(x[0], [], x[1]))

graph = combine_graphs(graphs)
draw_graph(graph)



