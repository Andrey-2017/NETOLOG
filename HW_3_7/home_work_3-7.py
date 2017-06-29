import requests
from urllib.parse import urlencode


authorize_url = 'https://oauth.yandex.ru/authorize'
app_id = '042093aaafe74802957290d256f0e42e'
auth_data = {
    'client_id': app_id,
    'response_type': 'token'
}


#print('?'.join((authorize_url, urlencode(auth_data))))


token = 'AQAAAAAFd7GFAARjTMGJZHT_N0-9rIYCfdkWgdI'


class YandexMetrika:
    api_management_url = 'https://api-metrika.yandex.ru/management/v1/'
    token = None

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {0}'.format(self.token),
            'Content-Type': 'application/json'
        }



    def get_counters(self):
        headers = self.get_headers()
        r = requests.get(self.api_management_url + 'counters', headers)
        return r.json()






class Counter:








