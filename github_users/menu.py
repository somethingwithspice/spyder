import github_users.style


def main_menu():
    options = 3 # Make sure to change this appropriately

    print(f"""{github_users.style.style.yellow}
     \_______/
 `.,-'\_____/`-.,'      ______   _______  ____  ____  ______   ________  _______     
  /`..'\ _ /`.,'\     .' ____ \ |_   __ \|_  _||_  _||_   _ `.|_   __  ||_   __ \\
 /  /`.,' `.,'\  \    | (___ \_|  | |__) | \ \  / /    | | `. \ | |_ \_|  | |__) |
/__/__/     \__\__\__  _.____`.   |  ___/   \ \/ /     | |  | | |  _| _   |  __ /
\  \  \     /  /  /   | \____) | _| |_      _|  |_    _| |_.' /_| |__/ | _| |  \ \_ 
 \  \,'`._,'`./  /     \______.'|_____|    |______|  |______.'|________||____| |___|          
  \,'`./___\,'`./
 ,'`-./_____\,-'`.
     /       \{github_users.style.style.end}""")
    
    print("\n")
    print(f"\t{github_users.style.style.red}[1]{github_users.style.style.end} Accumulate GitHub Accounts")
    print(f"\t{github_users.style.style.red}[2]{github_users.style.style.end} Scan GitHub Accounts")
    print(f"\t{github_users.style.style.red}[3]{github_users.style.style.end} GiHub Visual Graph")
    print(f"\t{github_users.style.style.red}[4]{github_users.style.style.end} Get Help")

    print()
    while True:
        user_input = input("Select: ")
        try:
            number = int(user_input)
            if number <= 0 or number > options:
                print(f"{github_users.style.style.red}Input must be between 1 and {options}{github_users.style.style.end}")    
            else:
                return number
        except ValueError as value:
            if user_input.upper() in ["EXIT", "EX", "QUIT", "Q", "END"]:
                print("...\n[exited]")
                return -1
            
            print(f"{github_users.style.style.red}{value} Input must be a number OR in ['exit', 'ex', 'quit', 'q', 'end']{github_users.style.style.end}")


