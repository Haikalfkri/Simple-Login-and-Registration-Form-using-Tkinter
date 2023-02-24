from tkinter import *
from tkinter import messagebox
import json

def get_data():
    name = name_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    new_data = {
        email: {
            "name": name,
            "password": password,
            "contact": contact
        }
    }


    if len(name) == 0 or len(password) == 0 or len(email) == 0 or len(contact) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any field empty")
    else:
        confirm = messagebox.askokcancel(title=email, message=f"Name: {name}\nContact: {contact}"
                                                              f"\nPassword: {password}\nAre you okay to save?")
        if confirm:
            try:
                with open("data.json", 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                name_entry.delete(0, END)
                password_entry.delete(0, END)
                contact_entry.delete(0, END)
                email_entry.delete(0, END)


window = Tk()
window.title("Registration Form")
window.config(padx=60, pady=40)

#Label
title_label = Label(text="Registration", font=("Arial", 20, "bold"))
title_label.grid(column=0, row=0, columnspan=2, pady=20)
email_label = Label(text="Email")
email_label.grid(column=0, row=1, pady=10, padx=20)
name_label = Label(text="Name")
name_label.grid(column=0, row=2, pady=10, padx=20)
contact_label = Label(text="Contact")
contact_label.grid(column=0, row=3, pady=10, padx=20)
password_label = Label(text="Password")
password_label.grid(column=0, row=4, pady=10, padx=20)


#Entry
email_entry = Entry(width=30)
email_entry.grid(column=1, row=1)
name_entry = Entry(width=30)
name_entry.grid(column=1, row=2)
contact_entry = Entry(width=30)
contact_entry.grid(column=1, row=3)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=4)

#Button
register_button = Button(text="Register", bg="yellow", highlightthickness=0, width=20, command=get_data)
register_button.grid(column=0, row=6, columnspan=2, pady=40)


window.mainloop()