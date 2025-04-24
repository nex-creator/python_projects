from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}
#reading file using pandas
try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient = "records")# convert dataframe to dictionary in list of dictionary

#button function
def next_card():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title , text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(canvas_image, image = front_image)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image = back_image)
    canvas.itemconfig(card_title, text="English",fill = "green")
    canvas.itemconfig(card_word, text=current_card["English"], fill = "green")
def is_known():
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv("words_to_learn.csv", index = False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx= 50,pady=50, bg = BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_card)

# retrieve images
front_image = PhotoImage(file = "card_front.png")
back_image = PhotoImage(file = "card_back.png")
right_image = PhotoImage(file= "right.png")
wrong_image = PhotoImage(file = "wrong.png")

#Canvas
canvas = Canvas(width = 800 , height = 526)
canvas_image = canvas.create_image(400,263,image = front_image)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0 , column = 0, columnspan=2)
# Canvas text
card_title = canvas.create_text(400,150,text= "Title", fill = "black", font =("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text= "Word" , fill = "black", font =("Ariel",60,"bold"))

#buttons
wrong_button = Button(image = wrong_image, highlightthickness= 0,command = next_card)
wrong_button.grid(row = 1, column =0)
right_button = Button(image = right_image, highlightthickness= 0, command = is_known)
right_button.grid(row= 1, column = 1)

next_card()

window.mainloop()

