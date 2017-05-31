import json


def create_cook_book():
    with open('coo_book.json') as f:
        cook_book = json.load(f)
    cook_book_new = dict()
    for key, ingr in cook_book.items():
        dish = key.lower()
        cook_book_new[dish] = ingr
    cook_book = cook_book_new
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book()
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = ingridient
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчёте на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()