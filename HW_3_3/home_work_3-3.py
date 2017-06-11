import requests
import os


def translate_it(text_place, translate_place, to_lang, lang='ru'):
    api_key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        "key": api_key,
        "text": '',
        "lang": '{0:s}-{1:s}'.format(to_lang, lang)
    }
    first_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), text_place)
    end_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), translate_place)
    for file_name in os.listdir(first_dir):
        if to_lang in file_name.lower():
            with open(os.path.join(first_dir, file_name)) as f:
                params['text'] = f.read()
            response = requests.get(url, params=params)
            json_ = response.json()
            trans_text = ''.join(json_['text'])
            with open(os.path.join(end_dir, file_name), 'w') as f:
                f.write(trans_text)
            break


def get_translating():
    text_place = 'Initial'
    translate_place = 'Final'
    print('Введите язык, с которого нужно перевести текст (de - немецкий, fr - французский, es - испанский:)')
    to_lang = input()
    translate_it(text_place, translate_place, to_lang, lang='ru')


get_translating()
