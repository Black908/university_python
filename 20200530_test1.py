"""
from tkinter import *
root = Tk()
root.mainloop()

from tkinter import *
root = Tk()

label = Label (root, text="Welcome, Please input your name")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="확인")
button.pack()

root.mainloop()

from tkinter import *
def buttonclick():
    ent_text = et.get()
    print(ent_text)
    lb['fg'] = ent_text
    et.delete

window = Tk()
window.title("버튼 이벤트 만들기") #창의 제목
lb = Label(window, text="아래 빈칸에 텍스트를 입력하세요", width=40)
et = Entry(window, width=40)
bt = Button(window, text="확인", width=40, bg="pink", command=buttonclick)
lb.pack()
et.pack()
bt.pack()
window.mainloop()
"""
from tkinter import *
from tkinter import messagebox
id_list = ['abcd', 'hong', 'kim']
pw_list = ['1111', '2222', '444']

def check_id_pw(id_value, pw_value):
    id_ok = id_value in id_list
    pw_ok = pw_value in pw_list

    if id_value == id_list and pw_value == pw_list:
        print('True')
    else:
        print('False')
    return

def ok_button_click():
    print('ok button clicked')
    id_value = id_entry.get()
    print('read id:', id_value)
    pw_value = pw_entry.get()
    print('read pw:', pw_value)

    check_value = check_id_pw(id_value, pw_value)

    if check_value ==True:
        messagebox.showinfo("알림","성공")
    else:
        messagebox.showinfo("알림","실패")

root = Tk()
