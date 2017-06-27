class Animal:
    name = 'pet'
    area = 'farm'
    kind = 'cattle and birds'


    def feeding(self):
        print('Кормить!')


    def eating(self):
        print('Животное можно есть!')
        
    
class Cow(Animal):
    subarea = 'hlev'
    voice = 'moo'
    def milking(self):
        print('Доить!')


class Pig(Animal):
    subarea = 'svinarnik'
    voice = 'hryu'
    def get_fat(self):
        print('Приготовление сала!')


class Sheep(Animal):
    subarea = 'ovcharnya'
    voice = 'bea'
    def milking(self):
        print('Доить!')


    def cuting(self):
        print('Стрижка шерсти')


class Goat(Animal):
    subarea = 'saray'
    voice = 'mea'
    def milking(self):
        print('Доить')


    def get_fluff(self):
        print('Получение козьего пуха')


class Duck(Animal):
    subarea = 'ptichnik'
    voice = 'krya'
    def get_egg(self):
        print('Сбор утиных яиц')
    
    
class Chicken(Animal):
    subarea = 'kuryatnik'
    voice = 'co-co'
    def get_egg(self):
        print('Сбор куриных яиц')
    

class Goose(Animal):
    subarea = 'gusyatnik'
    voice = 'ga-ga'
    def get_fat(self):
        print('Добыча гусиного жира')


    def get_fluff(self):
        print('Получение гусиного пуха')
