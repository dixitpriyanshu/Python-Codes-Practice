import tkinter as tk

THEME_COLOR = "#375362"

class QuizInterface:

    

    def __init__(self) -> None:
        self.score = 0
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg= THEME_COLOR, padx= 20, pady= 20)
        #-----------LABEL------------#

        self.score_label = tk.Label(text= f"Score: {self.score}", fg = "white", bg= THEME_COLOR)
        self.score_label.grid(row= 0, column= 1)


        #-------CANVAS--------------#
        self.canvas = tk.Canvas(width= 300, height= 250, bg= "white")
        self.canvas.create_text(150, 125, text= "Here goes the question", font= ("Arial", 20,"italic"), fill= THEME_COLOR)
        self.canvas.grid(row= 1, column= 0, columnspan= 2, pady= 50)

        #-------PHOTOIMAGE-------------#

        true_img = tk.PhotoImage(file = "Day 34 - Trivia API GUI Quiz/images/true.png")
        false_img = tk.PhotoImage(file = "Day 34 - Trivia API GUI Quiz/images/false.png")
        
        #---------BUTTONs-----------#
        self.true_button = tk.Button(image= true_img, highlightthickness= 0)
        self.true_button.grid(row= 2, column= 0)
        self.false_button = tk.Button(image= false_img, highlightthickness= 0)
        self.false_button.grid(row= 2, column= 1)








        self.window.mainloop()