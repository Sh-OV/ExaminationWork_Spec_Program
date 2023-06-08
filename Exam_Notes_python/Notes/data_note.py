# модуль, принимающий данные от пользователя (добавление новых заметок)
# и передающий их дальше для обработки в модуль data_subscriber

import datetime

def one_note ():
    note_list = []
    current_date = datetime.datetime.now().ctime()
    note_list.append(current_date)
    name_note = input('Название заметки: ')
    if len(name_note) == 0:
        name_note = "Новая заметка"
    note_list.append(name_note)
    text_note = input('Текст заметки: ')
    note_list.append(text_note)
    return note_list

def input_data():
    question = one_note()
    print('Добавьте новую заметку: ')
    d_0 = input(question[0])
    d_1 = input(question[1])
    d_2 = input(question[2])
    return [d_0, d_1, d_2]


