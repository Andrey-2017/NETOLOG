import requests
import time
import os
import json
from urllib.parse import urlencode


# authorize_url = 'https://oauth.vk.com/authorize'
# version = '5.67'
# app_id = '6083107'
# auth_data = {
#         'client_id': app_id,
#         'response_type': 'token',
#         'scope': 'friends',
#         'v': version
#         }
#
# print('?'.join((authorize_url, urlencode(auth_data))))


token = 'e38c31b95bcb3f4789d7f8a6c9b6a8b9e2e7e61707f20c7d9672034e7f64298f4c010ea6bd8650b3134d1'


def get_list(meth, id, param=(('extended', 1), ('fields', 'members_count'))):
    params = {
        'access_token': token,
        'v': '5.67',
        'user_id': id
        }
    params.update(param)
    response = requests.post('https://api.vk.com/method/' + meth, params)
    try:
        _list = response.json()['response']['items']
    except KeyError:
        _list = []
    return _list


def get_alone_groups_list(friends_list, groups_list, meth='groups.get'):
    user_alone_id_groups_list = set([l['id'] for l in groups_list])
    i = 0
    for friend in friends_list:
        friend_groups_list = get_list(meth, friend)
        time.sleep(0.4)
        i +=1
        print('---')
        print('Осталось {0} обращений к API'.format(len(friends_list) - i))
        id_groups_friends_list = set([l['id'] for l in friend_groups_list])
        intersec = user_alone_id_groups_list & id_groups_friends_list
        user_alone_id_groups_list = user_alone_id_groups_list - intersec
    alone_group_list = [l for l in groups_list if l['id'] in list(user_alone_id_groups_list)]
    return alone_group_list


def result():
    id = 'tim_leary'
    if type(id) == str:
        params = {
            'access_token': token,
            'v': '5.67',
            'user_ids': id
            }
        response = requests.get('https://api.vk.com/method/users.get', params)
        id = response.json()['response'][0]['id']
    friends_list = get_list('friends.get', id, param=())
    groups_list = get_list('groups.get', id)
    alone_group_list = get_alone_groups_list(friends_list, groups_list)
    file_name = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'groups.json')
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'w') as f:
        json.dump(alone_group_list, f)
    print('Программа закончила работу!')
    print('Количество групп без друзей - {0}'.format(len(alone_group_list)))


result()
