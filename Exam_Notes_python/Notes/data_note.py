# модуль, принимающий данные от пользователя (добавление новых записок)


def one_note ():
    my_list = []
    pc_0 = 'Дата: '
    my_list.append(pc_0)
    pc_1 = 'Название записки: '
    my_list.append(pc_1)
    pc_2 = 'Текст записки: '
    my_list.append(pc_2)
    return my_list

def input_data():
    question = one_note ()
    d_0 = input(question[0])
    d_1 = input(question[1])
    d_2 = input(question[2])
    return [d_0, d_1, d_2]


