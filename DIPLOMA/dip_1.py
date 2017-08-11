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


token = '376cdb7b1efa953bb1264b3517d2ad7e4b075506e809b4244329d11ca2131dd97bea6c4acdd8af6a0189d'


def get_list(meth, id):
    if type(id) == str:
        params = {
            'access_token': token,
            'v': '5.67',
            'user_ids': id
            }
        response = requests.get('https://api.vk.com/method/users.get', params)
        id = response.json()['response'][0]['id']
    if meth == 'groups.get':
        params = {
            'access_token': token,
            'v': '5.67',
            'user_id': id,
            'extended': 1,
            'fields': 'members_count'
            }
    else:
        params = {
            'access_token': token,
            'v': '5.67',
            'user_id': id
            }
    response = requests.get('https://api.vk.com/method/' + meth, params)
    _list = response.json()['response']['items']
    return _list


def convert_friends_list(friends_list):
    if len(friends_list) <= 500:
        f_id = []
        s = [str(a) for a in friends_list]
        s = ','.join(s)
        f_id.append(s)
    else:
        k = 353
        n = len(friends_list) // k
        M = [friends_list[k * i:k * (i + 1)] for i in range(n)]
        M.append(friends_list[k * n:])
        f_id = []
        for l in M:
            s = [str(a) for a in l]
            s = ','.join(s)
            f_id.append(s)
    return f_id


def member_group_list(g_id, f_id):
    a = []
    for l in f_id:
        params = {
        'access_token': token,
        'v': '5.67',
        'group_id': g_id,
        'user_ids': l
        }
        response = requests.get('https://api.vk.com/method/groups.isMember', params)
        time.sleep(0.3)
        a += response.json()['response']
    return a


def result():
    id = 'tim_leary'
    groups_list = get_list('groups.get', id)
    friends_list = get_list('friends.get', id)
    f_id = convert_friends_list(friends_list)
    group_list = [i['id'] for i in groups_list]
    m = 0
    for g in groups_list:
        member_list = member_group_list(g['id'], f_id)
        time.sleep(0.5)
        m += 1
        print('---')
        print('Осталось {0} обращений к API'.format(len(groups_list) - m))
        for l in member_list:
            if l['member'] == 1:
                group_list.remove(g['id'])
                break
    alone_groups_list = [l for l in groups_list if l['id'] in group_list]
    file_name = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'groups.json')
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'w') as f:
        json.dump(alone_groups_list, f)
    print('Программа закончила работу!')
    print('Количество групп без друзей - {0}'.format(len(alone_groups_list)))


result()
