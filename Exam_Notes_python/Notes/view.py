from tkinter import *
import data_note as dn
import datetime

path_csv = 'Exam_Notes_python/Notes/note_file.csv'
date = str(datetime.datetime.now().ctime())

def add_data_note(index = END):
    if txt_1.get() == "":
        date = str(datetime.datetime.now().ctime())
        txt1 = date
    else: txt1 = txt_1.get()
    list_phon.insert(index, txt1 + ',' + txt_2.get() + ',' + txt_3.get("1.0",'end'))
    save()
    del_window_text()
    return

def del_window_text():
    x = txt_1.get()
    txt_1.delete(0, END)
    txt_2.delete(0, END)
    txt_3.delete("1.0", END)
    return

def save(arg = 'r+'):
    f = open(path_csv, arg, encoding='utf-8')
    f.writelines
    f.writelines("".join(list_phon.get(0, END)))
    f.close()
    return

def delete_data_note(select = END):
    select = list(list_phon.curselection())
    select.reverse()
    for i in select:
        list_phon.delete(i)
    save('w')
    return

def save_changes():
    select = list(list_phon.curselection())
    select.reverse()
    for i in select:
        list_phon.delete(i)
    add_data_note()
    

def changes_data_note():
    del_window_text()
    select = list(list_phon.curselection())
    chang_str = list_phon.get(select).split(',')
    print(chang_str)
    date = str(datetime.datetime.now().ctime())
    txt_1.insert(0, date)
    txt_2.insert(1, chang_str[1])
    txt_3.insert('1.0', chang_str[2])
    return 

window = Tk()
window.title("ЗАПИСКИ")
window.geometry('1300x600')

args1 = {'bg' : "pale green", 'fg' : "blue", 'font' : ("Arial Bold", 12), 'activebackground' : "green"}
args2 = {'fg' : "navy", 'font' : ("Arial Bold", 12)}
lc = dn.one_note ()

lb_l = Label(window, text = lc[0], **args2).place(x = 10, y = 10)
txt_1 = Entry(window, width = 25, font = ("Arial Bold", 12))                                           
txt_1.place(x = 200, y = 10)
date = str(datetime.datetime.now().ctime())
txt_1.insert(0, date)
lb_2 = Label(window, text = lc[1], **args2)                                     
lb_2.place(x = 10, y = 50)
txt_2 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_2.place(x = 200, y = 50)
txt_2.insert(0, 'Новая записка')
lb_3 = Label(window, text = lc[2], **args2)                                     
lb_3.place(x = 10, y = 90)
txt_3 = Text(window, width = 25, height = 18, font = ("Arial Bold", 12))  
txt_3.place(x = 200, y = 90)

btn = Button(window, width = 25, text = "Добавить заметку", **args1, command = add_data_note)
btn.place(x = 600, y = 450)
btn = Button(window, width = 25, text = "Удалить заметку", **args1, command = delete_data_note)
btn.place(x = 900, y = 450)
btn = Button(window, width = 25, text = "Изменить заметку", **args1, command = changes_data_note)
btn.place(x = 600, y = 500)
btn = Button(window, width = 25, text = "Сохранить изменения", **args1, command = save_changes)
btn.place(x = 900, y = 500)

list_phon = Listbox(width = 120, height = 25, selectmode = EXTENDED) 
list_phon.place(x = 500, y = 10)
scroll_y = Scrollbar(orient="vertical", command=list_phon.yview)
scroll_y.place(x = 1235, y = 50)
list_phon.config(yscrollcommand = scroll_y.set)
scroll_x = Scrollbar(orient="horizontal", command=list_phon.xview)
scroll_x.place(x = 550, y = 425)
list_phon.config(xscrollcommand = scroll_x.set)

f = open(path_csv, 'r+', encoding='utf-8')
for x in f:
    list_phon.insert(END,x)
f.close()

window.mainloop()
