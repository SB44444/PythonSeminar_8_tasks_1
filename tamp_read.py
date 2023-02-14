def adding_dict(student_name):   #  Ф-ция заполнения данных 
    dic = made_dic(reading_data(student_name))  # Ф-ция создаёт из строки вида "Kat: ; M: 1 5 3 5 4; R: 5 4 5" список словарей
    print(reading_data(student_name))
    # print(dic)     
    hold = '0'
    subj_tamp = ' ' + input('Ведите название предмета \n:  ')    #  Добавили пробел для читаемости
    for i in range(len(dic)):       
        if subj_tamp in dic[i]:            #  В цикле если предмет есть в списке в словаре какого-либо эл-та
            print(subj_tamp, dic[i][subj_tamp])  # Выводим предмет и строку оценок
            while hold !='':
                hold = input('Ведите оценку от 1 до 5: Если все отметки проставлены нажмите ENTER\n:  ')
                if hold == '1' or hold == '2' or hold  == '3' or hold == '4' or hold == '5':
                    dic[i][subj_tamp] += ' ' + hold  # Выставляем оценки, если это верные цифры 
                print(subj_tamp, dic[i][subj_tamp])
            write_csv(student_name, dic)             #  Запуск ф-ции записи
    else:                                  #  Если предмета нет, добавляем словарь в список
        while hold != '':
            hold2 = input('Сохраните нговые данные, нажмите любую букву, ENTER и запустите программу\nДля отмены нажмите только ENTER\n')
            if hold2.isalpha() == True:                    
                dic.append(dict({subj_tamp: ''}))
                write_csv(student_name, dic)         #  Запуск ф-ции записи
                hold =''
    print(reading_data(student_name))   # Выводим  ученика, предмет и строку оценок
    return dic

def write_csv(student_name, dic_lst):  #  Ф-ция добавления данных по предмету в файл csv
    file = '' 
    student_name  += '.csv'     # Запись имени файла с расширением   
    for i in dic_lst:        
        for k, v in i.items():  # Для каждого эл-та списка выодим ключ и значение 
            file += str(k) + ':'  # Дописываем разделители для последующего открытия
            file += str(v) + ';'
    file = file[:-1]          #  Убираем лишнее
    with open(student_name, 'w+', encoding='utf-8') as data: data.write(file)  #  Запись строки в файл

def reading_data(student_name):      # Ф-ция чтения из файла
    student_name += '.csv'           # Запись имени файла с расширением
    with open(student_name, 'r', encoding='utf-8') as data:
        dic = data.read()    # Чтение из файла
    return dic

def made_dic(file_srt):  # Ф-ция создаёт из строки вида "kot: ; M: 1 5 3 5 4; R: 5 4 5" список словарей 
    dic_lst = []
    lst = list(file_srt.split(';'))   # Делим строку на список
    for i in lst:                # Для каждого эл-та списка словарь первый эл-т - ключ второй - значение
        i = i.split(':')
        dic_lst.append({i[0]: i[1]})
    return dic_lst

def create_file_csv(student_name):   #  Ф-ция создания файла
    student_name  += '.csv'
    with open(student_name, 'w+', encoding='utf-8') as data:
        data.write('\n')   




#student_name = 'Kat'   # Kat: ; M: 1 5 3 5 4; R: 5 4 5
#adding_dict(student_name)

