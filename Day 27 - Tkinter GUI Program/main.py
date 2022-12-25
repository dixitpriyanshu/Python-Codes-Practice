from tkinter import *

def convert():
    miles = int(miles_entry.get())
    km = miles * 1.6
    answer_label.config(text= f"{km}")

root = Tk()
root.title("Converter")
root.minsize(width= 100, height= 80)
root.config(padx= 20,pady= 20)

miles_label = Label(text= "miles")
km_label = Label(text= "km")
equal_label = Label(text= "is equal to")
answer_label = Label(text= "0")
miles_entry = Entry(width= 10)
calculate_button = Button(text= "Calculate", command=convert)

miles_entry.grid(column= 1, row= 0)
miles_label.grid(column= 2, row= 0)
equal_label.grid(column= 0, row= 1)
answer_label.grid(column= 1, row= 1)
km_label.grid(column= 2, row= 1)
calculate_button.grid(column= 1, row= 2)


root.mainloop()