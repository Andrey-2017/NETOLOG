import requests
import json
from urllib.parse import urlencode


# authorize_url = 'https://oauth.vk.com/authorize'
# version = '5.67'
# app_id = '6083107'
# auth_data = {
#        'client_id': app_id,
#        'response_type': 'token',
#        'scope': 'friends',
#        'v': version
#    }
#
# print('?'.join((authorize_url, urlencode(auth_data))))


def get_friends_list(id, token):
    params = {
    'access_token': token,
    'v': '5.67',
    'user_id': id
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    friends_list = response.json()['response']['items']
    return friends_list


def get_groups_list(id, token):
    params = {
    'access_token': token,
    'v': '5.67',
    'user_id': id,
    'extended': 1,
    'fields': 'members_count'
    }
    response = requests.get('https://api.vk.com/method/groups.get', params)
    try:
        groups_list = response.json()['response']['items']
    except KeyError:
        groups_list = []
    return groups_list


def alone_groups_list(friends_list, groups_list, token):
    user_alone_id_groups_list = []
    for l in groups_list:
        user_alone_id_groups_list.append(l['id'])
    i = 0
    for friend in friends_list:
        friend_groups_list = get_groups_list(friend, token)
        i +=1
        print('---')
        print('Осталось {0} обращений к API'.format(len(friends_list) - i))
        id_groups_friends_list = []
        for l in friend_groups_list:
            id_groups_friends_list.append(l['id'])
        intersec = set(user_alone_id_groups_list) & set(id_groups_friends_list)
        user_alone_id_groups_list = list(set(user_alone_id_groups_list) - intersec)
    alone_group_list = []
    for item in user_alone_id_groups_list:
        for l in groups_list:
            if l['id'] == item:
                alone_group_list.append(l)
    return alone_group_list


def result():
    id = 5030613
    token = '03317cedf04ba95b551d0ed42459f796cb744da5122209b63f8dde359289b0726f843bbbea3accf727476'
    friends_list = get_friends_list(id, token)
    groups_list = get_groups_list(id, token)
    alone_group_list = alone_groups_list(friends_list, groups_list, token)
    with open('groups.json', 'w') as f:
        json.dump(alone_group_list, f)


result()
