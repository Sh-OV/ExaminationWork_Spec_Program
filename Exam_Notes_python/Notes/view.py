from cProfile import label
from tkinter import *
import data_note as dn
import logger as lg

path_csv = 'Exam_Notes_python/Notes/note_file.csv'

def add_data_note(index = END):
    list_note.insert(index, txt_1.get() + ',' + txt_2.get() + ',' + txt_3.get() + ',' + '\n')
    save()
    del_window_text()
    return

def del_window_text():
    x = txt_1.get()
    txt_1.delete(0, END)
    txt_2.delete(0, END)
    txt_3.delete(0, END)
    return

def save(arg = 'r+'):
    f = open(path_csv, arg, encoding='utf-8')
    f.writelines("".join(list_note.get(0, END)))
    f.close()
    return

def delete_data_note(select = END):
    select = list(list_note.curselection())
    select.reverse()
    for i in select:
        x = i
        list_note.delete(i)
    save('w')
    return

def save_changes():
    select = list(list_note.curselection())
    add_data_note(select)
    delete_data_note(select)

def changes_data_note():
    select = list(list_note.curselection())
    chang_str = list_note.get(select).split(',')
    print(chang_str)
    txt_1.insert(0, chang_str[0])
    txt_2.insert(1, chang_str[1])
    txt_3.insert(2, chang_str[2])
   
    return 
   

window = Tk()
window.title("ЗАМЕТКИ")
window.geometry('1500x600')

args1 = {'bg' : "pale green", 'fg' : "blue", 'font' : ("Arial Bold", 12), 'activebackground' : "green"}
args2 = {'fg' : "navy", 'font' : ("Arial Bold", 12)}
lc = dn.input_data()

lb_l = Label(window, text = lc[0], **args2)                                     
lb_l.place(x = 10, y = 10)
txt_1 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_1.place(x = 250, y = 10)
lb_2 = Label(window, text = lc[1], **args2)                                     
lb_2.place(x = 10, y = 50)
txt_2 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_2.place(x = 250, y = 50)
lb_3 = Label(window, text = lc[2], **args2)                                     
lb_3.place(x = 10, y = 90)
txt_3 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_3.place(x = 250, y = 90)


btn = Button(window, width = 25, text = "Добавить заметку", **args1, command = add_data_note)
btn.place(x = 500, y = 450)
btn = Button(window, width = 25, text = "Удалить заметку", **args1, command = delete_data_note)
btn.place(x = 1000, y = 450)
btn = Button(window, width = 25, text = "Изменить", **args1, command = changes_data_note)
btn.place(x = 600, y = 500)
btn = Button(window, width = 25, text = "Сохранить изменение", **args1, command = save_changes)
btn.place(x = 900, y = 500)

list_note = Listbox(width = 120, height = 25, selectmode = EXTENDED) 
list_note.place(x = 500, y = 10)
scroll_y = Scrollbar(orient="vertical", command=list_note.yview)
scroll_y.place(x = 1235, y = 50)
list_note.config(yscrollcommand = scroll_y.set)
scroll_x = Scrollbar(orient="horizontal", command=list_note.xview)
scroll_x.place(x = 550, y = 425)
list_note.config(xscrollcommand = scroll_x.set)

f = open(path_csv, 'r+', encoding='utf-8')
for x in f:
    list_note.insert(END,x)
f.close()

window.mainloop()

# --------------------------------------------------------------------
logger = lg.get_logger(__name__)

def process(msg):
    logger.info("Перед процессом")
    print(msg)
    logger.info("После процесса")
# ---------------------------------------------------------------------
