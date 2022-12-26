import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    print(password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or password == "" or username == "":
        messagebox.showinfo(title= "Oops", message= "Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title= website, message= f"These are the details entered: \nEmail: {username}\nPassword: {password} \nIs is ok to save?")

        if is_ok:
            with open("Day 29 - Password Manager/data.txt", "a") as data:
                data.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

window =  tk.Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

canvas = tk.Canvas(width= 200, height= 200, highlightthickness= 0)

lock_img = tk.PhotoImage(file= "Day 29 - Password Manager/logo.png")
canvas.create_image(100, 100, image= lock_img)
canvas.grid(column= 1,row= 0)

#Labels

website_label = tk.Label(text= "Website:")
website_label.grid(column= 0, row= 1)

username_label = tk.Label(text= "Email/Username:")
username_label.grid(column= 0, row= 2)

password_label = tk.Label(text= "Password:")
password_label.grid(column= 0,row=3)

#Entries

website_entry = tk.Entry(width= 50)
website_entry.grid(column=1, row=1, columnspan= 2)
website_entry.focus()

username_entry = tk.Entry(width= 50)
username_entry.grid(column= 1, row=2, columnspan= 2)
username_entry.insert(0, "priyanshudixit2910@gmail.com")

password_entry = tk.Entry(width= 32)
password_entry.grid(column= 1, row=3)

#Buttons

password_button = tk.Button(text= "Generate Password", command= generate_password)
password_button.grid(column= 2, row=3)

add_button = tk.Button(text= "Add", width= 43, command= save_password)
add_button.grid(column= 1, row= 4, columnspan= 2)

window.mainloop()