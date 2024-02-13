from graph.helper.visual_github_network import *
import requests
import sys



def get_users(main_account, type_):

    users = []
    
    req = requests.get(f"https://api.github.com/users/{main_account}/{type_}")
    result = req.json()

    for x in result:
        users.append(x['login'])
    
    return users

def graph_depth_two():
    user = input("Give GitHub Account: ")
    
    
    following = get_users(user, "following")
    followers = get_users(user, "followers")
    graph = create_graph(user, followers, following)
    
    len_following = len(following)
    len_followers = len(followers)
    
    if len_following > 60 or len_followers > 60:
        print(f"Followers: {len_followers}  Following: {len_following}")
        user_input = input("Are you sure you want to continue? [y/n] ")
        if user_input.upper() not in ["Y", "YE", "YES", "YEA", "YEAH", "OK", "OKAY"]:
            sys.exit()
    
    graphs = []
    for x in range(len_following):
        sub_following = get_users(following[x], "following")
        sub_followers = get_users(following[x], "followers")
    
        if len(sub_following) < 60 and len(sub_followers) < 60:
            graphs.append(create_graph(following[x], sub_followers, sub_following))
        else:
            graphs.append(create_graph(following[x], sub_followers[:59], sub_following[:59]))
    
    for x in range(len_followers):
        sub_following = get_users(followers[x], "following")
        sub_followers = get_users(followers[x], "followers")
        
        if len(sub_following) < 60 and len(sub_followers) < 60:
            graphs.append(create_graph(followers[x], sub_followers, sub_following))
        else:
            graphs.append(create_graph(followers[x], sub_followers[:59], sub_following[:59]))
    
    
    
    graph = combine_graphs(graphs)
    draw_graph(graph)
    
    
