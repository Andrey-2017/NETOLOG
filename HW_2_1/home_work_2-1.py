def create_cook_book():       # Создаёт из текстового файла "книгу рецептов"
    cook_book = {}
    parameters_keys_list = ['ingredient_name', 'quantity', 'measure']
    with open('cooking_book.txt') as f:
        for line in f:
            dish_name = line.lower().strip()
            while not dish_name:
                dish_name = f.readline().lower().strip()
            quantity_ingredient = int(f.readline())
            ingredient_list = []
            for i in range(quantity_ingredient):
                parameters_ingredient_list = []
                parameters_ingredient_list_ = f.readline().lower().strip().split('|')
                for ing in parameters_ingredient_list_:
                    parameters_ingredient_list.append(ing.strip())
                parameters_ingredient_list[1] = int(parameters_ingredient_list[1])
                ingredients = dict(zip(parameters_keys_list, parameters_ingredient_list))
                ingredient_list.append(ingredients)
                cook_book[dish_name] = ingredient_list
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