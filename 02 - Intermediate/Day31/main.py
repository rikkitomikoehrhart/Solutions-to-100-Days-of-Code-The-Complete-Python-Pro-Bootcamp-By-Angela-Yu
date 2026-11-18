import os
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FUNCTIONALITY ---------------------------- #
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=CARD_FRONT)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=CARD_BACK)


# ---------------------------------- UI --------------------------------- #
window = Tk()
CARD_BACK = PhotoImage(file="./images/card_back.png")
CARD_FRONT = PhotoImage(file="./images/card_front.png")
RIGHT_IMG = PhotoImage(file="./images/right.png")
WRONG_IMG = PhotoImage(file="./images/wrong.png")
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=CARD_FRONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")


wrong_button = Button(image=WRONG_IMG, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=RIGHT_IMG, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)


next_card()

# Workaround for a macOS Tk bug: the window doesn't draw until it's
# resized,so nudge the size by 1px and back once the window is on screen.
def force_redraw():
    width, height = window.winfo_width(), window.winfo_height()
    window.geometry(f"{width + 1}x{height}")
    window.after(10, lambda: window.geometry(f"{width}x{height}"))

window.after(100, force_redraw)
window.mainloop()