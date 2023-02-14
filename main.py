from controller2 import start2
import os

clear = lambda: os.system('cls') # Очиста терминала
clear()
# os.system('cls')

def main(): # Функция запуска
    start2() # Функция старта основной программы

if __name__ == '__main__':   # Проверка имени функции запуска программы
    main()