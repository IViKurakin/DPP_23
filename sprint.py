import turtle
import random
import time

''' Смешение логики и представления (логика настроек программы и логика гонки находятся в одном месте). '''

# Глобальные переменные
'''! Использование глобальных переменных в функциях.'''
sc = None
t1 = None
t2 = None
win = False

# Функция базовой настройки игры
''' Логика настроек программы '''
def setup():
    global sc, t1, t2
    sc = turtle.Screen()
    sc.setup(500,500)
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t1.color('red')
    t2.color('green')
    t1.shape('turtle')
    t2.shape('turtle')
    t1.penup()
    t2.penup()
    t1.goto(-150,50)
    t2.goto(-150,-50)

# Функция для запуска игры
''' Отсутствие структуры (весь алгоритм написан в функциях, а не классах).'''
def start_race():
    global win
    for i in range(100):
        if not win:
            t1.forward(random.randint(1,5))
            time.sleep(1)
            t2.forward(random.randint(1,5))
            check_winner()
        else:
            break

# Функция для определения победителя
''' Отсутствие структуры (весь алгоритм написан в функциях, а не классах).'''
def check_winner():
    global win
    if t1.xcor() > 150:
        print('Победила красная черепашка')
        win = True
    if t2.xcor() > 150:
        print('Победила зеленая черепашка')
        win = True

# Код запуска
''' Логика игрового процесса'''
setup()
start_race()


'''! Код невозможно переиспользовать, поскольку он не представляет собой модуль.'''
