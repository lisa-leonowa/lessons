from tkinter import *
def enter():
    global new_win, flag, login
    login = ent_login.get()
    password = ent_password.get()
    if len(login) == len(password):
        if flag:
            close()
            flag = False
        new_window()

def new_window():
    global new_win, flag, login
    flag = True
    new_win = Toplevel(window)
    new_win.title("Социальная сеть")
    new_win.geometry("400x200")
    new_win['bg'] = 'LightBlue1'
    lbl_info = Label(new_win, text='Вход успешно произведен!', bg='LightBlue1')
    lbl_info.place(x=50, y=40)

    lbl_user = Label(new_win, text=f'Пользовать с логином: {login}', bg='LightBlue1')
    lbl_user.place(x=50, y=70)
    btn_exit = Button(new_win, text="Выход", width=10, command=close)
    btn_exit.place(x=60, y=100)

def close():
    new_win.destroy()

flag = False
window = Tk()
window.title("Социальная сеть")
window.geometry("400x200")
window['bg'] = 'LightBlue1'

lbn_login = Label(window, text="Введите логин", bg='LightBlue1')
lbn_login.place(x=80,y=40)

lbn_password = Label(window, text='Введите пароль', bg='LightBlue1')
lbn_password.place(x=80,y=70)

ent_login = Entry(window)
ent_login.place(x=180, y=40)

ent_password = Entry(window)
ent_password.place(x=180, y=70)

btn_enter = Button(window, text="Войти", width=10, command=enter)
btn_enter.place(x=150, y=100)

window.mainloop()