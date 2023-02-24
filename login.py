from tkinter import *
from tkinter import  messagebox
import json


def get_data():
    email = email_entry.get()
    password = password_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Sorry", message="You dont have an account")
    else:
        if email and data[email]['password'] == password:
            messagebox.showinfo(title=email, message=f"hello welcome back {data[email]['name']}")
        else:
            messagebox.showwarning(title="Sorry", message="You dont have an account")
    finally:
        email_entry.delete(0, END)
        password_entry.delete(0, END)

window = Tk()
window.title("Registration Form")
window.config(padx=60, pady=40)

#Label
title_label = Label(text="Login", font=("Arial", 20, "bold"))
title_label.grid(column=0, row=0, columnspan=2, pady=20)
email_label = Label(text="Email")
email_label.grid(column=0, row=1, pady=10, padx=20)
password_label = Label(text="Password")
password_label.grid(column=0, row=2, pady=10, padx=20)


#Entry
email_entry = Entry(width=30)
email_entry.grid(column=1, row=1)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=2)

#Button
register_button = Button(text="Login", bg="yellow", highlightthickness=0, width=20, command=get_data)
register_button.grid(column=0, row=6, columnspan=2, pady=40)


window.mainloop()