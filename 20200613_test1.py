"""
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("로그인하세요.")
root.resizeable(False, False)

id_list = ['abcd','hong','kim']
pw_list = ['1111','2222','444']

def cehck_id_pw(id_value, pw_value):
    print(id_list)
    if id_value in id_list:

        return True

def ok_button_click():
    print('ok button clicked')
    id_value = id_entry.get()
    print('read id:', id_value)
    pw_value = pw_entry.get()
    print('read pw:', pw_value)

    check_value = check_id_pw(id_value, pw_value)


#id_entry = Entry(root, width=30)



label = Label(root, text="ID 입력")
label.pack()

entry = Entry(root)
entry.pack()

label2 = Label(root, text="PW 입력")
label2.pack()

entry2 = Entry(root)
entry2.pack()

button = Button(root, text="로그인", command=ok_button_click)
button.pack()

root.mainloop()



from tkinter import *
r = Tk()
r.title("ID와 PW입력창")
lb1 = Label(r, text="아이디")
lb2 = Label(r, text="비밀번호")
ent1 = Entry(r)
ent2 = Entry(r)
btn = Button(r, text="획인")

lb1.grid(row=0 , column=0)
ent1.grid(row=0, column=1)
lb2.grid(row=1, column=0)
ent2.grid(row=1, column=1)
btn.grid(row=2, column=1)
r.mainloop()
"""


from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
root=Tk()

def fileload():
    messagebox.showinfo("안내","아직 지원하지 않습니다.")
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    f = open("","r")
    #값들을 읽어서 더해주기
    value = f.readlines()
    sum = 0
    for data in value:
        sum = sum+data

    messagebox.showinfo(sum)

def quit():
    root.destroy()
    root.quit()

menubar = Menu(root)

f1=Menu(menubar, tearoff=0)
f1.add_command(label="open", command=fileload)
f1.add_separator()
f1.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=f1)
root.config(menu=menubar)

root.mainloop()
