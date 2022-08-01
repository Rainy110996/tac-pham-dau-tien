
import tkinter
import tkinter.messagebox


def selection(var, password):
    value = var.get()
    if value == 1:
        password.config(show = "")
    else:
        password.config(show = "*")


def get_data(entry_username, entry_password):
    text_username = entry_username.get()
    text_password = entry_password.get()
    if text_username == "admin" and text_password == "admin":
        tkinter.messagebox.showinfo("Thông báo", "Đăng nhập thành công !")
    else:
        tkinter.messagebox.showwarning("Thông báo", "Đăng nhập thất bại")


app = tkinter.Tk()
app.title("Hello !!!")
app.geometry("720x480")

checkVar = tkinter.IntVar()

frame = tkinter.Frame(app, width=800, height=600, background="#DCDCDC")
frame.pack(anchor = tkinter.CENTER)

username = tkinter.Label(frame, text = 'Username:', background='#DCDCDC')
username.place(in_= frame, anchor="c", relx=.15, rely=.20)

entry_username = tkinter.Entry(frame)
entry_username.place(in_= frame, anchor="c", relx=.30, rely=.20)

password = tkinter.Label(frame, text = "Password:", background='#DCDCDC')
password.place(in_= frame, anchor="c", relx=.15, rely=.30)

entry_password = tkinter.Entry(frame, show = "*")
entry_password.place(in_= frame, anchor="c", relx=.30, rely=.30)

login = tkinter.Button(frame, text = "Login", width=16, background= "gray")
login.config(command= lambda: get_data(entry_username, entry_password))
login.place(in_= frame, anchor="c", relx=.30, rely=.40)

savepass = tkinter.Checkbutton(frame, background='#DCDCDC', variable = checkVar)
savepass.config(onvalue = 1, offvalue = 0, command = lambda: selection(checkVar, entry_password))
savepass.place(in_= frame, anchor="c", relx=.15, rely=.40)

forgotpass = tkinter.Label(frame, text = 'Forgot Password ?', background='#DCDCDC')
forgotpass.place(in_= frame, anchor="c", relx=.30, rely=.50)


app.mainloop()
