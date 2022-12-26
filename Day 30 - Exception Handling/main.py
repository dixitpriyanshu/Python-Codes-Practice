import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
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

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website:{
            "email" : username,
            "password" : password
        }
    }
    data_loc = "Day 30 - Exception Handling/data.json"
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open(data_loc, "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(data_loc, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open(data_loc, "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

window =  tk.Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

canvas = tk.Canvas(width= 200, height= 200, highlightthickness= 0)

lock_img = tk.PhotoImage(file= "Day 30 - Exception Handling/logo.png")
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