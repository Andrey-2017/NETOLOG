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
    token = '70aa16b94d18757b6b90e235a065d59749c738edb46866efe04b2c906aa0d29002b4c6ebd7cde08031d3b'
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
    common_friends = [x for x in friends_friends_list[0]]
    for item in friends_friends_list[0]:
        a = []
        for list in friends_friends_list[1:]:
            if item in list:
                a.append(1)
            else:
                a.append(0)
        if 0 in a:
            common_friends.remove(item)
    print('Список id общих друзей моих друзей - {0}'.format(common_friends))


get_common_friends()
