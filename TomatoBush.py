
class Tomato:
    states = {
        'Отсутствует': 0,
        'Цветение': 1,
        'Зеленый': 2,
        'Красный': 3
    }

    def __init__(self, index): 
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3
    

class TomatoBush:  
    def __init__(self, num):  
        self.tomatoes = [Tomato(index) for index in range(num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):  
        self.name = name
        self._plant = plant

    def work(self):
        print(f'{self.name} работает...')
        self._plant.grow_all()
        print(f'{self.get_status()}')

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f'{self.name} собирает урожай...')
            self._plant.give_away_all()
            print('Сбор урожая завершен')
        else:
            print('Слишком рано! Ваше растение еще зеленое и не созрело.')

    def get_status(self):
        return '\n'.join([f'Tomato {i._index} is '
                          f'{list(Tomato.states.keys())[i._state]}'
                          for i in self._plant.tomatoes])

    @staticmethod
    def knowledge_base():
        print('Время сбора урожая томатов в идеале должно происходить\n'
              'когда плоды становятся зрелыми зелеными и\n'
              'затем дать им дозреть на лозе.\n'
              'Это предотвращает раскалывание или ушибы\n'
              'и позволяет контролировать процесс созревания.')




if __name__ == '__main__': 
    Gardener.knowledge_base()

    bush = TomatoBush(3)
    gardener = Gardener('Adam', bush)

    for i in range(3):
        gardener.work()

    gardener.harvest()

    while not bush.all_are_ripe():
        gardener.work()

    gardener.harvest()
        




if __name__ == '__main__':
    Gardener.knowledge_base()

    bush = TomatoBush(3)
    gardener = Gardener('Adam', bush)

    for i in range(3):
        gardener.work()

    gardener.harvest()

    while not bush.all_are_ripe():
        gardener.work()

    gardener.harvest()

