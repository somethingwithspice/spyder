from graph.helper.visual_github_network import *
from graph.helper.html_handler import *
import sys


def sub_users_help(main_account_asoc_users, length_sub_usrs):
    graphs = []

    for x in range(length_sub_usrs):
        sub_following = get_users(main_account_asoc_users[x], "following")
        sub_followers = get_users(main_account_asoc_users[x], "followers")
   
        if len(sub_following) > 300:
            sub_following = sub_following[:299]
        if len(sub_followers) > 300:
            sub_followers = sub_followers[:299]
        
        graphs.append(create_graph(main_account_asoc_users[x], sub_followers, sub_following))
    
    return graphs
 

def graph_depth_two():
    user = input("Give GitHub Account: ")
    
    
    following = get_users(user, "following")
    followers = get_users(user, "followers")
    graph = create_graph(user, followers, following)
    
    len_following = len(following)
    len_followers = len(followers)
    
    if len_following > 100 or len_followers > 100:
        print(f"Followers: {len_followers}  Following: {len_following}")
        user_input = input("Are you sure you want to continue? [y/n] ")
        if user_input.upper() not in ["Y", "YE", "YES", "YEA", "YEAH", "OK", "OKAY"]:
            sys.exit()
    
    graphs = []
    graphs.extend(sub_users_help(following, len_following))
    graphs.extend(sub_users_help(followers, len_followers)) 
    
    graph = combine_graphs(graphs)
    draw_graph(graph)
    
    
