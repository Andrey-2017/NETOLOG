import osa
import os


def temp(x):
    def temp_convert(t):
        url = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
        client = osa.client.Client(url)
        response = client.service.ConvertTemp(Temperature=t, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')
        return response


    list_temp = []
    with open(x) as f:
        for line in f:
            line = (line.rstrip()).rstrip(' F')
            list_temp.append(int(line))
    aver_temp = temp_convert(sum(list_temp) / len(list_temp))
    print('Средняя температура за неделю составила {0:.0f} градусов по Цельсию.'.format(aver_temp))


def distance(y):
    def lenght_convert(l):
        url = 'http://www.webservicex.net/length.asmx?WSDL'
        client = osa.client.Client(url)
        response = client.service.ChangeLengthUnit(LengthValue=l, fromLengthUnit='Miles', toLengthUnit='Kilometers')
        return response


    list_di = []
    with open(y) as f:
        for line in f:
            line = (line.rstrip()).rstrip('mi')
            list_di.append(line)
    li_di = ''.join(list_di)
    li_di = li_di.split(' ')
    list_dist = []
    for item in range(len(li_di)):
        if item % 2:
            li_di[item] = li_di[item].split(',')
            li_di[item] = ''.join(li_di[item])
            list_dist.append(float(li_di[item]))
    common_distance = lenght_convert(sum(list_dist))
    print('Общая длина путешествия составила {0:.2f} километров.'.format(common_distance))


def val(z):
    def curr_convert(a, val_name):
        url = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
        client = osa.client.Client(url)
        response = client.service.ConvertToNum(fromCurrency=val_name, toCurrency='RUB', amount=a, rounding=1)
        return response


    list_cu = []
    with open(z) as f:
        for line in f:
            line = (line.rstrip()).split(' ')
            list_cu.append(line[1:])
    am = 0
    for item in list_cu:
        am += curr_convert(int(item[0]), item[1])
    print('Общая стоимость путешествия составила {0:.0f} рублей.'.format(am))


def result():
    print('Если Вы хотите узнать среднюю температуру за неделю, введите 1')
    print('Если Вы хотите узнать общую длину путешествия, введите 2')
    print('Если Вы хотите узнать общую стоимость путешествия, введите 3')
    key = input()
    if key == '1':
        x = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temps.txt')
        temp(x)
    if key == '2':
        y = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'travel.txt')
        distance(y)
    if key == '3':
        z = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'currencies.txt')
        val(z)


result()
