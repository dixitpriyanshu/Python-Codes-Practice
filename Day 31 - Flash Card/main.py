import tkinter as tk
import random
import pandas
# -------------- CONSTANTS ------------#

BACKGROUND_COLOR = "#B1DDC6"
#-----------GLOBAL-----------#
current_card = {}
to_learn ={}
#---------------- FILE ACTIONS------------#
try:
    data = pandas.read_csv("Day 31 - Flash Card/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Day 31 - Flash Card/data/french_words.csv")
    to_learn = original_data.to_dict(orient= "records")
else:
    to_learn = data.to_dict(orient= "records")

#---------------- Next Card----------#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(card_background, image = card_front_img)
    flip_timer = window.after(3000, func= flip_card)
    
# -------------- FLIP CARD ------------#

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image = card_back_img)
#-------------- USER KNOWs THE WORD --------------#

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Day 31 - Flash Card/data/words_to_learn.csv", index= False)
    next_card()

#------------------ UI -----------------#
window = tk.Tk()
window.title("Flashy")
window.config(bg= BACKGROUND_COLOR, padx= 50, pady= 50)
canvas = tk.Canvas(width= 800, height= 526, bg= BACKGROUND_COLOR, highlightthickness= 0)

flip_timer = window.after(3000, func= flip_card)

card_front_img = tk.PhotoImage(file= "Day 31 - Flash Card/images/card_front.png")
card_back_img = tk.PhotoImage(file= "Day 31 - Flash Card/images/card_back.png")
right_img = tk.PhotoImage(file= "Day 31 - Flash Card/images/right.png")
wrong_img = tk.PhotoImage(file= "Day 31 - Flash Card/images/wrong.png")

card_background = canvas.create_image(400, 263, image= card_front_img)
canvas.grid(row= 0,column= 0, columnspan= 2)


# Buttons
known_button = tk.Button(image= right_img, highlightthickness= 0, command= is_known)
known_button.grid(row= 1, column= 1)

unknown_button = tk.Button(image= wrong_img, highlightthickness= 0, command= next_card)
unknown_button.grid(row= 1, column= 0)

# Text

card_title = canvas.create_text(400, 150,text= "", font= ("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263,text= "", font= ("Arial", 60, "bold"))

next_card()

window.mainloop()