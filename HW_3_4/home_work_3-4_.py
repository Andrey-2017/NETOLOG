import requests
from urllib.parse import urlencode


authorize_url = 'https://oauth.vk.com/authorize'
version = '5.65'
app_id = '6083107'
auth_data = {
    'client_id': app_id,
    'response_type': 'token',
    'scope': 'friends',
    'v': version
}

#print('?'.join((authorize_url, urlencode(auth_data))))


def get_friends_list(id):
    token = '17612b8454bd135e842335f6b46f49bd27819d64de9a487afa995b51c072320b02a99e2d9ab478fd214a9'
    params = {
    'access_token': token,
    'v': version,
    'user_id': id
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    friends_list = response.json()['response']['items']
    return friends_list


def get_common_friends():
    my_id = 347720752
    my_friends_list = get_friends_list(my_id)
    friends_friends_list = []
    for item in my_friends_list:
        friends_friends_list.append(get_friends_list(item))
    intercec = [x for x in friends_friends_list]
    i = 0
    while i < len(friends_friends_list) - 1:
        intercec[0] = list(set(intercec[0]) & set(intercec[1]))
        intercec.pop(1)
        i += 1
    print('Список id общих друзей моих друзей - {0}'.format(intercec[0]))


get_common_friends()
