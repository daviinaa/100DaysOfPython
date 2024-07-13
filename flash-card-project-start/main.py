BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
current_card = {}

# use pandas to read csv and change to dataframe
try:
    french_words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words = pandas.read_csv("data/french_words.csv")
# ------------------------ convert dataframe to dictionary --------------#
else:
    list_of_fwords = french_words.to_dict(orient="records")

# ------------------------ right button function --------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    # -------------- pick random choice in list ------------------ #
    current_card = random.choice(list_of_fwords)
    french_word = current_card["French"]
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_tittle, text="French", fill="black")
    canvas.itemconfig(current_image, image=frontcard_png)
    flip_timer = window.after(3000, func=flip_card)


# ------------------------ change to english after 3 seconds ----------------#
def flip_card():
    # -------------- pick random choice in list ------------------ #
    canvas.itemconfig(current_image, image=backcard_png)
    canvas.itemconfig(card_tittle, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ------------------------ wrong button function --------------------------- #
def remove():
    list_of_fwords.remove(current_card)
    print(len(list_of_fwords))
    # convert a list to a dataframe
    data = pandas.DataFrame(list_of_fwords)
    # Dataframe to csv
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
frontcard_png = PhotoImage(file="images/card_front.png")
backcard_png = PhotoImage(file="images/card_back.png")
current_image = canvas.create_image(400, 263, image=frontcard_png)
card_tittle = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# buttons
right_png = PhotoImage(file="images/right.png")
right_button = Button(image=right_png, highlightthickness=0, command=remove)
right_button.grid(column=1, row=2)

wrong_png = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_png, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=2)

next_card()

window.mainloop()