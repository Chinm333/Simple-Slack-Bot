from time import sleep
from slack import WebClient
# webclient for the interaction b/w slack and code
client =WebClient("BOT_TOKEN")
def user_details():
    users_call = client.users_list()
    users = users_call['members']
    result = []
    # print(users_call)
    # loop for each user
    for user in users:
        uid = user['id'] 
        name = user['profile']['real_name']
        info = {"id": None, "name": None}
        if users_call['ok']:  
            info['id'] = uid
            info['name'] = name
            result.append(info)
        else:
            return None
    res = list(filter(lambda person: person['name'] == account_Name, result))
    return res
def user_activeORNot():            
    users = user_details()
    for user in users:
        presence_call = client.users_getPresence(user = user['id'])
        sleep(1)
        if presence_call['ok']:
            user['presence'] = presence_call['presence']
        else:
            user['presence'] = None
    if len(users)==0:
        return f"There is no account in the name of {account_Name}, please enter the name correctly"
    return users
account_Name = input("Please enter the account name \n") 
# print(user_details())
print(user_activeORNot())

