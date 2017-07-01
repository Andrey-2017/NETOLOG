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


class MetrikaBase:
    api_management_url = 'https://api-metrika.yandex.ru/management/v1/'
    api_stat_url = 'https://api-metrika.yandex.ru/stat/v1/'


    def __init__(self, tok):
        self.token = tok


    def get_headers(self):
        return {
            'Authorization': 'OAuth {0}'.format(self.token),
            'Content-Type': 'application/json'
        }


class YandexMetrika(MetrikaBase):
    def get_counters(self):
        headers = self.get_headers()
        r = requests.get(self.api_management_url + 'counters', headers=headers)
        return [Counter(self.token, counter['id']) for counter in r.json()['counters']]


class Counter(MetrikaBase):
    def __init__(self, tok, iden):
        self.counter_id = iden
        super().__init__(tok)



    def get_visits(self):
        headers = self.get_headers()
        params = {
            'id': self.counter_id,
            'metrics': 'ym:s:visits'
        }
        r = requests.get(self.api_stat_url + 'data', params, headers=headers)
        return r.json()['data']


    def get_pageviews(self):
        headers = self.get_headers()
        params = {
            'id': self.counter_id,
            'metrics': 'ym:s:pageviews'
        }
        r = requests.get(self.api_stat_url + 'data', params, headers=headers)
        return r.json()['data']


    def get_users(self):
        headers = self.get_headers()
        params = {
            'id': self.counter_id,
            'metrics': 'ym:s:users'
        }
        r = requests.get(self.api_stat_url + 'data', params, headers=headers)
        return r.json()['data']


ident = YandexMetrika(token)
iden = ident.get_counters()
for counter in iden:
    print('Количество посетителей {0}'.format(counter.get_visits()))
    print('Количество просмотров {0}'.format(counter.get_pageviews()))
    print('Количество новых посетителей {0}'.format(counter.get_users()))
