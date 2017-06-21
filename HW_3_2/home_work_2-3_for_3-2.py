import json


def files_reading(file_name, cods='cp1251'):
    with open(file_name, encoding=cods) as f:
        d = json.load(f)
    return d


def countries_reading(country):
    if country == 'a':
        d = files_reading('newsafr.json', 'utf-8')
        print('В новостях из Африки:')
        return d
    if country == 'c':
        d = files_reading('newscy.json', 'koi8-r')
        print('В новостях из Кипра:')
        return d
    if country == 'f':
        d = files_reading('newsfr.json', 'iso8859-5')
        print('В новостях из Франции (хотя всё-таки из Кипра):')
        return d
    if country == 'i':
        d = files_reading('newsit.json')
        print('В новостях из Италии:')
        return d


def get_pure_words(feed):
    words = ''
    for descr in feed['rss']['channel']['item']:
        if type(descr['description']) == str:
            words += descr['description']
        else:
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


def repeat_massiv(pure_words):
    word_frequencies = dict()
    for word in pure_words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    return word_frequencies


def get_top_ten(d):
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
        print('слово -{0:s}- встречается {1:d} раз'.format(key_list[index], d[key_list[index]]))


def result():
    print('Для выяснения Топ-10 слов в новостях:')
    print('из Африки введите - a')
    print('из Кипра введите - c')
    print('из Франции введите - f')
    print('из Италии введите - i')
    country = input()
    feed = countries_reading(country)
    pure_words = get_pure_words(feed)
    word_frequencies = repeat_massiv(pure_words)
    get_top_ten(word_frequencies)


result()
