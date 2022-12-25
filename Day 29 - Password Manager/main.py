import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

username_entry = tk.Entry(width= 50)
username_entry.grid(column= 1, row=2, columnspan= 2)

password_entry = tk.Entry(width= 32)
password_entry.grid(column= 1, row=3)

#Buttons

password_button = tk.Button(text= "Generate Password")
password_button.grid(column= 2, row=3)

add_button = tk.Button(text= "Add", width= 43)
add_button.grid(column= 1, row= 4, columnspan= 2)

window.mainloop()