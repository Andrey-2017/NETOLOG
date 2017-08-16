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


token = '3d8873921dfa091c2932d494fa5993478be108e73026fbc7ae190287d8512ed4019e425df3d3a1eb4b02d'


def get_list(meth, param):
    params = {
        'access_token': token,
        'v': '5.67'
        }
    params.update(param)
    response = requests.post('https://api.vk.com/method/' + meth, params)
    return response.json()['response']


def convert_friends_list(friends_list):
    if len(friends_list) <= 500:
        f_id = []
        s = [str(a) for a in friends_list]
        s = ','.join(s)
        f_id.append(s)
    else:
        k = 500
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
        b = get_list('groups.isMember', {'group_id': g_id, 'user_ids': l})
        time.sleep(0.3)
        a += b
    return a


def result():
    id = 'tim_leary'
    if type(id) == str:
        id = get_list('users.get', {'user_ids': id})[0]['id']
    groups_list = get_list('groups.get', {'user_id': id, 'extended': 1, 'fields': 'members_count'})['items']
    friends_list = get_list('friends.get', {'user_id': id})['items']
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
