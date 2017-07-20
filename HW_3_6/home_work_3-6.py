class Animal:
    def __init__(self, name):
        self.name = name


    common_name = 'домашнее животное'
    area = 'ферма'
    kind = 'скот и птица'


    def feeding(self):
        print('Животное нужно кормить!')


    def eating(self):
        print('Животное можно есть!')
        
    
class Cow(Animal):
    subarea = 'хлев'
    voice = 'му'


    def milking(self):
        print('Животное можно доить!')


class Pig(Animal):
    subarea = 'свинарник'
    voice = 'хрю'


    def get_fat(self):
        print('Приготовление сала!')


class Sheep(Animal):
    subarea = 'овчарня'
    voice = 'бе'


    def milking(self):
        print('Животное можно доить!')


    def cuting(self):
        print('Стрижка шерсти.')


class Goat(Animal):
    subarea = 'сарай'
    voice = 'ме'


    def milking(self):
        print('Животное можно доить')


    def get_fluff(self):
        print('Получение козьего пуха')


class Duck(Animal):
    subarea = 'птичник'
    voice = 'кря'


    def get_egg(self):
        print('Сбор утиных яиц.')
    
    
class Chicken(Animal):
    subarea = 'курятник'
    voice = 'ко-ко'


    def get_egg(self):
        print('Сбор куриных яиц.')
    

class Goose(Animal):
    subarea = 'гусятник'
    voice = 'га-га'


    def get_egg(self):
        print('Сбор гусиных яиц.')


    def get_fat(self):
        print('Добыча гусиного жира.')


    def get_fluff(self):
        print('Получение гусиного пуха.')


def cow_info():
    cow = Cow('корова Бурёнка')
    print('Тип животного - {0}'.format(cow.kind))
    print('Общее наименование животного - {0}'.format(cow.common_name))
    print('Имя животного - {0}'.format(cow.name))
    print('Место обитания животного - {0}'.format(cow.area))
    print('Место размещения животного - {0}'.format(cow.subarea))
    print('Голос животного - {0}'.format(cow.voice))
    cow.feeding()
    cow.eating()
    cow.milking()


def pig_info():
    pig = Pig('поросёнок Хрюша')
    print('Тип животного - {0}'.format(pig.kind))
    print('Общее наименование животного - {0}'.format(pig.common_name))
    print('Имя животного - {0}'.format(pig.name))
    print('Место обитания животного - {0}'.format(pig.area))
    print('Место размещения животного - {0}'.format(pig.subarea))
    print('Голос животного - {0}'.format(pig.voice))
    pig.feeding()
    pig.eating()
    pig.get_fat()


def sheep_info():
    sheep = Sheep('овца Долли')
    print('Тип животного - {0}'.format(sheep.kind))
    print('Общее наименование животного - {0}'.format(sheep.common_name))
    print('Имя животного - {0}'.format(sheep.name))
    print('Место обитания животного - {0}'.format(sheep.area))
    print('Место размещения животного - {0}'.format(sheep.subarea))
    print('Голос животного - {0}'.format(sheep.voice))
    sheep.feeding()
    sheep.eating()
    sheep.milking()
    sheep.cuting()


def goat_info():
    goat = Goat('коза Машка')
    print('Тип животного - {0}'.format(goat.kind))
    print('Общее наименование животного - {0}'.format(goat.common_name))
    print('Имя животного - {0}'.format(goat.name))
    print('Место обитания животного - {0}'.format(goat.area))
    print('Место размещения животного - {0}'.format(goat.subarea))
    print('Голос животного - {0}'.format(goat.voice))
    goat.feeding()
    goat.eating()
    goat.milking()
    goat.get_fluff()


def duck_info():
    duck = Duck('утка Кряква')
    print('Тип животного - {0}'.format(duck.kind))
    print('Общее наименование животного - {0}'.format(duck.common_name))
    print('Имя животного - {0}'.format(duck.name))
    print('Место обитания животного - {0}'.format(duck.area))
    print('Место размещения животного - {0}'.format(duck.subarea))
    print('Голос животного - {0}'.format(duck.voice))
    duck.feeding()
    duck.eating()
    duck.get_egg()


def chicken_info():
    chicken = Chicken('курица Пеструшка')
    print('Тип животного - {0}'.format(chicken.kind))
    print('Общее наименование животного - {0}'.format(chicken.common_name))
    print('Имя животного - {0}'.format(chicken.name))
    print('Место обитания животного - {0}'.format(chicken.area))
    print('Место размещения животного - {0}'.format(chicken.subarea))
    print('Голос животного - {0}'.format(chicken.voice))
    chicken.feeding()
    chicken.eating()
    chicken.get_egg()


def goose_info():
    goose = Goose('гусь Дональд')
    print('Тип животного - {0}'.format(goose.kind))
    print('Общее наименование животного - {0}'.format(goose.common_name))
    print('Имя животного - {0}'.format(goose.name))
    print('Место обитания животного - {0}'.format(goose.area))
    print('Место размещения животного - {0}'.format(goose.subarea))
    print('Голос животного - {0}'.format(goose.voice))
    goose.feeding()
    goose.eating()
    goose.get_egg()
    goose.get_fat()
    goose.get_fluff()


def animal_info():
    cow_info()
    print('***')
    pig_info()
    print('***')
    sheep_info()
    print('***')
    goat_info()
    print('***')
    duck_info()
    print('***')
    chicken_info()
    print('***')
    goose_info()


animal_info()
