from tkinter import *

def button_clicked():
    my_label.config(text= f"hii! {input.get()}")

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height=300)
window.config(padx= 100,pady= 200)

## Label
my_label = Label(text= "I am a Label", font= ("Arial", 24, "bold"))
my_label.grid(column= 0, row= 0)
my_label.config(padx= 50,pady= 50)

# my_label["text"] = New Text"
# Alternate
my_label.config(text= "Hii")

########  BUtton
button = Button(text= "Click Me", command= button_clicked)
button.grid(column= 1, row= 1)

######    Entry
input = Entry(width= 10)
input.grid(column= 3, row= 2)

new_button = Button(text= "Don't Click Me")
new_button.grid(column= 2,row= 0)


window.mainloop()