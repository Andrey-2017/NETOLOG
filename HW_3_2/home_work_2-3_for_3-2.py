import json


def french_reading():
    with open('newsfr.json', encoding='iso8859-5') as f:
        d = json.load(f)
    print('В новостях из Франции (хотя всё-таки из Кипра):')
    return d


def africa_reading():
    with open('newsafr.json', encoding='utf-8') as f:
        d = json.load(f)
    print('В новостях из Африки:')
    return d


def cyprus_reading():
    with open('newscy.json', encoding='koi8-r') as f:
        d = json.load(f)
    print('В новостях из Кипра:')
    return d


def italy_reading():
    with open('newsit.json') as f:
        d = json.load(f)
    print('В новостях из Италии:')
    return d


def countries_reading(country):
    if country == 'a':
        d = africa_reading()
        return d
    if country == 'c':
        d = cyprus_reading()
        return d
    if country == 'f':
        d = french_reading()
        return d
    if country == 'i':
        d = italy_reading()
        return d


def get_pure_words():
    country = input()
    feed = countries_reading(country)
    if country == 'i':
        words = ''
        for descr in feed['rss']['channel']['item']:
            words += descr['description']
        words = words.split(' ')
        pure_words = list()
        for strings in words:
            pure_word = strings.strip(',.()!/:;')
            if len(pure_word) >= 6:
                if 'href' not in pure_word:
                    if '<br>' not in pure_word:
                        if 'www' not in pure_word:
                            pure_words.append(pure_word.lower())
        return pure_words
    else:
        words = ''
        for descr in feed['rss']['channel']['item']:
            words += descr['description']['__cdata']
        words = words.split(' ')
        pure_words = list()
        for strings in words:
            pure_word = strings.strip(',.()!/:;')
            if len(pure_word) >= 6:
                if 'href' not in pure_word:
                    if '<br>' not in pure_word:
                        if 'www' not in pure_word:
                            pure_words.append(pure_word.lower())
        return pure_words


def repeat_massiv():
    pure_words = get_pure_words()
    d = dict()
    l = list()
    for word in pure_words:
        i = 0
        if word not in l:
            for strings in pure_words:
                if strings == word:
                    i += 1
            d[word] = i
            l = d.keys()
    return d


def get_top_ten():
    d = repeat_massiv()
    value_list = []
    key_list = []
    for value in d.values():
        if value not in value_list:
            value_list.append(value)
    value_list.sort(reverse=True)
    for value in value_list:
        for key in d.keys():
            if d[key] == value:
                key_list.append(key)
        key_list = key_list[:10]
    for index in range(len(key_list)):
        print('слово-', key_list[index], '-встречается', d[key_list[index]], 'раз')


def result():
    print('Для выяснения Топ-10 слов в новостях:')
    print('из Африки введите - a')
    print('из Кипра введите - c')
    print('из Франции введите - f')
    print('из Италии введите - i')
    get_top_ten()


result()
