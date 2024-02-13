import sys
import github_users.menu
import graph.visual_network


if __name__ == "__main__":
    user_choice = github_users.menu.main_menu()
    match user_choice:
        case 1:
            print("Not Defined")
        case 2:
            print("Not Defined")
        case 3:
            graph.visual_network.graph_depth_two()
        case 4:
            print("Not Defined")
        case _:
            print("Bye Bye!")
            sys.exit()

