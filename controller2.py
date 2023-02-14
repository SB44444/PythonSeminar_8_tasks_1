from os.path import exists
#  from list_filling import write_csv, write_txt, adding_data
#  from methods import #create_file_csv, create_file_txt, screen
#  from dic import adding_dict# , write_csv
from tamp_read import reading_data, create_file_csv, adding_dict
import os

def start2():
    text = input('Для начала работы нажмите любую букву\nДля выхода из программы любую цифру или символ\n - ')
    while text.isalpha() == True: # Если выбрана буква остаемся в меню выбора
        who = input('Преставьтесь, пожалуйста\nЕсли Вы учитель введите t\nЕсли ученик введите s\nДля выхода из программы любую цифру или символ\n - ')
        if who == 's':
            student_name = input('Для просмотра успеваемости введите свою фамилию и имя через пробел\n : ')            
            try:             
                print(reading_data(student_name))            
            except: print('Ученика с такой фомилией нет в сиске учащихся \nПовторите ввод ')
        if who == 't':
            write_view = input('Для записи оценок нажмите любую букву\nДля просмотра успеваемости любую цифру или символ\n -  ')
            if write_view.isalpha() == True:
                student_name = input('Для внесения данных введите фамилию и имя ученика через пробел\n : ')
                try:             
                    print(reading_data(student_name))
                    adding_dict(student_name)           
                except:              
                    create_file_csv(student_name)
                    # adding_dict(student_name)
            else:
                student_name = input('Введите фамилию и имя ученика через пробел для просмотра успеваемости\n : ')
                try:             
                    print(reading_data(student_name))            
                except: print('Ученика с такой фомилией нет в сиске учащихся\nПовторите ввод ')       

        text = input('Для продолжения нажмите любую букву\nДля выхода из программы любую цфру или символ\n - ')
    print('Работа программы завершена') 
