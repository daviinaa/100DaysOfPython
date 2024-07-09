import json
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    if len(pass_entry.get()) > 1:
        pass_entry.delete(0, 'end')
    else:
        pass_entry.insert(0, password)
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    webname = web_entry.get()
    email_user = email_entry.get()
    pword = pass_entry.get()
    new_dict = {
        webname: {
            "email": email_user,
            "password": pword,
        }
    }
    if len(webname) == 0 or len(pword) == 0:
        box_incomplete = messagebox.askokcancel(title="oops", message="Please dont leave any fields empty!")
    else:
        try:
            # reading the existing data
            with open("demo-file2.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("demo-file2.json", "w") as data_file:
                json.dump(new_dict, data_file, indent=4)
        else:
            # updating the data with new dictionary/data
            data.update(new_dict)
            with open("demo-file2.json", "w") as data_file:
                #     save updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')


# ---------------------------- SEARCH --------------------------------- #
def find_password():
    website_input = web_entry.get()
    try:
        with open("demo-file2.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        catching_another = messagebox.showinfo(title="Error", message="No datafile found")
    else:
        if website_input in data:
            email_pass = data[website_input]
            search_answer = messagebox.showinfo(title=website_input, message=f"Email: {email_pass['email']} \n "
                                                                             f"Password: {email_pass['password']}")
        else:
            catching_exception = messagebox.showinfo(title="Error",
                                                     message=f"No details for the {website_input} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=1)

# website label
website = Label(text="Website:", font=("Arial", 16, "normal"))
website.grid(column=0, row=2)

# email label
email = Label(text="Email/Username:", font=("Arial", 16, "normal"))
email.grid(column=0, row=3)

# Password label
password = Label(text="Password:", font=("Arial", 16, "normal"))
password.grid(column=0, row=4)

# website input
web_entry = Entry(width=21)
web_entry.focus()
web_entry.grid(column=1, row=2)

# email Input
email_entry = Entry(width=38)
email_entry.grid(column=1, row=3, columnspan=2)
email_entry.insert(0, "@gmail.com")

# Password Input
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=4)

# generate button
generate_pass = Button(text="Generate Password", command=generate)
generate_pass.grid(column=2, row=4)

# add pass button
add_pass = Button(text="Add", width=36, command=save)
add_pass.grid(column=1, row=5, columnspan=2)

# adding search button
search = Button(text="Search", width=13, command=find_password)
search.grid(column=2, row=2)

window.mainloop()
