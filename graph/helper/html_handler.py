import requests
import re


def get_users(main_account, type_):
    users = []
    pattern = '<a class="d-inline-block" data-hovercard-type="user" data-hovercard-url="/users/(.+?)/'
    
    for x in range(1, 100):
           
        url = f"https://github.com/{main_account}?page={x}&tab={type_}"
    
        result = requests.get(url)
        
        if result.status_code == 200:
            lines = result.text.split("\n")
            counter = 0
            for line in lines:
                username = re.search(pattern, line)
                if username:
                    users.append(username.group(1))
                    counter += 1
            if counter == 0:
                break
        else:       
            print("404 SITE NOT FOUND")
            break
    
    return users
    

