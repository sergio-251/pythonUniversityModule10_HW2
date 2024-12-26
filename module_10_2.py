# Потоки на классах
import threading, time
class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.__enemies = 100

    def run(self):
        print(f'{self.name}, <Имя рыцаря>, на нас напали!')
        days = 0
        while self.__enemies > 0:
            days += 1
            self.__enemies -= self.power
            time.sleep(1)
            print(f'{self.name} сражается {days} день(дня)..., осталось {self.__enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
